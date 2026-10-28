# LASecret

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

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

```objc
@interface LASecret : NSObject
```

## Overview

You create [`LASecret`](./lasecret.md) instances when you store an [`LAPersistedRight`](./lapersistedright.md); you can’t create them directly.

## Topics

### Loading secret data
- [func loadData(completion: (Data?, (any Error)?) -> Void)](./lasecret/loaddata%28completion%29.md)
  Retrieves data stored in a secret.

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

## See Also

### Persistence
- [class LARightStore](./larightstore.md)
  A container for data protected by a right.
- [class LAPersistedRight](./lapersistedright.md)
  A right that gates access to a key and a secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lasecret)*