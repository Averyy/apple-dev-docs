# wordBoundary

**Framework**: RegexBuilder  
**Kind**: property

An anchor that matches at a word boundary.

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
static var wordBoundary: Anchor { get }
```

#### Discussion

Word boundaries are identified using the Unicode default word boundary algorithm by default. To specify a different word boundary algorithm, use the `wordBoundaryKind(_:)` method.

This anchor is equivalent to `\b` in regex syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/anchor/wordboundary)*