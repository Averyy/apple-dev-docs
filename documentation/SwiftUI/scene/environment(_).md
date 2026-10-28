# environment(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Places an observable object in the scene’s environment.

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
nonisolated
func environment<T>(_ object: T?) -> some Scene where T : AnyObject, T : Observable
```

## Return Value

A scene that has the specified object in its environment.

## Discussion

Use this modifier to place an object that you declare with the [`Observable()`](../../Observation/observable%28%29.md) macro into a scene’s environment. For example, you can add an instance of a custom observable `Profile` class to the environment of a [`WindowGroup`](../windowgroup.md) scene:

```swift
@Observable class Profile { ... }

@main
struct MyApp: App {
    var body: some View {
        WindowGroup {
            ContentView()
        }
        .environment(Profile.currentProfile)
    }
}
```

You then read the object inside `ContentView` or one of its descendants using the [`Environment`](../environment.md) property wrapper:

```swift
struct ContentView: View {
    @Environment(Profile.self) private var currentProfile: Profile

    var body: some View { ... }
}
```

This modifier affects the given scene, as well as the scene’s descendant views. It has no effect outside the view hierarchy on which you call it. The environment of a given view hierarchy holds only one observable object of a given type.

> **Note**: This modifier takes an object that conforms to the [`Observable`](../../Observation/observable.md) protocol. To add environment objects that conform to the [`ObservableObject`](../../Combine/observableobject.md) protocol, use [`environmentObject(_:)`](./environmentobject%28_%29.md) instead.

## Parameters

- `object`: The object to set for this object’s type in the environment, or `nil` to clear an object of this type from the environment.

## See Also

### Modifying the environment of a scene
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene](./environment%28_,_%29.md)
  Sets the environment value of the specified key path to the given value.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some Scene](./transformenvironment%28_,transform%29.md)
  Transforms the environment value of the specified key path with the given function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/environment(_:))*