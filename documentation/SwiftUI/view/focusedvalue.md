# focusedValue(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the focused value for the given object type.

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
func focusedValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
```

## Mentions

- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)

#### Discussion

> ❗ **Important**: This initializer only accepts objects conforming to the `Observable` protocol. For reading environment objects that conform to `ObservableObject`, use `focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.

## Parameters

- `object`: The object to read the focus value for.

## See Also

- [func focusedValue(_:_:)](view/focusedvalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedSceneValue<T>(T?) -> some View](view/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue(_:_:)](view/focusedscenevalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [struct FocusedValues](focusedvalues.md)
  A collection of state exported by the focused scene or view and its ancestors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusedvalue(_:))*