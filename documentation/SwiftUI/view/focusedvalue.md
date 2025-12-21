# focusedValue(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.

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
nonisolated
func focusedValue<Value>(_ keyPath: WritableKeyPath<FocusedValues, Value?>, _ value: Value) -> some View
```

#### Return Value

A modified representation of this view.

## Parameters

- `keyPath`: The key path to associate   with when adding   it to the existing table of exported focus values.
- `value`: The focus value to export.

## See Also

- [func focusedValue<T>(T?) -> some View](view/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedSceneValue<T>(T?) -> some View](view/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue(_:_:)](view/focusedscenevalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [struct FocusedValues](focusedvalues.md)
  A collection of state exported by the focused scene or view and its ancestors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusedvalue(_:_:))*