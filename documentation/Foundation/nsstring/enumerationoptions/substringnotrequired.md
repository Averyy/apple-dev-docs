# substringNotRequired

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

A way to indicate that the block does not need substring, in which case `nil` will be passed. This is simply a performance shortcut.

## See Also

- [static var byLines: NSString.EnumerationOptions](nsstring/enumerationoptions/bylines.md)
- [static var byParagraphs: NSString.EnumerationOptions](nsstring/enumerationoptions/byparagraphs.md)
- [static var byComposedCharacterSequences: NSString.EnumerationOptions](nsstring/enumerationoptions/bycomposedcharactersequences.md)
- [static var byWords: NSString.EnumerationOptions](nsstring/enumerationoptions/bywords.md)
- [static var bySentences: NSString.EnumerationOptions](nsstring/enumerationoptions/bysentences.md)
- [static var reverse: NSString.EnumerationOptions](nsstring/enumerationoptions/reverse.md)
- [static var localized: NSString.EnumerationOptions](nsstring/enumerationoptions/localized.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions/substringnotrequired)*