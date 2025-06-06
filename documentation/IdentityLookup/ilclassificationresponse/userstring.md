# userString

**Framework**: SMS and Call Reporting  
**Kind**: property

Text included in a response sent over SMS.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var userString: String? { get set }
```

#### Discussion

Use this property if you set the `ILClassificationExtensionSMSReportDestination` key in the extension’s `Info.plist` file. The string can store additional data that you want to pass in the SMS message.

## See Also

- [var action: ILClassificationAction](ilclassificationresponse/action.md)
  A classification that determines what action the system takes.
- [var userInfo: [String : Any]?](ilclassificationresponse/userinfo.md)
  JSON data included in a response sent over the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationresponse/userstring)*