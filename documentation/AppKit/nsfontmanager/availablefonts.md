# availableFonts

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The names of the fonts available in the system (not the [`NSFont`](../nsfont.md) objects themselves).

**Availability**:
- macOS

## Declaration

```swift
var availableFonts: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * availableFonts;
```

#### Discussion

Note that these fonts are in various system font directories.

## See Also

### Getting Available Fonts
- [var availableFontFamilies: [String]](./availablefontfamilies.md)
  The names of the font families available in the system.
- [func availableFontNames(with: NSFontTraitMask) -> [String]?](./availablefontnames%28with%29.md)
  Returns the names of the fonts available in the system whose traits are described exactly by the given font trait mask (not the `NSFont` objects themselves).
- [func availableMembers(ofFontFamily: String) -> [[Any]]?](./availablemembers%28offontfamily%29.md)
  Returns an array with one entry for each available member of a font family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/availablefonts)*