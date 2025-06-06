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

The message’s body contains a JSON string with both the classification action and the contents of the user info dictionary. For more information, see [`NSJSONSerialization`](https://developer.apple.com/documentation/foundation/nsjsonserialization).

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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [enum ILClassificationAction](ilclassificationaction.md)
  The actions the system can take in response to the reported communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationresponse)*