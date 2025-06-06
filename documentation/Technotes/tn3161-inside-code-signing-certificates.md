# TN3161: Inside Code Signing: Certificates

**Framework**: Technotes

Learn how code signing uses certificates to identify code authors.

#### Overview

[`TN3125: Inside Code Signing: Provisioning Profiles`](tn3125-inside-code-signing-provisioning-profiles.md) explains how Apple platforms use provisioning profiles to authorize the execution of third-party code.  A provisioning profile ties together five criteria: who, what, where, when, and how.  In the case of the who, TN3125 describes how every profile includes a certificate for each developer covered by that profile.  However, it doesn’t go into details as to what a certificate is.  This technote aims to fill in those details.

For advice on the day-to-day management of code-signing identities, see [`Distribution`](https://developer.apple.com/documentation/Xcode/distribution) and [`Developer Account Help`](https://developer.apple.comhttps://developer.apple.com/help/account/).

##### About This Technote Series

Code signing is a foundational technology on all Apple platforms.  Many documents that discuss code signing focus on solving a specific problem.  The  technotes peek behind the code signing curtain, to give you a better understanding of how it works.  For a list of all the technotes in this series, see the introduction in [`TN3125: Inside Code Signing: Provisioning Profiles`](tn3125-inside-code-signing-provisioning-profiles.md).

> ❗ **Important**: The  technotes discuss code signing details that aren’t considered API.  The structure of a code signature has changed numerous times in the past and may well change again in the future.  Don’t encode this information in your product.  When signing code, use Xcode (all platforms) or the `codesign` tool (macOS only).  To get information or validate a code signature, use the `codesign` tool or the [`Code Signing Services`](https://developer.apple.com/documentation/Security/code-signing-services) API.  Apple updates these facilities to accommodate any changes to the code signature structure as they roll out.

#### Public Key Infrastructure

To understand certificates you must first understand a little about public key cryptography and its associated public key infrastructure (PKI).

> **Note**: Many of the Apple-specific processes described in this section are formally documented on the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) page.

##### Public Key Cryptography

Modern cryptography uses two different key systems.  Symmetric key cryptography has the same key for both encryption and decryption.  You encrypt a message with a key and anyone with that key can decrypt it.  Public key cryptography uses clever mathematics to create asymmetric key pairs.  You publish your public key widely.  Anyone can send you a message by encrypting it with that public key.  You retain the private key and use that to decrypt the message.  As long as you keep the private key secret, only you can read these messages.

##### Digital Signatures

Asymmetric key pairs also allow for digital signatures.  You keep the private key to yourself and you publish your public key.  If you sign a message with your private key, anyone can verify that signature with your public key.

> **Note**: With some public key algorithms, signing a message is equivalent to encrypting a hash of that message, but that’s not universally true.  It’s best to think of encryption and signing as two conceptually different tasks.

Digital signatures are central to code signing.  Think of your code as a message which you sign and the operating system verifies before execution.  This verification has two steps:

1. Verify the signature itself, that is, nothing has changed since it was signed by your private key.
2. Evaluate whether your public key is trusted in this context.

This second step uses certificates.

##### Digital Certificate

In the real world, a certificate is a document where the issuer attests to some facts about the subject.  For example, in your birth certificate:

- The issuer is the regional authority of your birth.
- The subject is you.
- The facts are your name, date of birth, parents, and so on.

This system relies on the fact that real world certificates are non-trivial to forge: They’re printed on fancy paper, use special stamps, wax seals, and so on.

A digital certificate has the same goal as a real certificate: The issuer attests to some facts about the subject.  However, it can’t use fancy paper to prevent forgeries.  Instead, a digital certificate relies on public key cryptography.

Apple code signing uses the X.509 standard for digital certificates.  An X.509 certificate contains five pieces of information:

- Details of the issuer
- Details of the subject
- The subject’s public key
- Required facts, like the valid date range
- Optional facts, known as extensions

The issuer signs this information with their private key and then bundles it all together to form a certificate.

> **Note**: For a detailed description of the X.509 certificate format, see [`RFC 5280`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5280).

For example, if you download a code-signing certificate from the Developer website, you can dump the resulting `.cer` file like so:

```shell
 1 % openssl x509 -in "developerID_application.cer" -inform der -text
 2 Certificate:
 3     Data:
 4         Version: 3 (0x2)
 5         Serial Number: 242040529399961421 (0x35be6944021d74d)
 6     Signature Algorithm: sha256WithRSAEncryption
 7         Issuer: CN=Developer ID Certification Authority, OU=Apple Certi…
 8         Validity
 9             Not Before: Jul 31 16:31:20 2017 GMT
10             Not After : Aug  1 16:31:20 2022 GMT
11         Subject: … CN=Developer ID Application: …, OU=SKMME9E2Y8, …
12         Subject Public Key Info:
13             …
14         X509v3 extensions:
15             …
16     Signature Algorithm: sha256WithRSAEncryption
17          cc:73:eb:43:51:a9:d4:d1:dc:5b:5a:fe:9a:d9:fe:eb:ea:c4:
18          …
```

Breaking this down:

- Line 7 shows the details of the issuer, in this case the Developer ID Certification Authority.
- Line 11 shows the details of the subject.  This example shows a Developer ID certificate, used for Mac code that’s distributed directly.  For code signing certificates, Apple places the developer’s Team ID into the subject’s Organization Unit (`OU`) field.
- Lines 12 through 13 are the subject’s public key.
- Lines 3 through 5 and 8 through 10 are the required facts, namely the certificate format version, serial number, and valid date range.
- Lines 14 through 15 are the optional facts.  Code-signing certificates contain numerous extensions.  Some are industry standard extensions, while others are Apple-specific.   The latter are documented on the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) page.
- Lines 16 through 18 are the issuer’s signature.

