# contentImage

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Image shown in the content of the notification.

**Availability**:
- macOS 10.9+ - Deprecated in 11.0

## Declaration

```swift
@NSCopying
var contentImage: NSImage? { get set }
```

```objc
@property (copy, nullable) NSImage * contentImage;
```

## See Also

### Display Information
- [var title: String?](./title.md)
  Specifies the title of the notification.
- [var subtitle: String?](./subtitle.md)
  Specifies the subtitle of the notification.
- [var informativeText: String?](./informativetext.md)
  The body text of the notification.
- [var identifier: String?](./identifier.md)
  A string that uniquely identifies a notification.
- [var response: NSAttributedString?](./response.md)
  The response with which the user responded to a notification.
- [var responsePlaceholder: String?](./responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/contentimage)*