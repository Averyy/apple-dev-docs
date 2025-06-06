# buildPartialBlock(first:)

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
static func buildPartialBlock<R, W, C1, C2, C3, C4>(first regex: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?)> where R : RegexComponent, R.RegexOutput == (W, C1, C2, C3, C4)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/alternationbuilder/buildpartialblock(first:)-6mjz0)*