To condense this into plain English, this certificate says that “Apple certifies that this developer is associated with this public key, and the matching private key can be used to sign Mac code.”  This is clearly a simplification—it doesn’t touch on the valid date range, serial number, or even how Apple identified the developer in the first place—but it’s a reasonable model to start out with.

Apple issues a variety of different code-signing certificate types.  For a complete list, see [`Certificate types`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/certificate-types).

Certificates are usually stored in one of two formats:

To convert between these formats, run the `openssl` command-line tool with the `x509` subcommand:

```shell
% openssl x509 -in "developerID_application.cer" -inform der -out "developerID_application.pem"        
% openssl x509 -in "developerID_application.pem" -out "developerID_application.cer" -outform der
```

##### Chain of Trust

Certificates often form a chain of trust: the verifier uses the issuer information in a certificate to find the issuer’s certificate, then uses its issuer information to find the next certificate in the chain, and so on, until it hits an anchor, that is, a certificate it trusts as a matter of policy.  This process can be  complex, but for Apple’s code signing certificates it’s usually quite simple.  To view the certificate chain for an app, run the following command:

```shell
% codesign --display -vvv "MyApp.app"
…
Authority=Developer ID Application: …
Authority=Developer ID Certification Authority
Authority=Apple Root CA
…
```

> **Note**: For a detailed description of the standard algorithm to build a chain of trust, see [`RFC 5280`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5280).

In this example the Developer ID Application leaf certificate was issued by the Developer ID Certification Authority intermediate certificate which was issued by the Apple Root CA root certificate.  This three-level chain of trust is standard for Apple code signing, where:

- The leaf certificate is issued to a developer by the Apple Developer website.
- The intermediate certificate is one of a very limited set used for code signing, including Apple Worldwide Developer Relations Certification Authority and Developer ID Certification Authority.  Apple publishes these intermediate certificates on the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) page.
- The root certificate is Apple Root CA.  Apple operating systems trust this implicitly.

> ❗ **Important**: Don’t rely on the exact details of this chain of trust; it could change in the future.

The `Authority` fields in the example above show a short summary of each certificate in the chain. To get the actual certificates, run `codesign` with the `--extract-certificates` option:

```shell
% codesign --display --extract-certificates "MyApp.app"
```

This creates a certificate file for each certificate in the chain, using `codesign0` for the leaf, `codesign1` for its issuer, and so on.  So, to dump the leaf certificate, run this command:

```shell
% openssl x509 -in codesign0 -inform der -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 242040529399961421 (0x35be6944021d74d)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=Developer ID Certification Authority, OU=Apple Certi…
        Validity
            Not Before: Jul 31 16:31:20 2017 GMT
            Not After : Aug  1 16:31:20 2022 GMT
        Subject: … CN=Developer ID Application: …
        …
```

##### Digital Identity

The previous section’s discussion of certificates was focused entirely on public keys.  Certificates are public data structures used to evaluate trust on the public key that’s, in turn, used to verify the signature.

