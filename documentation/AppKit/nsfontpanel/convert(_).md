# convert(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts the specified font using the settings in the receiver, with the aid of the shared `NSFontManager` if necessary.

**Availability**:
- macOS

## Declaration

```swift
func convert(_ fontObj: NSFont) -> NSFont
```

```objc
- (NSFont *) panelConvertFont:(NSFont *) fontObj;
```

## Return Value

The converted font, or `aFont` itself if it can’t be converted.

## Discussion

For example, if `aFont` is Helvetica Oblique 12.0 point and the user has selected the Times font family (and nothing else) in the Font panel, the font returned is Times Italic 12.0 point.

## Parameters

- `fontObj`: The font to be converted.

## See Also

### Related Documentation
- [func convert(NSFont) -> NSFont](../nsfontmanager/convert%28_%29.md)
  Converts the given font according to the object that initiated a font change, typically the Font panel or Font menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/convert(_:))*