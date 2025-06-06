# access(_:keyPath:)

**Framework**: Observation  
**Kind**: method

Registers access to a specific property for observation.

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
func access<Subject, Member>(_ subject: Subject, keyPath: KeyPath<Subject, Member>) where Subject : Observable
```

## Parameters

- `subject`: An instance of an observable type.
- `keyPath`: The key path of an observed property.

## See Also

- [func withMutation<Subject, Member, T>(of: Subject, keyPath: KeyPath<Subject, Member>, () throws -> T) rethrows -> T](observationregistrar/withmutation(of:keypath:_:).md)
  Identifies mutations to the transactions registered for observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observationregistrar/access(_:keypath:))*