To sign code you need a certificate and the private key that matches the public key in that certificate.  This combination is called a digital identity or, if it’s for signing code, a code-signing identity.

> ❗ **Important**: As a certificate only contains a public key, you can’t use it to sign code.

Many people use the term  when they mean .  This industry-wide confusion extends into the Apple ecosystem.  For example, Xcode uses the term , Keychain Access uses , and Apple Mail uses .

Apple tools and APIs that work with a digital identity generally prefer the  PKCS#12 format.  PKCS#12 files usually have the `.p12` extension, although `.pfx` is a common alternative.

> **Note**: To learn more about PKCS#12, read [`RFC 7292`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7292).

Non-Apple tools and libraries, most notably OpenSSL, work with digital identities in the PEM format.  In this case the PEM file contains two separate items: one for the certificate and one for the private key.  Such files can have a variety of extensions but one common one is `.cer`, further increasing the confusion between certificates and digital identities.

To convert between the PKCS#12 and PEM formats, run the `openssl` command-line tool with the `pkcs12` subcommand.

##### Certificate Signing Request

Apple issues code-signing certificates in three different ways:

- Manual certificate signing request (CSR) process
- Xcode’s certificate management
- Cloud-managed certificates

It’s important to understand how these issuing processes relate to the private key that, when combined with the certificate, forms your code-signing identity.

