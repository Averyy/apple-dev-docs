# applyListOrder(_:)

**Framework**: Swift  
**Kind**: method

Reorders elements in place to match `order`, preserving elements not in `order`. Implements USD’s “ordered” list-op semantics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func applyListOrder(_ order: [USDToken])
```

## Parameters

- `order`: The desired ordering for elements that appear in both `self` and `order`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/applylistorder(_:)-8ncuj)*