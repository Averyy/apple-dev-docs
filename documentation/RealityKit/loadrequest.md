# LoadRequest

**Framework**: RealityKit  
**Kind**: class

A resource loader that acts as a publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
class LoadRequest<Output>
```

## Topics

### Getting the result
- [var result: Result<Output, any Error>?](loadrequest/result.md)
  The result of the load operation.
### Instance Methods
- [func subscribe<S>(S)](loadrequest/subscribe(_:).md)
  Attaches the specified subscriber to this publisher.

## Relationships

### Conforms To
- [Publisher](../Combine/Publisher.md)

## See Also

- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest)*