[`Developer Account Help`](https://developer.apple.comhttps://developer.apple.com/help/account/) describes the manual CSR process.  A key step in that process is using Keychain Access to create a CSR.  This does two things:

1. It creates a public / private key pair in your login keychain.
2. It takes the public key, wraps it in a CSR structure, and prompts you to save that to a `.certSigningRequest` file.

You then submit your CSR to the Developer website, which issues a certificate that contains your public key.  When you download this certificate and import it into your keychain, it forms a code-signing identity with the private key created in step 1.

> **Note**: To learn more about CSRs in general, read [`RFC 2986`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2986).

This process has some key advantages:

- Your private key never leaves your Mac.  As long as you keep that key to yourself, no one can sign code as you.
- You can choose to use a private key that’s stored on a smart card or some other type of hardware token.

However, it does have one notable drawback: It’s easy to miss that your most critical code-signing asset, your private key, is tucked away in your login keychain.  And if you do miss that, you might lose your private key, for example, when you migrate to a new Mac.  If that happens, follow the advice in [`Developer > Support > Certificates`](https://developer.apple.comhttps://developer.apple.com/support/certificates/).

Xcode’s certificate management follows the same overall path as the manual CSR process.  For example, when you create a new code-signing identity using the process described in [`Synchronizing code signing identities with your developer account`](https://developer.apple.com/documentation/Xcode/sharing-your-teams-signing-certificates), Xcode effectively creates a CSR, submits it to the Developer website, downloads the resulting certificate, and adds that to your keychain.  It’s easy to use, but it has the same trap: Xcode automatically generates a private key and stores it in your login keychain.

When you use a [`cloud-managed certificate`](https://developer.apple.comhttps://developer.apple.com/help/account/create-certificates/cloud-managed-certificates)—for example, when building with Xcode Cloud—both the private key and the certificate are managed by Apple’s cloud signing infrastructure.  You don’t have direct access to either of them.

##### Cryptographic Message Syntax

Internally, code signing uses Cryptographic Message Syntax (CMS).  This is very much an implementation detail, but it can be fun to explore.  To extract the CMS structure for a code signature, run `codesign` with the `--dump-cms` option:

```shell
% codesign --display --dump-cms=cms.asn1 "MyApp.app"
…
% openssl asn1parse -in cms.asn1 -inform der -i
    0:d=0  hl=2 l=inf  cons: SEQUENCE          
    2:d=1  hl=2 l=   9 prim:  OBJECT            :pkcs7-signedData
    …
```

> **Note**: To learn more about CMS, read [`RFC 5652`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5652).

#### Code Signings Pki Operations

Code signing has three core operations:

- Sign code
- Display a code signature
- Verify a code signature

The following sections explain how each of these operations interact with Apple’s code signing infrastructure.

##### Sign Code

When you sign code, you pass `codesign` the name of a code-signing identity using the `--sign` subcommand.  For example:

```shell
% codesign --sign "Apple Development" "MyApp.app"
```

> **Note**: This example uses the `codesign` command-line tool, but these concepts also apply to Xcode.  To see how Xcode invokes `codesign`, go to the Reports navigator, find your Build report, and look at the CodeSign step in the build transcript.

By default `codesign` searches all keychains for a code-signing identity whose certificate matches the supplied name.  If multiple identities match, `codesign` complains about the ambiguity.  To resolve this, either pass in the full name or pass in the SHA-1 hash of the identity’s certificate.

The `codesign` man page explains this search process in detail.  For general information about man pages, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

When searching for code-signing identities, `codesign` checks certain aspects of each identity’s certificate:

- It checks that it can build a chain of trust from the certificate to a trusted root.
- It checks that the current time is within the certificate’s valid range.
- It checks that the certificate supports code signing.  Specifically, it looks for Code Signing within the certificate’s Extended Key Usage extension:

```shell
% openssl x509 -in "developerID_application.cer" -inform der -text
        …
        X509v3 extensions:
            …
            X509v3 Extended Key Usage: critical
                Code Signing
            …
```

To see all available code-signing identities, run this command:

```shell
% security find-identity -p codesigning

Policy: Code Signing
  Matching identities
  1) 8CEF1273B13E1C6E7F6E73EBBEF42278F0D88C97 "Apple Development: …"
  2) ADC03B244F4C1018384DCAFFC920F26136F6B59B "Developer ID Application: …" (CSSMERR_TP_CERT_EXPIRED)
  3) 3F8BE319780F84EB2E94ABDFA24E8045A0572A7B "Developer ID Application: …"
     3 identities found

  Valid identities only
  1) 8CEF1273B13E1C6E7F6E73EBBEF42278F0D88C97 "Apple Development: …"
  2) 3F8BE319780F84EB2E94ABDFA24E8045A0572A7B "Developer ID Application: …"
     2 valid identities found
```

Note how there are three code-signing identities but one of them has expired leaving only two valid ones.

The hex string next to each identity is the SHA-1 hash of its certificate, which is a good way to resolve any ambiguities with the name.

Unless you specify a keychain file using the `--keychain` option, `codesign` searches all keychains including the data protection keychain.  If you do supply a keychain file, `codesign` searches just that keychain.

> **Note**: If you’re unfamiliar with the data protection keychain, see [`TN3137: On Mac keychain APIs and implementations`](tn3137-on-mac-keychains.md).

The `codesign` tool is able to find and use code-signing identities in the data protection keychain, including ones stored in a smart card or some other type of hardware token.  However:

- The `security find-identity` command only searches keychain files; it won’t show identities in the data protection keychain.
- If you want to use a code-signing identity stored in the data protection keychain, don’t specify a keychain file using the `--keychain` option, because that tells `codesign` to search just that file.
- If you sign your code with Xcode, use Xcode 13 or later.  Earlier versions of Xcode only work with file-based code-signing identities.

> **Note**: macOS has built-in support for PIV smart cards.  Third-party developers can add support for other types of hardware tokens by creating a [`CryptoTokenKit`](https://developer.apple.com/documentation/CryptoTokenKit) app extension.

Once `codesign` has determined the code-signing identity to use, it builds a chain of trust between the identity’s certificate and a trusted anchor.  If it’s unable to build that chain, it fails with an error `unable to build chain to self-signed root`.  The most common cause of that failure is a missing intermediate certificate.  The intermediate certificates used by `codesign` are automatically installed by Xcode.  If you’re not using Xcode, download these intermediate certificates from the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) page and install them yourself.

The `codesign` tool adds the full chain of trust to the CMS structure within the code signature.  When you run code on a device, the system uses the intermediate certificates in this CMS structure to build its chain of trust.  That means that user devices don’t have to have the code signing intermediate certificates installed.

##### Display a Code Signature

To display the chain of trust for a code signature, run the `codesign` command with the `--display` subcommand and two `-v` options:

```shell
% codesign --display -vv "MyApp.app"
…
Authority=Apple Development: …
Authority=Apple Worldwide Developer Relations Certification Authority
Authority=Apple Root CA
…
```

Each `Authority` field represents a link in the chain of trust.  This is just a short summary.  To see the full certificates, use the `--extract-certificates` option:

```shell
% codesign --display --extract-certificates "MyApp.app"
…
% openssl x509 -in codesign0 -inform der -text
Certificate:
    …
    Signature Algorithm: sha256WithRSAEncryption
        …
        Subject: … CN=Apple Development: …
        …
```

One oddity of this feature is that `codesign` doesn’t simply print the list of certificates stored in the CMS structure within the code signature.  Rather, it builds the chain of trust from scratch by performing a standard trust evaluation on the CMS leaf certificate.  It does this using a [`Trust`](https://developer.apple.com/documentation/Security/trust).  In most cases that produces a chain of trust that matches the one in the CMS structure, but that’s not  to be the case.  If `codesign` displays a chain of trust that seems odd (for example, it might show just a single `Authority` field) extract the CMS structure and look at its certificates.

For instructions on how to extract the CMS structure, see [`Cryptographic Message Syntax`](tn3161-inside-code-signing-certificates#Cryptographic-Message-Syntax.md).

##### Verify a Code Signature

To verify a code signature, run the `codesign` command with the `--verify` subcommand:

```shell
% codesign --verify "MyApp.app" ; echo $?
0
```

That command succeeds silently, only setting the status, so add a few `-v` options to increase the verbosity:

```shell
% codesign --verify -vvv "MyApp.app"
MyApp.app: valid on disk
MyApp.app: satisfies its Designated Requirement
```

For a more in-depth check, add the `--strict` and `--deep` options:

```shell
% codesign --verify -vvv --deep --strict "/Applications/Xcode.app" 
--prepared:/Applications/Xcode.app/Contents/SharedFrameworks/XCUnit.framew…
--prepared:/Applications/Xcode.app/Contents/SharedFrameworks/GLToolsInterf…
…
/Applications/Xcode.app: valid on disk
/Applications/Xcode.app: satisfies its Designated Requirement
```

Be careful how you interpret this output.  It isn’t saying that the code is fit for some specific purpose, like running on your Mac or installing on your iPhone.  Rather, it says that the code is internally consistent, that is:

- All of the expected files are present.
- There are no extra files.
- None of the files have been modified.  To learn how code signing checks for changes, read [`TN3126: Inside Code Signing: Hashes`](tn3126-inside-code-signing-hashes.md).
- A basic X.509 trust evaluation of the leaf certificate succeeded.
- The code satisfies its own designated requirement (DR).  To learn more about code signing requirements in general, and the significance of the DR in particular, see [`TN3127: Inside Code Signing: Requirements`](tn3127-inside-code-signing-requirements.md).

To check whether the code is fit for a specific purpose, you need some other mechanism:

- For an app you’re submitting to the App Store, use `altool` with the `--validate-app` subcommand.  For more on this, see the `altool` [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).  This uses the same infrastructure as the Validate App button in the Xcode organizer.
- For Mac apps that you directly distribute using Developer ID code signing, use the `syspolicy_check` tool.  To learn more about this tool, see its [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

#### Non Apple Certificates

Apple’s code signing support was created before Apple started issuing code signing certificates to third-party developers.  That results in some behavior that seems odd today:

- When signing code, `codesign` doesn’t check that the code-signing identity’s certificate was issued by Apple.
- When verifying code, `codesign` doesn’t check if the code will be accepted by the target platform.

Historically it might have made sense to sign code with a code-signing identity whose certificate wasn’t issued by Apple.  That’s no longer the case.  Most Apple platforms only run code with an Apple-issued certificate.  The only exception to this is macOS, which can run code with other certificates, or indeed with no certificate.  However, that’s not useful in practice because Gatekeeper blocks code with a non-Apple certificate.

For general information about Gatekeeper, see [`Safely open apps on your Mac`](https://developer.apple.comhttps://support.apple.com/en-us/HT202491).

#### App Store Re Signing

When you distribute an app on the App Store, the App Store re-signs your app as part of the distribution process.  It’s easy to confirm this on macOS.  Imagine you have an app called MyAppStoreApp that’s available on the Mac App Store.  Install the app and then run this command to display its code signature:

```shell
% codesign --display -vv "/Applications/MyAppStoreApp.app"
…
Authority=Apple Mac OS Application Signing
Authority=Apple Worldwide Developer Relations Certification Authority
Authority=Apple Root CA
…
```

The leaf certificate is `Apple Mac OS Application Signing`.  This doesn’t match the certificate from the code-signing identity you used to sign your app prior to submission, which is named either `Apple Distribution: <Team>` or `3rd Party Mac Developer Application: TTT <Team>`, where `<Team>` identifies your team.

> ❗ **Important**: While this example was from macOS, this re-signing happens for all App Store apps on all platforms.

In most cases you don’t notice that your app has been re-signed, but there are a few places where it matters:

- App Store apps are signed with credentials that don’t expire.  In contrast, your distribution certificate and provisioning profiles can expire.  However, this re-signing means that your credentials only need to be valid at the time that you submit your app.
- The App Store must be able to re-sign all of your code.  If it can’t see a particular code item, it can’t re-sign that code and the code won’t run.  A common example of this problem is code embedded in an archive, like a `.zip` or a `.jar` file.  For best results, follow the rules in [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle).
- Apps that try to do their own tamper detection have to take this re-signing into account.  It’s common for such code to fail when Apple reworks the App Store distribution process.  To avoid such problems, use the App Attest feature of the [`DeviceCheck`](https://developer.apple.com/documentation/DeviceCheck) framework to establish your app’s integrity.
- You sign your app for distribution as part of the App Store submission process.  That’s the intended use for an App Store distribution-signed app.  You can’t run such an app yourself.

With regards that last point, the one exception is macOS.  In some situations macOS is able to run an App Store distribution-signed app.  However, this isn’t supported, and it currently fails if the app claims a restricted entitlement.  For more about restricted entitlements, see [`TN3125: Inside Code Signing: Provisioning Profiles`](tn3125-inside-code-signing-provisioning-profiles.md).

Because you can’t reliably run your App Store distribution-signed app, you need some other way to test it before release.  A great option for this is [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/).  TestFlight has many fine features, but a key benefit in this context is that it re-signs your app, much like the App Store.

#### Certificate Expiration

All X.509 certificates have a valid date range.  For Apple code-signing certificates that’s typically a year from the date of issue, although the exact duration varies based on the certificate type.

For App Store apps certificate expiration isn’t complicated.  When you submit an app to the App Store, it checks that the app’s distribution certificate is currently valid.  The App Store then re-signs your app, making it independent of your distribution certificate’s expiry date.

This mechanism only works for App Store apps, which raises the question of what happens when you use Developer ID signing to directly distribute Mac software.  People who install your product expect it to continue working, regardless of your certificate’s expiration date.  Apple enables this by embedding a secure timestamp within your code signature.  This records when your code was signed.  When you run the code, macOS checks that its Developer ID certificate was valid at the time that it was signed.

Xcode automatically adds a secure timestamp when it signs code with a Developer ID code-signing identity.  If you sign code using `codesign`, pass in the `--timestamp` option to add a secure timestamp.  The Apple notary service ensures that all code has a secure timestamp, so if you get this wrong you’ll learn about it when you go to notarize your code.  For more about notarization, see [`Notarizing macOS software before distribution`](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution).

To check whether your code has a secure timestamp, look at the output from the `--display` subcommand.  For example:

```shell
% codesign --display -v "MyApp.app"
…
Timestamp=27 Jan 2024 at 10:52:13
…
```

The `Timestamp` field represents the secure timestamp.

Don’t confused the `Timestamp` and `Signed Time` fields.  The latter is not secured by the Apple timestamp service.  Rather, `codesign` sets this field based on your Mac’s current time.  You typically see this field in development-signed code.  For example:

```shell
% codesign --sign "Apple Development" -f "MyApp.app" 
…
% codesign --display -v "MyTool.app"
…
Signed Time=27 Jan 2024 at 10:53:29
…
```

The secure timestamp requirement has one important consequence: You must have access to the internet to sign code with a Developer ID code-signing identity.  Specifically, `codesign` currently talks to the Apple timestamp service at `timestamp.apple.com` using a protocol based on the X.509 Time-Stamp Protocol, as described in [`RFC 3161`](https://developer.apple.comhttps://tools.ietf.org/html/rfc3161).  If you’re unable to sign code when running on a particular network, check that its firewall allows these connections.

> ❗ **Important**: The Apple timestamp service is reserved for use by code signing.  Its name and behaviour are considered implementation details.  Don’t ship a product that depends on those details.

Certificates aren’t the only code-signing asset that expire.  Provisioning profiles also have an expiration date.  To learn more about that, see [`TN3125: Inside Code Signing: Provisioning Profiles`](tn3125-inside-code-signing-provisioning-profiles.md).

#### Revision History

-  Made a minor editorial change.
-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3161-inside-code-signing-certificates)*