# withLocale(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a new image with the specified locale.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func withLocale(_ locale: Locale?) -> NSImage
```

```objc
- (NSImage *) imageWithLocale:(NSLocale *) locale;
```

#### Discussion

If the receiver contains locale-sensitive representations, the returned image will prefer to draw using representations appropriate for the specified locale. If locale is `nil`, the returned image uses the default behavior of choosing representations appropriate for the system’s currently-configured locale.

## See Also

### Localizing Images
- [var locale: Locale?](./locale.md)
  The image’s preferred locale for resolving representations, if one has been specified using `-imageWithLocale:`. Otherwise, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/withlocale(_:))*