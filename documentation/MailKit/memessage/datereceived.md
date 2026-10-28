# dateReceived

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

The date that the recipient received the message.

**Availability**:
- macOS 12.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * dateReceived;
```

## Discussion

This property is only available if the message has been delivered. For example, it isn’t present in a draft message.

## See Also

### Accessing the Sent and Received Dates
- [dateSent](./datesent.md)
  The date the sender sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/datereceived)*