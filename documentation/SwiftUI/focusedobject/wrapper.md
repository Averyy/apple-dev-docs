# FocusedObject.Wrapper

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency @dynamicMemberLookup @frozen struct Wrapper
```

## Topics

### Accessing members
- [subscript<T>(dynamicMember _: ReferenceWritableKeyPath<ObjectType, T>) -> Binding<T>](./wrapper/subscript%28dynamicmember%29.md)
  Returns a binding to the value of a given key path.

## See Also

### Getting the value
- [var projectedValue: FocusedObject<ObjectType>.Wrapper?](./projectedvalue.md)
  A projection of the focused object that creates bindings to its properties using dynamic member lookup.
- [var wrappedValue: ObjectType?](./wrappedvalue.md)
  The underlying value referenced by the focused object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedobject/wrapper)*