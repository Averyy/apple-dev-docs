# sender

**Framework**: SMS and Call Reporting  
**Kind**: property  
**Role**: Instance Property

The sender of the message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var sender: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * sender;
```

## See Also

### Getting Information About a Message
- [var messageBody: String?](./messagebody.md)
  The body of a message received from an unknown sender.
- [var receiverISOCountryCode: String?](./receiverisocountrycode.md)
  The ISO Country Code of the receiving phone number, in format specified by the ISO 3166-2 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryrequest/sender)*