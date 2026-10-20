# ObservedObject.Wrapper

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A wrapper of the underlying observable object that can create bindings to its properties.

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
@dynamicMemberLookup @preconcurrency @frozen struct Wrapper
```

## Topics

### Subscripts
- [subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<ObjectType, Subject>) -> Binding<Subject>](./wrapper/subscript%28dynamicmember%29.md)
  Gets a binding to the value of a specified key path.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the value
- [var wrappedValue: ObjectType](./wrappedvalue.md)
  The underlying value that the observed object references.
- [var projectedValue: ObservedObject<ObjectType>.Wrapper](./projectedvalue.md)
  A projection of the observed object that creates bindings to its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/observedobject/wrapper)*