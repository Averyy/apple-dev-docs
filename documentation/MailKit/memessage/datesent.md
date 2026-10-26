# dateSent

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

The date the sender sent the message.

**Availability**:
- macOS 12.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * dateSent;
```

#### Discussion

This property corresponds to the Date header in the message. The message sender sets this header, and it may not be present.

## See Also

### Accessing the Sent and Received Dates
- [dateReceived](./datereceived.md)
  The date that the recipient received the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/datesent)*