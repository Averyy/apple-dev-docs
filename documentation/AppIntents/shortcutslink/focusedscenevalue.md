# focusedSceneValue(_:)

**Framework**: App Intents  
**Kind**: method

Sets the focused value for the given object type at a scene-wide scope.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func focusedSceneValue<T>(_ object: T?) -> some View where T : AnyObject, T : Observable
```

#### Discussion

> ❗ **Important**: This initializer only accepts objects conforming to the `Observable` protocol. For reading environment objects that conform to `ObservableObject`, use `focusedObject(_:)`, instead.

To read this value, use the `FocusedValue` property wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/focusedscenevalue(_:))*