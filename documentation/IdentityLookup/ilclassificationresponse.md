# ILClassificationResponse

**Framework**: SMS and Call Reporting  
**Kind**: class

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

#### Overview

To work in areas where Wi-Fi connections and cellular data may be unreliable, the extension sends the response using an SMS message. As long as the action isn’t [`ILClassificationAction.none`](ilclassificationaction/none.md), the extension creates an SMS message to the number provided by the `ILClassificationExtensionSMSReportDestination` key in the extension’s `info.plist` file.

The message’s body contains a JSON string with both the classification action and the contents of the user info dictionary. For more information, see [`JSONSerialization`](https://developer.apple.com/documentation/foundation/jsonserialization).

## Topics

### Creating Responses
- [init(action: ILClassificationAction)](ilclassificationresponse/init(action:).md)
  Creates a new response using the provided classification.
### Accessing Data
- [var action: ILClassificationAction](ilclassificationresponse/action.md)
  A classification that determines what action the system takes.
- [var userInfo: [String : Any]?](ilclassificationresponse/userinfo.md)
  JSON data included in a response sent over the network.
- [var userString: String?](ilclassificationresponse/userstring.md)
  Text included in a response sent over SMS.
### Initializers
- [init(classificationAction: ILClassificationAction)](ilclassificationresponse/init(classificationaction:).md)
- [init?(coder: NSCoder)](ilclassificationresponse/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [enum ILClassificationAction](ilclassificationaction.md)
  The actions the system can take in response to the reported communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationresponse)*