# body

**Framework**: Message UI  
**Kind**: property  
**Role**: Instance Property

The initial content of the message.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var body: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * body;
```

#### Discussion

If you want to provide initial content in the body of a message, do so before you display it. After the message is displayed you cannot change the value of this property.

## See Also

### Setting the initial message information
- [var recipients: [String]?](./recipients.md)
  An array of strings that contains the initial recipients of the message.
- [var subject: String?](./subject.md)
  The initial subject of the message.
- [var message: MSMessage?](./message.md)
  A message object from your iMessage app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/body)*