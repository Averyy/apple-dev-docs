# informativeText

**Framework**: Foundation  
**Kind**: property

The body text of the notification.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var informativeText: String? { get set }
```

#### Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

## See Also

- [var title: String?](nsusernotification/title.md)
  Specifies the title of the notification.
- [var subtitle: String?](nsusernotification/subtitle.md)
  Specifies the subtitle of the notification.
- [var contentImage: NSImage?](nsusernotification/contentimage.md)
  Image shown in the content of the notification.
- [var identifier: String?](nsusernotification/identifier.md)
  A string that uniquely identifies a notification.
- [var response: NSAttributedString?](nsusernotification/response.md)
  The response with which the user responded to a notification.
- [var responsePlaceholder: String?](nsusernotification/responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/informativetext)*