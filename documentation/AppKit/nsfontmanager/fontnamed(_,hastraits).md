# fontNamed(_:hasTraits:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the given font has all the specified traits.

**Availability**:
- macOS

## Declaration

```swift
func fontNamed(_ fName: String, hasTraits someTraits: NSFontTraitMask) -> Bool
```

```objc
- (BOOL) fontNamed:(NSString *) fName hasTraits:(NSFontTraitMask) someTraits;
```

#### Return Value

[`true`](../../Swift/true.md) if the font named `typeface` has all the traits specified in `fontTraitMask`; [`false`](../../Swift/false.md) if it doesn’t.

#### Discussion

Using `NSUnboldFontMask` returns [`true`](../../Swift/true.md) if the font is not bold, [`false`](../../Swift/false.md) otherwise. Using `NSUnitalicFontMask` returns [`true`](../../Swift/true.md) if the font is not italic, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `fName`: The name of the font.
- `someTraits`: The font traits to test, specified by combining the font trait mask values described in `Constants` using the C bitwise OR operator.

## See Also

### Examining Fonts
- [func traits(of: NSFont) -> NSFontTraitMask](./traits%28of%29.md)
  Returns the traits of the given font.
- [struct NSFontTraitMask](../nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [func weight(of: NSFont) -> Int](./weight%28of%29.md)
  Returns an approximation of the specified font’s weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontnamed(_:hastraits:))*