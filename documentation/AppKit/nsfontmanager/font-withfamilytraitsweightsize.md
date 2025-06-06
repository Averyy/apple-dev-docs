# font(withFamily:traits:weight:size:)

**Framework**: AppKit  
**Kind**: method

Attempts to load a font with the specified characteristics.

**Availability**:
- macOS ?+

## Declaration

```swift
func font(withFamily family: String, traits: NSFontTraitMask, weight: Int, size: CGFloat) -> NSFont?
```

#### Return Value

A font with the specified characteristics if successful, or `nil` if not.

## Parameters

- `family`: The generic name of the desired font, such as Times or Helvetica.
- `traits`: The font traits, specified by combining the font trait mask values described in   using the C bitwise OR operator. Using   or   loads a font that doesn’t have either the bold or italic trait, respectively.
- `weight`: A hint for the weight desired, on a scale of 0 to 15: a value of 5 indicates a normal or book weight, and 9 or more a bold or heavier weight. The weight is ignored if   includes  .
- `size`: The point size of the desired font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/font(withfamily:traits:weight:size:))*