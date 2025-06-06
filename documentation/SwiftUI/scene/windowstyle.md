# windowStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for windows created by this scene.

**Availability**:
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func windowStyle<S>(_ style: S) -> some Scene where S : WindowStyle
```

## See Also

- [struct WindowGroup](windowgroup.md)
  A scene that presents a group of identically structured windows.
- [struct Window](window.md)
  A scene that presents its content in a single, unique window.
- [struct UtilityWindow](utilitywindow.md)
  A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [protocol WindowStyle](windowstyle.md)
  A specification for the appearance and interaction of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowstyle(_:))*