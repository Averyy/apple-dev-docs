# identifier

**Framework**: Foundation  
**Kind**: property

A string that uniquely identifies a notification.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var identifier: String? { get set }
```

#### Discussion

The identifier is unique to a notification. A notification delivered with the same identifier as an existing notification replaces the existing notification rather than causing the display of a new notification.

## See Also

- [var title: String?](nsusernotification/title.md)
  Specifies the title of the notification.
- [var subtitle: String?](nsusernotification/subtitle.md)
  Specifies the subtitle of the notification.
- [var informativeText: String?](nsusernotification/informativetext.md)
  The body text of the notification.
- [var contentImage: NSImage?](nsusernotification/contentimage.md)
  Image shown in the content of the notification.
- [var response: NSAttributedString?](nsusernotification/response.md)
  The response with which the user responded to a notification.
- [var responsePlaceholder: String?](nsusernotification/responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/identifier)*