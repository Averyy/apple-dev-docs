# identifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string that uniquely identifies a notification.

**Availability**:
- macOS 10.9+ - Deprecated in 11.0

## Declaration

```swift
var identifier: String? { get set }
```

```objc
@property (copy, nullable) NSString * identifier;
```

## Discussion

The identifier is unique to a notification. A notification delivered with the same identifier as an existing notification replaces the existing notification rather than causing the display of a new notification.

## See Also

### Display Information
- [var title: String?](./title.md)
  Specifies the title of the notification.
- [var subtitle: String?](./subtitle.md)
  Specifies the subtitle of the notification.
- [var informativeText: String?](./informativetext.md)
  The body text of the notification.
- [var contentImage: NSImage?](./contentimage.md)
  Image shown in the content of the notification.
- [var response: NSAttributedString?](./response.md)
  The response with which the user responded to a notification.
- [var responsePlaceholder: String?](./responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/identifier)*