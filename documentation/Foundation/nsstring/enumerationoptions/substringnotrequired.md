# substringNotRequired

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var substringNotRequired: NSString.EnumerationOptions { get }
```

```c
NSStringEnumerationSubstringNotRequired
```

#### Discussion

A way to indicate that the block does not need substring, in which case `nil` will be passed. This is simply a performance shortcut.

## See Also

### Constants
- [static var byLines: NSString.EnumerationOptions](./bylines.md)
- [static var byParagraphs: NSString.EnumerationOptions](./byparagraphs.md)
- [static var byComposedCharacterSequences: NSString.EnumerationOptions](./bycomposedcharactersequences.md)
- [static var byWords: NSString.EnumerationOptions](./bywords.md)
- [static var bySentences: NSString.EnumerationOptions](./bysentences.md)
- [static var reverse: NSString.EnumerationOptions](./reverse.md)
- [static var localized: NSString.EnumerationOptions](./localized.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/substringnotrequired)*