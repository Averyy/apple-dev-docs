# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The underlying value that the observed object references.

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
@preconcurrency var wrappedValue: ObjectType
```

#### Discussion

The wrapped value property provides primary access to the observed object’s data. However, you don’t typically access it by name. Instead, SwiftUI accesses this property for you when you refer to the variable that you create with the `@ObservedObject` attribute.

```swift
struct MySubView: View {
    @ObservedObject var model: DataModel

    var body: some View {
        Text(model.name) // Reads name from model's wrapped value.
    }
}
```

When you change a wrapped value, you can access the new value immediately. However, SwiftUI updates views that display the value asynchronously, so the interface might not update immediately.

## See Also

- [var projectedValue: ObservedObject<ObjectType>.Wrapper](observedobject/projectedvalue.md)
  A projection of the observed object that creates bindings to its properties.
- [ObservedObject.Wrapper](observedobject/wrapper.md)
  A wrapper of the underlying observable object that can create bindings to its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/observedobject/wrappedvalue)*