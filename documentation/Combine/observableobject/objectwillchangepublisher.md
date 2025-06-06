# ObjectWillChangePublisher

**Framework**: Combine  
**Kind**: associatedtype  
**Required**: Yes

The type of publisher that emits before the object has changed.

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
associatedtype ObjectWillChangePublisher : Publisher = ObservableObjectPublisher where Self.ObjectWillChangePublisher.Failure == Never
```

## See Also

- [var objectWillChange: Self.ObjectWillChangePublisher](observableobject/objectwillchange.md)
  A publisher that emits before the object has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/observableobject/objectwillchangepublisher)*