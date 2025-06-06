# weight(of:)

**Framework**: AppKit  
**Kind**: method

Returns an approximation of the specified font’s weight.

**Availability**:
- macOS ?+

## Declaration

```swift
func weight(of fontObj: NSFont) -> Int
```

#### Return Value

An approximation of the weight of the given font, where 0 indicates the lightest possible weight, 5 indicates a normal or book weight, and 9 or more indicates a bold or heavier weight. Because this method returns only an approximation of a font’s weight, it is not guaranteed to return the exact weight with which `fontObj` was initialized.

## Parameters

- `fontObj`: The font whose approximate weight is returned.

## See Also

- [func traits(of: NSFont) -> NSFontTraitMask](nsfontmanager/traits(of:).md)
  Returns the traits of the given font.
- [func fontNamed(String, hasTraits: NSFontTraitMask) -> Bool](nsfontmanager/fontnamed(_:hastraits:).md)
  Indicates whether the given font has all the specified traits.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/weight(of:))*