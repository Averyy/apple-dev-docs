# Published.Publisher

**Framework**: Combine  
**Kind**: struct

A publisher for properties marked with the `@Published` attribute.

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
struct Publisher
```

## Topics

### Declaring Publisher Topography
- [Published.Publisher.Output](published/publisher/output.md)
  The kind of values published by this publisher.
- [Published.Publisher.Failure](published/publisher/failure.md)
  The kind of errors this publisher might publish.
### Applying Operators
- [Publisher Operators](published-publisher-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Instance Methods
- [func receive<S>(subscriber: S)](published/publisher/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
### Default Implementations
- [Publisher Implementations](published/publisher/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [var projectedValue: Published<Value>.Publisher](published/projectedvalue.md)
  The property for which this instance exposes a publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/publisher)*