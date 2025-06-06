# ObservableObjectPublisher.Failure

**Framework**: Combine  
**Kind**: typealias

The kind of errors this publisher might publish.

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
typealias Failure = Never
```

#### Discussion

Use `Never` if this `Publisher` does not publish errors.

## See Also

- [ObservableObjectPublisher.Output](observableobjectpublisher/output.md)
  The kind of values published by this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/observableobjectpublisher/failure)*