# MTRAttributeValueWaiter

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 18.3+
- iPadOS 18.3+
- Mac Catalyst 18.3+
- macOS 15.3+
- tvOS 18.3+
- visionOS 2.3+
- watchOS 11.3+

## Declaration

```swift
class MTRAttributeValueWaiter
```

## Topics

### Instance Properties
- [var uuid: UUID](mtrattributevaluewaiter/uuid.md)
### Instance Methods
- [func cancel()](mtrattributevaluewaiter/cancel.md)
  Cancel the wait for the set of attribute path/value pairs represented by this MTRAttributeValueWaiter.  If the completion has not been called yet, it will becalled with MTRErrorCodeCancelled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrattributevaluewaiter)*