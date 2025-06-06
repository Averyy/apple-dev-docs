# Code Signing Information Flags

**Framework**: Security

Use these supplemental flags to retrieve signing information.

#### Overview

Use these constants with the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to specify what type of information to return. See [`Signing Information Dictionary Keys`](signing-information-dictionary-keys.md) for more information about the information returned.

## Topics

### Constants
- [var kSecCSInternalInformation: UInt32](kseccsinternalinformation.md)
  Internal code signing information.
- [var kSecCSSigningInformation: UInt32](kseccssigninginformation.md)
  Cryptographic signing information.
- [var kSecCSRequirementInformation: UInt32](kseccsrequirementinformation.md)
  Code requirements—including the designated requirement—embedded in the code.
- [var kSecCSDynamicInformation: UInt32](kseccsdynamicinformation.md)
  Dynamic validity information about running code.
- [var kSecCSContentInformation: UInt32](kseccscontentinformation.md)
  More information about the file system contents making up the signed code on disk.
- [var kSecCSSkipResourceDirectory: UInt32](kseccsskipresourcedirectory.md)
  Suppress validating the resource directory.
- [var kSecCSCalculateCMSDigest: UInt32](kseccscalculatecmsdigest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/code-signing-information-flags)*