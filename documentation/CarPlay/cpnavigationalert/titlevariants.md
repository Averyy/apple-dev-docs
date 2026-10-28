# titleVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of title strings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var titleVariants: [String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * titleVariants;
```

## Discussion

Each title should be localized and ready for display to the user. The system selects the title to display based on the available screen space.

## See Also

### Getting Titles
- [var subtitleVariants: [String]](./subtitlevariants.md)
  An array of subtitle strings.
- [func updateTitleVariants([String], subtitleVariants: [String])](./updatetitlevariants%28_,subtitlevariants%29.md)
  Updates title and subtitle variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/titlevariants)*