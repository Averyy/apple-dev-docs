# FocusedValues

**Framework**: SwiftUI  
**Kind**: struct

A collection of state exported by the focused view and its ancestors.

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
struct FocusedValues
```

## Topics

### Getting the value for a key
- [subscript<Key>(Key.Type) -> Key.Value?](focusedvalues/subscript(_:).md)
  Reads and writes values associated with a given focused value key.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [func focusedValue<T>(T?) -> some View](view/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue(_:_:)](view/focusedvalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedSceneValue<T>(T?) -> some View](view/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue(_:_:)](view/focusedscenevalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvalues)*