# didSet(_:keyPath:)

**Framework**: Observation  
**Kind**: method

A property observation called after setting the value of the subject.

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
func didSet<Subject, Member>(_ subject: Subject, keyPath: KeyPath<Subject, Member>) where Subject : Observable
```

## Parameters

- `subject`: An instance of an observable type.
- `keyPath`: The key path of an observed property.

## See Also

- [func willSet<Subject, Member>(Subject, keyPath: KeyPath<Subject, Member>)](observationregistrar/willset(_:keypath:).md)
  A property observation called before setting the value of the subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observationregistrar/didset(_:keypath:))*