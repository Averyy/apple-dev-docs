# ObservableObjectPublisher

**Framework**: Combine  
**Kind**: class

A publisher that publishes changes from observable objects.

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
final class ObservableObjectPublisher
```

## Topics

### Creating an Observable Object Publisher
- [init()](observableobjectpublisher/init.md)
  Creates an observable object publisher instance.
### Declaring Publisher Topography
- [ObservableObjectPublisher.Output](observableobjectpublisher/output.md)
  The kind of values published by this publisher.
- [ObservableObjectPublisher.Failure](observableobjectpublisher/failure.md)
  The kind of errors this publisher might publish.
### Delivering Elements to Subscribers
- [func send()](observableobjectpublisher/send.md)
  Sends the changed value to the downstream subscriber.
### Applying Operators
- [Publisher Operators](observableobjectpublisher-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](observableobjectpublisher/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [protocol ObservableObject](observableobject.md)
  A type of object with a publisher that emits before the object has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/observableobjectpublisher)*