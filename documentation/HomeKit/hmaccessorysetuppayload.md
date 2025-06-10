# HMAccessorySetupPayload

**Framework**: HomeKit  
**Kind**: class

A payload for authenticating a HomeKit accessory.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
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
- [init?(url: URL?)](hmaccessorysetuppayload/init(url:).md)
  Creates an accessory setup payload.
- [init?(url: URL, ownershipToken: HMAccessoryOwnershipToken?)](hmaccessorysetuppayload/init(url:ownershiptoken:).md)
  Creates an accessory setup payload instance that includes an ownership token.
- [class HMAccessoryOwnershipToken](hmaccessoryownershiptoken.md)
  Authentication data that your app provides when adding an accessory to a home.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuppayload)*