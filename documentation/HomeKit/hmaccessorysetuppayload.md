# HMAccessorySetupPayload

**Framework**: HomeKit  
**Kind**: class

A payload for authenticating a HomeKit accessory.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 27.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
class HMAccessorySetupPayload
```

#### Overview

The setup payload provides a URL to authenticate an accessory. Typically, the URL comes from scanning a QR code on the accessory. Use a setup payload to authenticate devices that are already deployed, for which scanning a QR code would be difficult, or if you need to provide an optional ownership token that you negotiate with the accessory outside of HomeKit.

For details about the payload’s content, please join the [`MFi Program`](https://developer.apple.comhttps://developer.apple.com/programs/mfi/).

## Topics

### Creating a Payload
- [init?(url: URL?)](hmaccessorysetuppayload/init(url:)-7ytm5.md)
  Creates an accessory setup payload.
- [init?(url: URL, ownershipToken: HMAccessoryOwnershipToken?)](hmaccessorysetuppayload/init(url:ownershiptoken:)-32mrj.md)
  Creates an accessory setup payload instance that includes an ownership token.
- [class HMAccessoryOwnershipToken](hmaccessoryownershiptoken.md)
  Authentication data that your app provides when adding an accessory to a home.
### Initializers
- [init?(URL: URL?)](hmaccessorysetuppayload/init(url:)-j8tu.md)
- [init?(URL: URL, ownershipToken: HMAccessoryOwnershipToken?)](hmaccessorysetuppayload/init(url:ownershiptoken:)-24qin.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuppayload)*