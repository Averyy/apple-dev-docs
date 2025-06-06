# buildPartialBlock(accumulated:next:)

**Framework**: RegexBuilder  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?)>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/alternationbuilder/buildpartialblock(accumulated:next:)-6yu9n)*