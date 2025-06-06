# Importing an Identity

**Framework**: Security

Learn how to import an identity from file.

#### Overview

Because it contains a private key, an identity must be kept secret. Though you might store a certificate by itself in an unencrypted, DER-encoded file and pass it around freely, you typically wouldn’t store or transmit an identity this way. The PKCS #12 file format, on the other hand, provides a means to store sensitive cryptographic objects in a password-protected container.

When you receive a PKCS #12 file (often with a `p12` extension) on a Mac, the Keychain Access app handles it by default. If the file is password protected, the app first prompts for a password when you open it. The contents of the file are then stored in the most recently selected keychain. And although file might include a variety of different cryptographic objects, it’s often used simply to transmit an identity.

You can also import a PKCS #12 file directly into your app using the certificate, key, and trust services API. This might be useful if you need to securely communicate a new identity to your app in the field. As a concrete example, suppose your app has fetched such a file from a secure website and stored it locally at a particular file URL. You begin by reading this file into a data object:

An identity is a secret that you guard closely by applying a strong password to the PKCS #12 data. In fact, the CKTS API won’t even import PKCS #12 data that lacks a password. In order to supply the password during import, you create an options dictionary with the password string:

> ❗ **Important**:  Do not bundle passwords with your app in any form. Doing so is insecure, because no matter how carefully you try to obscure a password, a motivated attacker will find a way to mimic the operations you use to reveal it for your own purposes. Instead, prompt the user for a password when you need it, or read it from the secure storage offered by a keychain.

 Do not bundle passwords with your app in any form. Doing so is insecure, because no matter how carefully you try to obscure a password, a motivated attacker will find a way to mimic the operations you use to reveal it for your own purposes. Instead, prompt the user for a password when you need it, or read it from the secure storage offered by a keychain.

Then, use the data and the options in a call to the [`SecPKCS12Import(_:_:_:)`](secpkcs12import(_:_:_:).md) function:

Because the PKCS #12 format allows for bundling multiple cryptographic objects together, this function populates an array object. Typically, you iterate over every object in the array, handling each one in turn. In this case, assume that you are interested in only the first item. If the import function returns no error, and if at least one array item exists, you extract that as the first item in the array, which is a dictionary:

Notice that in Objective-C, you first pass ownership of the array and its contents to Automatic Reference Counting (ARC), which handles releasing it later. In Swift, the system automatically takes ownership. Either way, this dictionary held by the first item may contain these keys:

- [`kSecImportItemIdentity`](ksecimportitemidentity.md)—Value contains the certificate and private key wrapped together as an identity.
- [`kSecImportItemCertChain`](ksecimportitemcertchain.md)—Value contains the chain of certificates relevant to evaluating the trust of the certificate contained in the identity.
- [`kSecImportItemTrust`](ksecimportitemtrust.md)—Value contains a trust that’s set up with all of the relevant intermediate certificates. The trust is not guaranteed to evaluate successfully.
- [`kSecImportItemKeyID`](ksecimportitemkeyid.md)—Value contains a key ID that’s often the SHA-1 digest of the public key in the identity.
- [`kSecImportItemLabel`](ksecimportitemlabel.md)—Value contains an item label. This label is not guaranteed to be in any particular format but is typically the same string returned by the [`SecCertificateCopySubjectSummary(_:)`](seccertificatecopysubjectsummary(_:).md) function for the certificate embedded in the identity.

To get the identity object, use the [`kSecImportItemIdentity`](ksecimportitemidentity.md) key:

You can additionally read a trust object from the dictionary in a similar way, using the appropriate key. For example:

See [`Evaluating a Trust and Parsing the Result`](evaluating-a-trust-and-parsing-the-result.md) for details on how to use the trust to evaluate the certificate.

> **Note**:  In macOS, when it succeeds, the [`SecPKCS12Import(_:_:_:)`](secpkcs12import(_:_:_:).md) function call automatically stores the extracted identity in the default keychain in addition to returning a reference to it as one of the items in the array of dictionaries.

 In macOS, when it succeeds, the [`SecPKCS12Import(_:_:_:)`](secpkcs12import(_:_:_:).md) function call automatically stores the extracted identity in the default keychain in addition to returning a reference to it as one of the items in the array of dictionaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/importing-an-identity)*