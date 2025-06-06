# SKAdNetwork 2.1 release notes

**Framework**: StoreKit

A version of SKAdNetwork available in iOS 14 and later.

#### Overview

Use `“2.1”` as the version number when signing ads for this version.

Ad networks are eligible to receive a version 2.1 postback if all three of the following conditions are met:

- The source app generates a signature for version 2.1.
- The source app is built with the iOS 14 SDK or later.
- The advertised app is App Store-signed and running on a device with iOS 14 or later.

##### New Features

New features include:

- SKAdNetwork now signs install-validation postbacks using Apple’s NIST P-256 public key. For more information, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

## See Also

- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md)
  A version of SKAdNetwork available in iOS 16.1 and later.
- [SKAdNetwork 3 release notes](skadnetwork-3-release-notes.md)
  A version of SKAdNetwork available in iOS 14.6 and later.
- [SKAdNetwork 2.2 release notes](skadnetwork-2-2-release-notes.md)
  A version of SKAdNetwork available in iOS 14.5 and later.
- [SKAdNetwork 2 release notes](skadnetwork-2-release-notes.md)
  A version of SKAdNetwork available in iOS 14 and later.
- [SKAdNetwork 1 release notes](skadnetwork-1-release-notes.md)
  A version of SKAdNetwork available in iOS 11.3 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork-2-1-release-notes)*