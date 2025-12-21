# headers

**Framework**: TelephonyMessagingKit  
**Kind**: property

Additional headers in a received MMS message, as a key-value dictionary of strings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var headers: [String : String]
```

#### Discussion

Don’t populate this dictionary when sending a message.

## See Also

- [var parts: [MMSPartContent]](mmscontent/parts.md)
  The individual parts of the MMS message.
- [struct MMSPartContent](mmspartcontent.md)
  A structure that defines custom headers within MMS content.
- [var subject: String?](mmscontent/subject.md)
  The subject of the MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent/headers)*