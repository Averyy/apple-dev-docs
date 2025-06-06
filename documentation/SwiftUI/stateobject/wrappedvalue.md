# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The underlying value referenced by the state object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency var wrappedValue: ObjectType { get }
```

#### Discussion

The wrapped value property provides primary access to the value’s data. However, you don’t typically access it directly. Instead, SwiftUI accesses this property for you when you refer to the variable that you create with the `@StateObject` attribute:

```swift
@StateObject private var contact = Contact()

var body: some View {
    Text(contact.name) // Reads name from contact's wrapped value.
}
```

When you change a wrapped value, you can access the new value immediately. However, SwiftUI updates views that display the value asynchronously, so the interface might not update immediately.

## See Also

- [var projectedValue: ObservedObject<ObjectType>.Wrapper](stateobject/projectedvalue.md)
  A projection of the state object that creates bindings to its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stateobject/wrappedvalue)*