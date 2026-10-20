# NSCompoundPredicate.LogicalType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the possible types of a compound predicate.

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
enum LogicalType
```

```c
enum NSCompoundPredicateType : NSUInteger;
```

## Topics

### Constants
- [NSCompoundPredicate.LogicalType.not](./logicaltype/not.md)
  A logical NOT predicate.
- [NSCompoundPredicate.LogicalType.and](./logicaltype/and.md)
  A logical AND predicate.
- [NSCompoundPredicate.LogicalType.or](./logicaltype/or.md)
  A logical OR predicate.
### Initializers
- [init?(rawValue: UInt)](./logicaltype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Information About a Compound Predicate
- [var compoundPredicateType: NSCompoundPredicate.LogicalType](./compoundpredicatetype.md)
  The predicate type for the receiver.
- [var subpredicates: [Any]](./subpredicates.md)
  The receiver’s subpredicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscompoundpredicate/logicaltype)*