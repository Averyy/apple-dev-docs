# EnvironmentObject.Wrapper

**Framework**: SwiftUI  
**Kind**: struct

A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@dynamicMemberLookup @frozen @preconcurrency struct Wrapper
```

## Topics

### Getting a binding value
- [subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<ObjectType, Subject>) -> Binding<Subject>](environmentobject/wrapper/subscript(dynamicmember:).md)
  Returns a binding to the resulting value of a given key path.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var wrappedValue: ObjectType](environmentobject/wrappedvalue.md)
  The underlying value referenced by the environment object.
- [var projectedValue: EnvironmentObject<ObjectType>.Wrapper](environmentobject/projectedvalue.md)
  A projection of the environment object that creates bindings to its properties using dynamic member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentobject/wrapper)*