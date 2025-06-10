# ObservationRegistrar

**Framework**: Observation  
**Kind**: struct

Provides storage for tracking and access to data changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct ObservationRegistrar
```

#### Overview

You don’t need to create an instance of `ObservationRegistrar` when using the [`Observable()`](observable().md) macro to indicate observability of a type.

## Topics

### Creating an observation registrar
- [init()](observationregistrar/init.md)
  Creates an instance of the observation registrar.
### Receiving change notifications
- [func willSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](observationregistrar/willset(_:keypath:).md)
  A property observation called before setting the value of the subject.
- [func didSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](observationregistrar/didset(_:keypath:).md)
  A property observation called after setting the value of the subject.
### Identifying transactional access
- [func access<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](observationregistrar/access(_:keypath:).md)
  Registers access to a specific property for observation.
- [func withMutation<Subject, Member, T>(of: Subject, keyPath: KeyPath<Subject, Member>, () throws -> T) rethrows -> T](observationregistrar/withmutation(of:keypath:_:).md)
  Identifies mutations to the transactions registered for observers.
### Default Implementations
- [Decodable Implementations](observationregistrar/decodable-implementations.md)
- [Encodable Implementations](observationregistrar/encodable-implementations.md)
- [Equatable Implementations](observationregistrar/equatable-implementations.md)
- [Hashable Implementations](observationregistrar/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func withObservationTracking<T>(() -> T, onChange: @autoclosure () -> () -> Void) -> T](withobservationtracking(_:onchange:).md)
  Tracks access to properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observationregistrar)*