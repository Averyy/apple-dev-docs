# CMSSignerStatus

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The constants that indicate the status of the signature and signer information in a signed message.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum CMSSignerStatus
```

```c
enum CMSSignerStatus : uint32_t;
```

## Overview

These are obtained using the [`CMSDecoderCopySignerStatus(_:_:_:_:_:_:_:)`](./cmsdecodercopysignerstatus%28_,_,_,_,_,_,_%29.md) function.

## Topics

### Constants
- [CMSSignerStatus.unsigned](./cmssignerstatus/unsigned.md)
  The message was not signed.
- [CMSSignerStatus.valid](./cmssignerstatus/valid.md)
  The message was signed and both the signature and the signer certificate have been verified.
- [CMSSignerStatus.needsDetachedContent](./cmssignerstatus/needsdetachedcontent.md)
  The message was signed but has detached content. You must call the [`CMSDecoderSetDetachedContent(_:_:)`](./cmsdecodersetdetachedcontent%28_,_%29.md) function before ascertaining the signature status.
- [CMSSignerStatus.invalidSignature](./cmssignerstatus/invalidsignature.md)
  The message was signed but the signature is invalid.
- [CMSSignerStatus.invalidCert](./cmssignerstatus/invalidcert.md)
  The message was signed but the signer’s certificate could not be verified.
- [CMSSignerStatus.invalidIndex](./cmssignerstatus/invalidindex.md)
  The specified value for the signer index (`signerIndex` parameter) is greater than the number of signers of the message minus one (`signerIndex > (numSigners – 1)`).
### Initializers
- [init?(rawValue: UInt32)](./cmssignerstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmssignerstatus)*