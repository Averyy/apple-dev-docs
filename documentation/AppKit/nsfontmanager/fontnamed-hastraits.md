# fontNamed(_:hasTraits:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the given font has all the specified traits.

**Availability**:
- macOS ?+

## Declaration

```swift
func fontNamed(_ fName: String, hasTraits someTraits: NSFontTraitMask) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the font named `typeface` has all the traits specified in `fontTraitMask`; [`false`](https://developer.apple.com/documentation/swift/false) if it doesn’t.

#### Discussion

Using `NSUnboldFontMask` returns [`true`](https://developer.apple.com/documentation/swift/true) if the font is not bold, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. Using `NSUnitalicFontMask` returns [`true`](https://developer.apple.com/documentation/swift/true) if the font is not italic, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `fName`: The name of the font.
- `someTraits`: The font traits to test, specified by combining the font trait mask values described in   using the C bitwise OR operator.

## See Also

- [func traits(of: NSFont) -> NSFontTraitMask](nsfontmanager/traits(of:).md)
  Returns the traits of the given font.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [func weight(of: NSFont) -> Int](nsfontmanager/weight(of:).md)
  Returns an approximation of the specified font’s weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontnamed(_:hastraits:))*