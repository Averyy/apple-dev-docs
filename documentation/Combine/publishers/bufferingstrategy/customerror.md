# Publishers.BufferingStrategy.customError(_:)

**Framework**: Combine  
**Kind**: case

When the buffer is full, execute the closure to provide a custom error.

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
case customError(() -> Failure)
```

## See Also

- [Publishers.BufferingStrategy.dropNewest](publishers/bufferingstrategy/dropnewest.md)
  When the buffer is full, discard the newly received element.
- [Publishers.BufferingStrategy.dropOldest](publishers/bufferingstrategy/dropoldest.md)
  When the buffer is full, discard the oldest element in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/bufferingstrategy/customerror(_:))*