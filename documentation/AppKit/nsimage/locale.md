# locale

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image’s preferred locale for resolving representations, if one has been specified using `-imageWithLocale:`. Otherwise, `nil`.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var locale: Locale? { get }
```

```objc
@property (copy, readonly, nullable) NSLocale * locale;
```

## See Also

### Localizing Images
- [func withLocale(Locale?) -> NSImage](./withlocale%28_%29.md)
  Creates and returns a new image with the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/locale)*