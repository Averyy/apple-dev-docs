# Guest Creation Flags

**Framework**: Security

Use these supplemental flags to create a guest object.

#### Overview

These flags supplement the flags described in [`SecCSFlags`](seccsflags.md). Use these additional constants with the flags parameter of the [`SecHostCreateGuest`](sechostcreateguest.md) function.

## Topics

### Constants
- [var kSecCSDedicatedHost: UInt32](kseccsdedicatedhost.md)
  Declares dedicated hosting for the given host.
- [var kSecCSGenerateGuestHash: UInt32](kseccsgenerateguesthash.md)
  Ask the host to generate the unique binary identifier ([`kSecCodeInfoUnique`](kseccodeinfounique.md)) from the copy on disk at the path given.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/guest-creation-flags)*