# onScrollVisibilityChange(threshold:_:)

**Framework**: PermissionKit  
**Kind**: method

Adds an action to be called when the view crosses the threshold to be considered on/off screen.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func onScrollVisibilityChange(threshold: Double = 0.5, _ action: @escaping (Bool) -> Void) -> some View
```

#### Discussion

Use this modifier to be informed when the view has crossed the provided threshold to be considered on/off screen.

```None
struct VideoPlayer: View {
    @State var playing: Bool

    var body: some View {
        Group {
            // ...
        }
        .onScrollVisibilityChange(threshold: 0.2) { isVisible in
            playing = isVisible
        }
    }
}
```

When the view appears on-screen, the action will be called if the threshold has already been reached.

## Parameters

- `threshold`: The amount required to be visible within the viewport of the the parent   view before the   is fired. By default when the view has crossed more than 50%   on-screen, the action will be called.
- `action`: The action which will be called when the threshold has been reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/onscrollvisibilitychange(threshold:_:))*