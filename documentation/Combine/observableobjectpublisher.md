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

### Creating an observable object publisher
- [init()](observableobjectpublisher/init.md)
  Creates an observable object publisher instance.
### Delivering elements to subscribers
- [func send()](observableobjectpublisher/send.md)
  Sends the changed value to the downstream subscriber.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [protocol ObservableObject](observableobject.md)
  A type of object with a publisher that emits before the object has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/observableobjectpublisher)*