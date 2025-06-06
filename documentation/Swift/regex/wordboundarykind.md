# wordBoundaryKind(_:)

**Framework**: Swift  
**Kind**: method

Returns a regular expression that uses the specified word boundary algorithm.

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
func wordBoundaryKind(_ wordBoundaryKind: RegexWordBoundaryKind) -> Regex<Regex<Output>.RegexOutput>
```

#### Return Value

The modified regular expression.

## Parameters

- `wordBoundaryKind`: The algorithm to use for determining word boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/wordboundarykind(_:))*