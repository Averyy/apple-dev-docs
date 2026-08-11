# MSUPIRequest

**Framework**: Messages  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class MSUPIRequest
```

#### Overview

Request for UPI (Unified Payments Interface) device validation.

In order to use this API, you must use the managed entitlement `com.apple.developer.upi-device-validation`. This API is only functional on devices with SMS capability, and only compatible with non-iMessagable recipients.

## Topics

### Initializers
- [init(validationToken: String, recipients: [String])](msupirequest/init(validationtoken:recipients:).md)
### Instance Properties
- [var recipients: [String]](msupirequest/recipients.md)
- [var validationToken: String](msupirequest/validationtoken.md)
### Instance Methods
- [func send(completionHandler: (Bool) -> Void)](msupirequest/send(completionhandler:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msupirequest)*