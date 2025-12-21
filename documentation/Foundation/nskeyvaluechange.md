# NSKeyValueChange

**Framework**: Foundation  
**Kind**: enum

The kinds of changes that can be observed.

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
enum NSKeyValueChange
```

#### Overview

These constants are returned as the value for a [`kindKey`](nskeyvaluechangekey/kindkey.md) key in the change dictionary passed to [`observeValue(forKeyPath:of:change:context:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/observeValue(forKeyPath:of:change:context:)) indicating the type of change made.

## Topics

### Constants
- [NSKeyValueChange.setting](nskeyvaluechange/setting.md)
  Indicates that the value of the observed key path was set to a new value. This change can occur when observing an attribute of an object, as well as properties that specify to-one and to-many relationships.
- [NSKeyValueChange.insertion](nskeyvaluechange/insertion.md)
  Indicates that an object has been inserted into the to-many relationship that is being observed.
- [NSKeyValueChange.removal](nskeyvaluechange/removal.md)
  Indicates that an object has been removed from the to-many relationship that is being observed.
- [NSKeyValueChange.replacement](nskeyvaluechange/replacement.md)
  Indicates that an object has been replaced in the to-many relationship that is being observed.
### Initializers
- [init?(rawValue: UInt)](nskeyvaluechange/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NSGrammaticalCase](nsgrammaticalcase.md)
- [enum NSGrammaticalDefiniteness](nsgrammaticaldefiniteness.md)
- [enum NSGrammaticalDetermination](nsgrammaticaldetermination.md)
- [enum NSGrammaticalPerson](nsgrammaticalperson.md)
- [enum NSGrammaticalPronounType](nsgrammaticalpronountype.md)
- [struct NSKeyValueObservingOptions](nskeyvalueobservingoptions.md)
  The values that can be returned in a change dictionary.
- [enum NSKeyValueSetMutationKind](nskeyvaluesetmutationkind.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluechange)*