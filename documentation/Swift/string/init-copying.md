# init(copying:)

**Framework**: Swift  
**Kind**: init

Creates a new string, copying the specified code units.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(copying codeUnits: UTF8Span)
```

#### Discussion

This initializer skips UTF-8 validation because `codeUnits` must contain valid UTF-8.

> **Note**: O(n)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(copying:))*