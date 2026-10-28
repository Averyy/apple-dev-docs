# traits(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the traits of the given font.

**Availability**:
- macOS

## Declaration

```swift
func traits(of fontObj: NSFont) -> NSFontTraitMask
```

```objc
- (NSFontTraitMask) traitsOfFont:(NSFont *) fontObj;
```

## Return Value

The font traits, returned as a mask created by combining values listed in `Constants` with the C bitwise OR operator.

## Parameters

- `fontObj`: The font whose traits are returned.

## See Also

### Examining Fonts
- [func fontNamed(String, hasTraits: NSFontTraitMask) -> Bool](./fontnamed%28_,hastraits%29.md)
  Indicates whether the given font has all the specified traits.
- [struct NSFontTraitMask](../nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [func weight(of: NSFont) -> Int](./weight%28of%29.md)
  Returns an approximation of the specified font’s weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/traits(of:))*