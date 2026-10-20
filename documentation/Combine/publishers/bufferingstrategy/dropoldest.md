# Publishers.BufferingStrategy.dropOldest

**Framework**: Combine  
**Kind**: case  
**Role**: Case

When the buffer is full, discard the oldest element in the buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case dropOldest
```

## See Also

### Buffering strategies
- [Publishers.BufferingStrategy.dropNewest](./dropnewest.md)
  When the buffer is full, discard the newly received element.
- [Publishers.BufferingStrategy.customError(_:)](./customerror%28_%29.md)
  When the buffer is full, execute the closure to provide a custom error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/bufferingstrategy/dropoldest)*