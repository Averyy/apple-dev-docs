# parts

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The individual parts of the MMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var parts: [MMSPartContent]
```

## Discussion

When sending an MMS, add the individual parts to this array. When receiving an MMS, inspect this array to receive the MMS parts, in order.

## See Also

### Accessing content properties
- [struct MMSPartContent](../mmspartcontent.md)
  A structure that defines custom headers within MMS content.
- [var subject: String?](./subject.md)
  The subject of the MMS message.
- [var headers: [String : String]](./headers.md)
  Additional headers in a received MMS message, as a key-value dictionary of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent/parts)*