# LASecret

**Framework**: Local Authentication  
**Kind**: class

Data that’s protected by a persisted right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LASecret
```

#### Overview

You create [`LASecret`](lasecret.md) instances when you store an [`LAPersistedRight`](lapersistedright.md); you can’t create them directly.

## Topics

### Loading secret data
- [func loadData(completion: (Data?, (any Error)?) -> Void)](lasecret/loaddata(completion:).md)
  Retrieves data stored in a secret.

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

## See Also

- [class LARightStore](larightstore.md)
  A container for data protected by a right.
- [class LAPersistedRight](lapersistedright.md)
  A right that gates access to a key and a secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lasecret)*