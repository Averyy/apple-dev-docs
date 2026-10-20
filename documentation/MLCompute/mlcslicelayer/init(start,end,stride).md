# init(start:end:stride:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a slice layer with the start, end, and stride you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(start: [Int], end: [Int], stride: [Int]?)
```

## Parameters

- `start`: The start vector.
- `end`: The end vector.
- `stride`: The stride vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcslicelayer/init(start:end:stride:))*