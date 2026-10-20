# LoadRequest

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A resource loader that acts as a publisher.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class LoadRequest<Output>
```

## Topics

### Getting the result
- [var result: Result<Output, any Error>?](./loadrequest/result.md)
  The result of the load operation.
### Instance Methods
- [func subscribe<S>(S)](./loadrequest/subscribe%28_%29.md)
  Attaches the specified subscriber to this publisher.

## Relationships

### Conforms To
- [Publisher](../Combine/publisher.md)

## See Also

### Essentials
- [Loading entities from a file](./loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest)*