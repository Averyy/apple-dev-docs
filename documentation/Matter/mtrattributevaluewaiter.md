# MTRAttributeValueWaiter

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRAttributeValueWaiter : NSObject
```

## Topics

### Instance Properties
- [var uuid: UUID](./mtrattributevaluewaiter/uuid.md)
### Instance Methods
- [func cancel()](./mtrattributevaluewaiter/cancel%28%29.md)
  Cancel the wait for the set of attribute path/value pairs represented by this MTRAttributeValueWaiter.  If the completion has not been called yet, it will becalled with MTRErrorCodeCancelled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrattributevaluewaiter)*