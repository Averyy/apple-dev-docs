# MSUPIRequest

**Framework**: Messages  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class MSUPIRequest
```

```objc
@interface MSUPIRequest : NSObject
```

#### Overview

Request for UPI (Unified Payments Interface) device validation.

In order to use this API, you must use the managed entitlement `com.apple.developer.upi-device-validation`. This API is only functional on devices with SMS capability, and only compatible with non-iMessagable recipients.

## Topics

### Initializers
- [init(validationToken: String, recipients: [String])](./msupirequest/init%28validationtoken,recipients%29.md)
### Instance Properties
- [var recipients: [String]](./msupirequest/recipients.md)
- [var validationToken: String](./msupirequest/validationtoken.md)
### Instance Methods
- [func send(completionHandler: (Bool) -> Void)](./msupirequest/send%28completionhandler%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msupirequest)*