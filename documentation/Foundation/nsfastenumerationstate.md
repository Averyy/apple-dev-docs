# NSFastEnumerationState

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

This defines the structure used as contextual information in the [`NSFastEnumeration`](./nsfastenumeration.md) protocol.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSFastEnumerationState
```

```c
typedef struct { ... } NSFastEnumerationState;
```

#### Overview

For more information, see [`countByEnumerating(with:objects:count:)`](./nsfastenumeration/countbyenumerating%28with,objects,count%29.md).

## Topics

### Initializers
- [init()](./nsfastenumerationstate/init%28%29.md)
- [init(state: UInt, itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>?, mutationsPtr: UnsafeMutablePointer<UInt>?, extra: (UInt, UInt, UInt, UInt, UInt))](./nsfastenumerationstate/init%28state,itemsptr,mutationsptr,extra%29.md)
### Instance Properties
- [var extra: (UInt, UInt, UInt, UInt, UInt)](./nsfastenumerationstate/extra.md)
  A C array that you can use to hold returned values.
- [var itemsPtr: AutoreleasingUnsafeMutablePointer<AnyObject?>?](./nsfastenumerationstate/itemsptr.md)
  A C array of objects.
- [var mutationsPtr: UnsafeMutablePointer<UInt>?](./nsfastenumerationstate/mutationsptr.md)
  Arbitrary state information used to detect whether the collection has been mutated.
- [var state: UInt](./nsfastenumerationstate/state.md)
  Arbitrary state information used by the iterator. Typically this is set to `0` at the beginning of the iteration.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfastenumerationstate)*