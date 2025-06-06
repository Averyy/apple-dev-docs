# init(wrappedValue:)

**Framework**: SwiftUI  
**Kind**: init

Creates an observed object with an initial wrapped value.

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
@preconcurrency init(wrappedValue: ObjectType)
```

#### Discussion

Don’t call this initializer directly. Instead, declare an input to a view with the `@ObservedObject` attribute, and pass a value to this input when you instantiate the view. Unlike a [`StateObject`](stateobject.md) which manages data storage, you use an observed object to refer to storage that you manage elsewhere, as in the following example:

```swift
class DataModel: ObservableObject {
    @Published var name = "Some Name"
    @Published var isEnabled = false
}

struct MyView: View {
    @StateObject private var model = DataModel()

    var body: some View {
        Text(model.name)
        MySubView(model: model)
    }
}

struct MySubView: View {
    @ObservedObject var model: DataModel

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

Explicitly calling the observed object initializer in `MySubView` would behave correctly, but would needlessly recreate the same observed object instance every time SwiftUI calls the view’s initializer to redraw the view.

## Parameters

- `wrappedValue`: An initial value for the observable object.

## See Also

- [init(initialValue: ObjectType)](observedobject/init(initialvalue:).md)
  Creates an observed object with an initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/observedobject/init(wrappedvalue:))*