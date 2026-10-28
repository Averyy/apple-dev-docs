# CMSSignedAttributes

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

Optional attributes you can add to a signed message.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct CMSSignedAttributes
```

```c
enum CMSSignedAttributes : uint32_t;
```

## Overview

Use these flags with the [`CMSEncoderAddSignedAttributes(_:_:)`](./cmsencoderaddsignedattributes%28_,_%29.md) method to cause the encoder to add attributes to a signed message that can be interpreted by the recipient. These attributes are not used for unsigned messages.

## Topics

### Attributes
- [static var attrSmimeCapabilities: CMSSignedAttributes](./cmssignedattributes/attrsmimecapabilities.md)
  Identify signature, encryption, and digest algorithms supported by the encoder.
- [static var attrSmimeEncryptionKeyPrefs: CMSSignedAttributes](./cmssignedattributes/attrsmimeencryptionkeyprefs.md)
  Indicate that the signing certificate included with the message is the preferred one for S/MIME encryption.
- [static var attrSmimeMSEncryptionKeyPrefs: CMSSignedAttributes](./cmssignedattributes/attrsmimemsencryptionkeyprefs.md)
  Indicate that the signing certificate included with the message is the preferred one for S/MIME encryption, but using an attribute object identifier (OID) preferred by Microsoft.
- [static var attrSigningTime: CMSSignedAttributes](./cmssignedattributes/attrsigningtime.md)
  Include the signing time.
- [static var attrAppleCodesigningHashAgility: CMSSignedAttributes](./cmssignedattributes/attrapplecodesigninghashagility.md)
  Include Apple codesigning hash agility.
- [static var attrAppleCodesigningHashAgilityV2: CMSSignedAttributes](./cmssignedattributes/attrapplecodesigninghashagilityv2.md)
  Include Apple codesigning hash agility, version 2.
- [static var attrAppleExpirationTime: CMSSignedAttributes](./cmssignedattributes/attrappleexpirationtime.md)
  Include the expiration time.
- [kCMSAttrNone](./cmssignedattributes/kcmsattrnone.md)
  No attributes.
### Initializers
- [init(rawValue: UInt32)](./cmssignedattributes/init%28rawvalue%29.md)
  Initializes a new attributes structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmssignedattributes)*