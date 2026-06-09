# init(initialValue:)

**Framework**: SwiftUI  
**Kind**: init

Creates a state property that stores an initial wrapped value.

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
init(initialValue thunk: @escaping () -> Value)
```

#### Discussion

You don’t call this initializer directly. Instead, SwiftUI calls it for you when you declare a property with the `@State` attribute and provide an initial value:

```swift
struct MyView: View {
    @State private var isPlaying: Bool = false

    // ...
}
```

SwiftUI initializes the state’s storage only once for each container instance that you declare. In the above code, SwiftUI creates `isPlaying` only the first time it initializes a particular instance of `MyView`. On the other hand, each instance of `MyView` creates a distinct instance of the state. For example, each of the views in the following [`VStack`](vstack.md) has its own `isPlaying` value:

```swift
var body: some View {
    VStack {
        MyView()
        MyView()
    }
}
```

## See Also

- [init()](lazystate/init.md)
  Creates a state property without an initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazystate/init(initialvalue:))*