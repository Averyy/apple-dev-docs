# traits(of:)

**Framework**: AppKit  
**Kind**: method

Returns the traits of the given font.

**Availability**:
- macOS ?+

## Declaration

```swift
func traits(of fontObj: NSFont) -> NSFontTraitMask
```

#### Return Value

The font traits, returned as a mask created by combining values listed in `Constants` with the C bitwise OR operator.

## Parameters

- `fontObj`: The font whose traits are returned.

## See Also

- [func fontNamed(String, hasTraits: NSFontTraitMask) -> Bool](nsfontmanager/fontnamed(_:hastraits:).md)
  Indicates whether the given font has all the specified traits.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [func weight(of: NSFont) -> Int](nsfontmanager/weight(of:).md)
  Returns an approximation of the specified font’s weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/traits(of:))*