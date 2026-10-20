# receiverISOCountryCode

**Framework**: SMS and Call Reporting  
**Kind**: property  
**Role**: Instance Property

The ISO Country Code of the receiving phone number, in format specified by the ISO 3166-2 standard.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var receiverISOCountryCode: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * receiverISOCountryCode;
```

## See Also

### Getting Information About a Message
- [var sender: String?](./sender.md)
  The sender of the message.
- [var messageBody: String?](./messagebody.md)
  The body of a message received from an unknown sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryrequest/receiverisocountrycode)*