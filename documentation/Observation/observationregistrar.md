# ObservationRegistrar

**Framework**: Observation  
**Kind**: struct  
**Role**: Structure

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

You don’t need to create an instance of `ObservationRegistrar` when using the [`Observable()`](./observable%28%29.md) macro to indicate observability of a type.

## Topics

### Creating an observation registrar
- [init()](./observationregistrar/init%28%29.md)
  Creates an instance of the observation registrar.
### Receiving change notifications
- [func willSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](./observationregistrar/willset%28_,keypath%29.md)
  A property observation called before setting the value of the subject.
- [func didSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](./observationregistrar/didset%28_,keypath%29.md)
  A property observation called after setting the value of the subject.
### Identifying transactional access
- [func access<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](./observationregistrar/access%28_,keypath%29.md)
  Registers access to a specific property for observation.
- [func withMutation<Subject, Member, T>(of: Subject, keyPath: KeyPath<Subject, Member>, () throws -> T) rethrows -> T](./observationregistrar/withmutation%28of,keypath,_%29.md)
  Identifies mutations to the transactions registered for observers.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Change tracking
- [func withObservationTracking<T>(() -> T, onChange: @autoclosure () -> () -> Void) -> T](./withobservationtracking%28_,onchange%29.md)
  Tracks access to properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observationregistrar)*