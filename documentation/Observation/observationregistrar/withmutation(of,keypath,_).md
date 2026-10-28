# withMutation(of:keyPath:_:)

**Framework**: Observation  
**Kind**: method  
**Role**: Instance Method

Identifies mutations to the transactions registered for observers.

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
func withMutation<Subject, Member, T>(of subject: Subject, keyPath: KeyPath<Subject, Member>, _ mutation: () throws -> T) rethrows -> T where Subject : Observable
```

## Discussion

This method calls [`willSet(_:keyPath:)`](./willset%28_,keypath%29.md) before the mutation. Then it calls [`didSet(_:keyPath:)`](./didset%28_,keypath%29.md) after the mutation.

## Parameters

- `subject`: An instance of an observable type.
- `keyPath`: The key path of an observed property.

## See Also

### Identifying transactional access
- [func access<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](./access%28_,keypath%29.md)
  Registers access to a specific property for observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observationregistrar/withmutation(of:keypath:_:))*