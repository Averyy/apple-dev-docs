# environmentObject(_:)

**Framework**: App Intents  
**Kind**: method

Supplies an observable object to a view’s hierarchy.

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
nonisolated
func environmentObject<T>(_ object: T) -> some View where T : ObservableObject
```

#### Discussion

Use this modifier to add an observable object to a view’s environment. The object must conform to the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol.

Adding an object to a view’s environment makes the object available to subviews in the view’s hierarchy. To retrieve the object in a subview, use the `EnvironmentObject` property wrapper.

> **Note**: If the observable object conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol, use either `View/environment(_:)` or the `View/environment(_:_:)` modifier to add the object to the view’s environment.

If the observable object conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol, use either `View/environment(_:)` or the `View/environment(_:_:)` modifier to add the object to the view’s environment.

## Parameters

- `object`: The object to store and make available to   the view’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/environmentobject(_:))*