# simple

**Framework**: Swift  
**Kind**: property

A word boundary algorithm that implements the “simple word boundary” Unicode recommendation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var simple: RegexWordBoundaryKind { get }
```

#### Discussion

A simple word boundary is a position in the input between two characters that match `/\w\W/` or `/\W\w/`, or between the start or end of the input and a `\w` character. Word boundaries therefore depend on the option- defined behavior of `\w`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexwordboundarykind/simple)*