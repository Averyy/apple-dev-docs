# TN3127: Inside Code Signing: Requirements

**Framework**: Technotes

Explore how macOS uses code signing requirements to reason about code identity.

#### Overview

Code signing requirements are an obscure and dusty corner of the code signing castle.  Most developers don’t need to worry about them.  They sign their code using Xcode, or the `codesign` tool, and those automatically do the right thing when it comes to requirements.

However, in some cases requirements are important, especially on macOS.  For example:

- If you’re building an XPC service, you might want to restrict it to specific clients.  The best way to do this is by setting a code signing requirement on the connection with [`setCodeSigningRequirement(_:)`](https://developer.apple.com/documentation/foundation/nsxpcconnection/3943309-setcodesigningrequirement).  But what requirement to use?
- When working with privacy-protected resources on macOS, like the microphone, you might find that the system fails to remember your choices during development.
- You might find that the keychain presents unexpected authorization alerts when you deploy your app through a new channel, like TestFlight.

> **Note**: macOS 14 added a new way to express limits on code.  For the details, see [`Applying launch environment and library constraints`](https://developer.apple.com/documentation/Security/applying-launch-environment-and-library-constraints).

macOS 14 added a new way to express limits on code.  For the details, see [`Applying launch environment and library constraints`](https://developer.apple.com/documentation/Security/applying-launch-environment-and-library-constraints).

##### About This Technote Series

Code signing is a foundational technology on all Apple platforms.  Many documents that discuss code signing focus on solving a specific problem.  The  technotes peek behind the code signing curtain, to give you a better understanding of how it works.  For a list of all the technotes in this series, see the introduction in [`TN3125: Inside Code Signing: Provisioning Profiles`](tn3125-inside-code-signing-provisioning-profiles.md).

> ❗ **Important**: The  technotes discuss code signing details that aren’t considered API.  The structure of a code signature has changed numerous times in the past and may well change again in the future.  Don’t encode this information in your product.  When signing code, use Xcode (all platforms) or the `codesign` tool (macOS only).  To get information or validate a code signature, use the `codesign` tool or the [`Code Signing Services`](https://developer.apple.com/documentation/Security/code-signing-services) API.  Apple updates these facilities to accommodate any changes to the code signature structure as they roll out.

The  technotes discuss code signing details that aren’t considered API.  The structure of a code signature has changed numerous times in the past and may well change again in the future.  Don’t encode this information in your product.  When signing code, use Xcode (all platforms) or the `codesign` tool (macOS only).  To get information or validate a code signature, use the `codesign` tool or the [`Code Signing Services`](https://developer.apple.com/documentation/Security/code-signing-services) API.  Apple updates these facilities to accommodate any changes to the code signature structure as they roll out.

#### Basics

A code signing requirement is a function that, given a code signature, returns a Boolean value.  This function uses traditional expression syntax.  For example `anchor apple and identifier = "com.apple.TextEdit"` is a requirement that returns true if:

- The code was signed by Apple as Apple code.
- The code’s signing identifier is `com.apple.TextEdit`.

In short, this requirement identifies the TextEdit app.

> ❗ **Important**: A  is a string chosen by the signer to uniquely identify their code. For bundled code this is typically the bundle identifier.  Don’t confuse this with a , which is a digital identity used for code signing.  This digital identity includes a  and its associated private key.  Finally,  is an abstract user-level concept of the ‘same code’.  For example, a user might consider the TextEdit app in macOS 12 to be the same as the TextEdit app in macOS 11 but not the same as the Calculator app.  macOS uses code signing requirements to establish code identity.

A  is a string chosen by the signer to uniquely identify their code. For bundled code this is typically the bundle identifier.  Don’t confuse this with a , which is a digital identity used for code signing.  This digital identity includes a  and its associated private key.  Finally,  is an abstract user-level concept of the ‘same code’.  For example, a user might consider the TextEdit app in macOS 12 to be the same as the TextEdit app in macOS 11 but not the same as the Calculator app.  macOS uses code signing requirements to establish code identity.

Use `codesign` to evaluate a requirement:

```shell
% codesign --verify -v -R '=anchor apple and identifier = "com.apple.TextEdit"' "/System/Applications/TextEdit.app"
…
/System/Applications/TextEdit.app: explicit requirement satisfied

% codesign --verify -v -R '=anchor apple and identifier = "com.apple.TextEdit"' "/System/Applications/Calculator.app"
…
test-requirement: code failed to satisfy specified code requirement(s)
```

So TextEdit satisfies this requirement but Calculator does not.  You can also check requirements programmatically.  The following example calls [`SecStaticCodeCheckValidityWithErrors(_:_:_:_:)`](https://developer.apple.com/documentation/Security/SecStaticCodeCheckValidityWithErrors(_:_:_:_:)) to check whether the given file satisfies the `anchor apple and identifier = "com.apple.TextEdit"` requirement:

```swift
func isTextEdit(_ url: URL) throws -> Bool {
    let req = try secCall { SecRequirementCreateWithString(#"anchor apple and identifier = "com.apple.TextEdit""# as NSString, [], $0) }
    let code = try secCall { SecStaticCodeCreateWithPath(url as NSURL, [], $0) }
    var errorQ: Unmanaged<CFError>? = nil
    let err = SecStaticCodeCheckValidityWithErrors(code, [], req, &errorQ)
    if err == errSecSuccess {
        return true
    } else {
        let error = errorQ!.takeRetainedValue() as Error
        guard err == errSecCSReqFailed else {
            throw error
        }
        return false
    }
}
```

> **Note**: This code uses the `secCall(_:)` helper from [`Signing a daemon with a restricted entitlement`](https://developer.apple.com/documentation/Xcode/signing-a-daemon-with-a-restricted-entitlement).

This code uses the `secCall(_:)` helper from [`Signing a daemon with a restricted entitlement`](https://developer.apple.com/documentation/Xcode/signing-a-daemon-with-a-restricted-entitlement).

Compiling requirements is relatively expensive so, if you do this a lot, cache the requirement object you get back from `SecRequirementCreateWithString`.  Alternatively, use the `csreq` command-line tool to compile the requirement in advance, embed that data within your program, and then create a requirement by passing that data to `SecRequirementCreateWithData`.

The code signing requirement language is very flexible.  It can express a very specific requirement or a very general one.  For example, the requirement `cdhash H"ff19a91b272a49d1a0f16ee54c672da60f0e116f"` is satisfied only by code with a specific cdhash value.  On the other hand, the requirement `anchor apple generic` is satisfied by any code signed with any code signing identity issued by Apple.  When you craft a custom requirement, think carefully about how specific you want it to be.

For a detailed explanation of the code signing requirement language, see [`Code Signing Requirement Language`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/RequirementLang/RequirementLang.html#//apple_ref/doc/uid/TP40005929-CH5-SW1).  For more on cdhash values, see [`TN3126: Inside Code Signing: Hashes`](tn3126-inside-code-signing-hashes.md).  For more information about the tools used in these examples, read their man pages.  If you’re unfamiliar with that process, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).  Specifically, the `codesign` man page is the key reference if you’re working at this level.

#### Designated Requirement

Most code has a  (DR) which is how the code identifies itself: It’s the code’s way of saying “If you see me again, here’s how you tell it’s really me.”  The DR is critical on macOS, an open platform where code impersonation is a cause for concern.

> **Note**: Other Apple platforms allow for a DR, but it doesn’t represent the primary means of tracking code identity.

Other Apple platforms allow for a DR, but it doesn’t represent the primary means of tracking code identity.

Imagine you have an app that accesses the microphone.  At that point macOS prompts the user to authorize that.  A few days later your app’s software update mechanism runs and replaces version 1.2 with version 1.3.  Then the user runs the new version of your app and it again accesses the microphone.  How can macOS tell that version 1.3 of your app is the ‘same code’ as version 1.2?

macOS solves this problem by recording your app’s DR in its database of apps authorized to access the microphone.  Each time your app tries to access the microphone, macOS checks that this version of the app satisfies the original DR.  In short, the DR is all about code identity.

Unsigned code has no DR.  Ad hoc signed code, called Sign to Run Locally by Xcode, has a DR but it’s tied to that specific version of the code.  In both cases macOS can’t reliably track the identity of the code.  You often see this problem when you create a simple test project in Xcode and don’t bother to enable code signing.  If the app accesses the microphone, macOS prompts you to authorize that access.  If you tweak the code and run it again, macOS repeats that prompt.  Without a DR, macOS can’t track this authorization across versions of your app.

The DR is part of the code signature.  To view it, run `codesign`:

```shell
% codesign --display -r - "/System/Applications/TextEdit.app"
…
designated => identifier "com.apple.TextEdit" and anchor apple
```

TextEdit’s DR shows a pattern common to virtually all DRs:

- Most of the DR checks who signed the code.
- The `identifier` term identifies the code within the scope of that signer.

The `identifier` term checks the , a string chosen by the signer to uniquely identify their code.  For bundled code this is typically the bundle identifier but that’s not required; the signer can set the code signing identifier to whatever value they want.

When you create a new app, Xcode or the `codesign` tool sets the DR to a default value based on your code signing identity.  For example:

```shell
% codesign --display -r - "AppWithTool.app"
…
designated => anchor apple generic and identifier "com.example.apple-samplecode.AppWithTool" and …details omitted… SKMME9E2Y8
% codesign --display -r - "AppWithTool.app/Contents/MacOS/ToolX"      
…
designated => anchor apple generic and identifier "com.example.apple-samplecode.AppWithTool.ToolX" and …details omitted… SKMME9E2Y8
```

> **Note**: To build the AppWithTool app used in this example, follow the instructions in [`Embedding a command-line tool in a sandboxed app`](https://developer.apple.com/documentation/Xcode/embedding-a-helper-tool-in-a-sandboxed-app).

To build the AppWithTool app used in this example, follow the instructions in [`Embedding a command-line tool in a sandboxed app`](https://developer.apple.com/documentation/Xcode/embedding-a-helper-tool-in-a-sandboxed-app).

The DRs in this example are heavily abbreviated lest you get lost in the details.  The critical things to note here are:

- The `anchor apple generic` term, which requires that the code be signed by a code signing identity issued by Apple. Contrast this to the `anchor apple` term used in TextEdit’s DR.  The latter requires that the code be signed by Apple as Apple code, whereas the former only requires that the code signing identity was issued by Apple.
- The check for Team ID `SKMME9E2Y8`, most of which has been omitted in this example.
- The `identifier` term, which requires that the app has a code signing identifier of `com.example.apple-samplecode.AppWithTool` and the tool has a code signing identifier of `com.example.apple-samplecode.AppWithTool.ToolX`. Note that the code signing identifier is different for the app and its embedded command-line tool.  This is best practice, as it allows the system to identify the app and the tool as separate items of code.

The example above omits a large fraction of the DRs, with those omitted parts checking who signed the code.  The mechanics of this vary based on the code signing identity.  For a full explanation of these omitted terms, see [`Default and Xcode designated requirements`](tn3127-inside-code-signing-requirements#Default-and-Xcode-designated-requirements.md).

The DR is part of the code signature, making it an .  A signature can have other internal requirements but that feature isn’t used in practice.

#### Mutually Compatible Designated Requirements

Two apps, A and B, have  if app A satisifies app B’s DR and app B satisfies app A’s DR.

This property is important when you ship two different variants of the same app, one that you distribute on the Mac App Store and another that you distribute directly using Developer ID signing.  If these apps have mutually compatible DRs then they share access to privacy-protected resources.  For example, if the user grants the Mac App Store app access to the microphone, the Developer ID app gains access as well.

To check if two apps have mutually compatible DRs, first dump the DR of app A:

```shell
% codesign --display -r "MAS.req.txt" "MyApp-MAS.app"
…
% sed -e 's/designated => //' -i .bu "MAS.req.txt"                 
```

> **Note**: Note The `codesign` command writes the DR with its type prefix, `designated =>`.  The `sed` command removes that because its presence causes problems for the next step.

Note The `codesign` command writes the DR with its type prefix, `designated =>`.  The `sed` command removes that because its presence causes problems for the next step.

Next, check that app B satisfies app A’s DR:

```shell
% codesign --verify -vv -R "MAS.req.txt" "MyApp-DevID.app"
…
…/MyApp-DevID.app: explicit requirement satisfied
```

Finally, repeat this process in reverse:

```shell
% codesign --display -r "DevID.req.txt" "MyApp-DevID.app"
…
% sed -e 's/designated => //' -i .bu "DevID.req.txt"                                     
% codesign --verify -vv -R "DevID.req.txt" "MyApp-MAS.app"                
…
…/MyApp-MAS.app: explicit requirement satisfied
```

There’s no requirement for different variants of your app to have mutually compatible DRs.  You might, for example, want each variant to have its own independent access to privacy-protected resources.  However, it’s very common for Mac App Store and Developer ID apps to have mutually compatible DRs.

#### Default and Xcode Designated Requirements

When you sign code with `codesign`, it applies a  based on the code signing identity you supply.  For example, if you sign a development build with your Apple Development code signing identity it gets a different DR than a distribution build signed with your Developer ID code signing identity.

These default DRs strike a balance between generality and specificity.  They ensure that:

- A privilege, like microphone access, acquired by an existing version of your app is still available to a new version.
- Other teams can’t sign an app that impersonates your app, that is, an app that satisfies your app’s DR.

These default DRs have one important limitation: Mac App Store and Developer ID variants of your app aren’t mutually compatible.

Xcode avoids this limitation by signing code with custom DRs that support mutual compatibility.  If you want mutual compatibility but don’t use Xcode to sign your code, supply a custom DR just like Xcode does.  For information on how to sign with a custom DR, see [`Creating distribution-signed code for macOS`](https://developer.apple.com/documentation/Xcode/creating-distribution-signed-code-for-the-mac).

As code signing requirements have a textual representation, you might be tempted to write your custom DR by hand.  Don’t do that.  Code signing requirements are tricky to get right.  Rather, use Xcode to sign some code for the intended distribution channel, dump the DR of that signed code to a file, and then edit the file to change the code signing identifier and Team ID embedded in the DR.  For example, if `TestApp-MAS.app` is an app signed by Xcode for Mac App Store distribution, use this command to dump its DR:

```shell
% codesign --display -r "TestApp-MAS.req.txt" "TestApp-MAS.app"
% cat "TestApp-MAS.req.txt" 
designated => (anchor apple generic …details ommitted… "SKMME9E2Y8") and identifier "com.example.apple-samplecode.TestApp"
```

The following sections explain the Xcode DRs for the three common types of macOS code signing identity.

##### Xcode Designated Requirement for Developer Id Code

If you use Xcode to sign the AppWithTool app with a Developer ID code signing identity, the DR looks like this:

```shell
% codesign --display -r - "AppWithTool.app"         
…
designated => 
anchor apple generic 
and identifier "com.example.apple-samplecode.AppWithTool" 
and (
    certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ 
    or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ 
        and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ 
        and certificate leaf[subject.OU] = SKMME9E2Y8
    )
```

While this is reformatted to make it easier to read, it’s still quite hard to read.  To help with that, let’s replace some terms with shorter identifiers.  The `certificate leaf[field.1.2.840.113635.100.6.1.9]` term requires that the leaf certificate, the certificate that’s part of the code signing identity that actually signed the code, includes an extension with the OID 1.2.840.113635.100.6.1.9.  This OID is present in the Apple Mac OS Application Signing certificate used by Apple to sign Mac App Store apps.  Let’s shorten this to `LeafIsMacAppStore`.

> ❗ **Important**: The OID checks shown here only make sense in the scope established by `anchor apple generic`, that is, for certificates issued by Apple.  There’s nothing to stop a malicious CA from issuing certificates with these OIDs.

The OID checks shown here only make sense in the scope established by `anchor apple generic`, that is, for certificates issued by Apple.  There’s nothing to stop a malicious CA from issuing certificates with these OIDs.

The `certificate 1[field.1.2.840.113635.100.6.2.6]` term requires that the certificate that issued the leaf certificate include an extension with the OID 1.2.840.113635.100.6.2.6.  This OID is present in the Developer ID Certification Authority certificate used by Apple to issue Developer ID signing certificates.  Let’s shorten this to `IssuerIsDeveloperID`.

The `certificate leaf[field.1.2.840.113635.100.6.1.13]` term requires that the certificate that issued the signing certificate include an extension with the OID 1.2.840.113635.100.6.1.13.  This OID is present in the Developer ID Application signing certificates issued by Apple.  Let’s shorten this to `LeafIsDeveloperIDApp`.

> **Note**: Developer ID Installer certificates have a different OID, 1.2.840.113635.100.6.1.14.  That’s why you can’t use those for signing apps, or vice versa.

Developer ID Installer certificates have a different OID, 1.2.840.113635.100.6.1.14.  That’s why you can’t use those for signing apps, or vice versa.

The `certificate leaf[subject.OU] = SKMME9E2Y8` term requires that the leaf certificate’s Organization Unit field be SKMME9E2Y8.  In a Developer ID certificate, this is where you’ll find the Team ID.

Applying the shortcuts above reveals this:

```shell
anchor apple generic 
and identifier "com.example.apple-samplecode.AppWithTool" 
and (
    LeafIsMacAppStore 
    or IssuerIsDeveloperID 
        and LeafIsDeveloperIDApp 
        and certificate leaf[subject.OU] = SKMME9E2Y8
    )
```

Or, in English, the requirement states that the code must be signed:

- With a code signing identity whose certificate was issued by Apple
- And with a code signing identifier of `com.example.apple-samplecode.AppWithTool`
- Either by the Mac App Store
- Or using a Developer ID Application code signing identity for Team ID SKMME9E2Y8

For more information about the Apple-specific OIDs referenced in this technote, see the documents published on the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) page.

##### Xcode Designated Requirement for Mac App Store Code

AppWithTool isn’t on the Mac App Store, so you can’t look at its Xcode DR.  You can, however, look at the DR for Numbers, which is typical of a Mac App Store app:

```shell
% codesign --display -r - "/Applications/Numbers.app"
…
designated =>
(
    anchor apple generic 
    and certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ 
        or anchor apple generic
            and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ 
            and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ 
            and certificate leaf[subject.OU] = K36BKF7T3D
)
and identifier "com.apple.iWork.Numbers"
```

This looks very different from the Developer ID DR but, surprisingly, it’s actually the same.  To see this, apply the shortcuts defined earlier:

```shell
(
    anchor apple generic 
    and LeafIsMacAppStore 
        or anchor apple generic
            and IssuerIsDeveloperID 
            and LeafIsDeveloperIDApp 
            and certificate leaf[subject.OU] = K36BKF7T3D
)
and identifier "com.apple.iWork.Numbers"
```

Now factor the `anchor apple generic` out from both sides of the `or` and move the `identifier "com.apple.iWork.Numbers"` up:

```shell
anchor apple generic 
and identifier "com.apple.iWork.Numbers"
and (
    LeafIsMacAppStore 
        or IssuerIsDeveloperID 
            and LeafIsDeveloperIDApp 
            and certificate leaf[subject.OU] = K36BKF7T3D
)
```

This is exactly the same as the Developer ID DR, except for the Team ID and code signing identifier, and those necessarily change because this is a different app.

The upshot of this is that a Mac App Store app and its Developer ID variant have mutually compatible DRs.  If, to continue the microphone example from earlier, you access the microphone from the Mac App Store variant of your app and then, later on, try to access it from the Developer ID variant, the system allows that access without an additional prompt.

##### Xcode Designated Requirement for Apple Development Code

Here’s the DR of the AppWithTool app signed by Xcode with an Apple Development code signing identity:

```shell
% codesign --display -r - "AppWithTool Dev.app"      
…
designated => 
identifier "com.example.apple-samplecode.AppWithTool" 
and anchor apple generic 
and certificate leaf[subject.CN] = "Apple Development: …" 
and certificate 1[field.1.2.840.113635.100.6.2.1] /* exists */
```

This is much easier to read.  The `anchor apple generic` and `identifier "com.example.apple-samplecode.AppWithTool"` terms were discussed in [`Designated requirement`](tn3127-inside-code-signing-requirements#Designated-requirement.md).

The `certificate leaf[subject.CN] = "Apple Development: …"` requires that the Common Name field of the leaf certificate be `Apple Development: …`.

The `certificate 1[field.1.2.840.113635.100.6.2.1]` term requires that the certificate that issued the leaf certificate include an extension with the OID 1.2.840.113635.100.6.2.1.  This OID is present in the Apple Worldwide Developer Relations Certification Authority signing certificate used by Apple to issue Apple Development signing certificates.

This Apple Development DR is very different from the DR used by Developer ID and Mac App Store apps.  A Mac App Store app won’t satisfy this DR and vice versa.  Returning to the microphone example, if you run an Apple Development variant of your app and use that to access the microphone, and then run a Developer ID or Mac App Store variant of your app, the system  display a prompt when the new app accesses the microphone.

#### Revision History

-  Added the [`Mutually compatible designated requirements`](tn3127-inside-code-signing-requirements#Mutually-compatible-designated-requirements.md) section.  Updated the [`Default and Xcode designated requirements`](tn3127-inside-code-signing-requirements#Default-and-Xcode-designated-requirements.md) to account for the differences between `codesign` and Xcode (r. 124692958).  Made other editorial changes.
-  Made minor editorial changes.
-  Made minor editorial changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3127-inside-code-signing-requirements)*