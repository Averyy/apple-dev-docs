# convert(_:)

**Framework**: AppKit  
**Kind**: method

Converts the specified font using the settings in the receiver, with the aid of the shared `NSFontManager` if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func convert(_ fontObj: NSFont) -> NSFont
```

#### Return Value

The converted font, or `aFont` itself if it can’t be converted.

#### Discussion

For example, if `aFont` is Helvetica Oblique 12.0 point and the user has selected the Times font family (and nothing else) in the Font panel, the font returned is Times Italic 12.0 point.

## Parameters

- `fontObj`: The font to be converted.

## See Also

- [func convert(NSFont) -> NSFont](nsfontmanager/convert(_:).md)
  Converts the given font according to the object that initiated a font change, typically the Font panel or Font menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/convert(_:))*