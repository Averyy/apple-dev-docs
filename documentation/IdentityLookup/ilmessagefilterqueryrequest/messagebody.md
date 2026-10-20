# messageBody

**Framework**: SMS and Call Reporting  
**Kind**: property  
**Role**: Instance Property

The body of a message received from an unknown sender.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var messageBody: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * messageBody;
```

## See Also

### Getting Information About a Message
- [var sender: String?](./sender.md)
  The sender of the message.
- [var receiverISOCountryCode: String?](./receiverisocountrycode.md)
  The ISO Country Code of the receiving phone number, in format specified by the ISO 3166-2 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryrequest/messagebody)*