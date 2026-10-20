# ILClassificationResponse

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

A response object that tells the system how to handle the reported communications.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILClassificationResponse
```

```objc
@interface ILClassificationResponse : NSObject
```

#### Overview

To work in areas where Wi-Fi connections and cellular data may be unreliable, the extension sends the response using an SMS message. As long as the action isn’t [`ILClassificationAction.none`](./ilclassificationaction/none.md), the extension creates an SMS message to the number provided by the `ILClassificationExtensionSMSReportDestination` key in the extension’s `info.plist` file.

The message’s body contains a JSON string with both the classification action and the contents of the user info dictionary. For more information, see [`JSONSerialization`](../Foundation/jsonserialization.md).

## Topics

### Creating Responses
- [init(action: ILClassificationAction)](./ilclassificationresponse/init%28action%29.md)
  Creates a new response using the provided classification.
### Accessing Data
- [var action: ILClassificationAction](./ilclassificationresponse/action.md)
  A classification that determines what action the system takes.
- [var userInfo: [String : Any]?](./ilclassificationresponse/userinfo.md)
  JSON data included in a response sent over the network.
- [var userString: String?](./ilclassificationresponse/userstring.md)
  Text included in a response sent over SMS.
### Initializers
- [init(classificationAction: ILClassificationAction)](./ilclassificationresponse/init%28classificationaction%29.md)
- [init?(coder: NSCoder)](./ilclassificationresponse/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Responses
- [enum ILClassificationAction](./ilclassificationaction.md)
  The actions the system can take in response to the reported communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationresponse)*