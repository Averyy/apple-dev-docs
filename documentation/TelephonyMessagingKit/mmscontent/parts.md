# parts

**Framework**: TelephonyMessagingKit  
**Kind**: property

The individual parts of the MMS message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var parts: [MMSPartContent]
```

#### Discussion

When sending an MMS, add the individual parts to this array. When receiving an MMS, inspect this array to receive the MMS parts, in order.

## See Also

- [struct MMSPartContent](mmspartcontent.md)
  A structure that defines custom headers within MMS content.
- [var subject: String?](mmscontent/subject.md)
  The subject of the MMS message.
- [var headers: [String : String]](mmscontent/headers.md)
  Additional headers in a received MMS message, as a key-value dictionary of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent/parts)*