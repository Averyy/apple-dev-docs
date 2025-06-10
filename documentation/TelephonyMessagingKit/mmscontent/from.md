# from

**Framework**: TelephonyMessagingKit  
**Kind**: property

The sender of the MMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var from: MMSHandle?
```

#### Discussion

The system populates this property for received messages. Don’t populate it when sending a message.

## See Also

- [var recipients: [MMSHandle]](mmscontent/recipients.md)
  The recipients of the MMS message, as an array of MMS handles.
- [struct MMSHandle](mmshandle.md)
  A structure that represents an MMS address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent/from)*