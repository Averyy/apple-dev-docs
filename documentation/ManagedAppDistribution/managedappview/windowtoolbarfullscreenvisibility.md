# windowToolbarFullScreenVisibility(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Configures the visibility of the window toolbar when the window enters full screen mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func windowToolbarFullScreenVisibility(_ visibility: WindowToolbarFullScreenVisibility) -> some View
```

#### Discussion

By default, the window toolbar will show at the top of the display, above the window’s contents.

You can use this modifier to override the default behavior.

For example, you can specify that the window toolbar should be hidden by default, and only show once the mouse moves into the area occupied by the menu bar:

```None
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ...
            }
            .windowToolbarFullScreenVisibility(.onHover)
    }
}
```

## Parameters

- `visibility`: The visibility to use for the window toolbar in   full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/windowtoolbarfullscreenvisibility(_:))*