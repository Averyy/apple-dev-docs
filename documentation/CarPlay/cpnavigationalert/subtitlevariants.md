# subtitleVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of subtitle strings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var subtitleVariants: [String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * subtitleVariants;
```

#### Discussion

Each subtitle should be localized and ready for display to the user. The system selects the subtitle to display based on the available screen space.

## See Also

### Getting Titles
- [var titleVariants: [String]](./titlevariants.md)
  An array of title strings.
- [func updateTitleVariants([String], subtitleVariants: [String])](./updatetitlevariants%28_,subtitlevariants%29.md)
  Updates title and subtitle variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/subtitlevariants)*