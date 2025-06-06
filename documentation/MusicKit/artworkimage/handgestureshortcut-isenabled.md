# handGestureShortcut(_:isEnabled:)

**Framework**: MusicKit  
**Kind**: method

Assigns a hand gesture shortcut to the modified control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func handGestureShortcut(_ shortcut: HandGestureShortcut, isEnabled: Bool = true) -> some View
```

#### Discussion

Performing the control’s shortcut while the control is anywhere in the frontmost scene is equivalent to direct interaction with the control to perform its primary action.

The following example lets users of a watchOS music app toggle playback by double-tapping their thumb and index finger together:

```swift
struct PlaybackControls: View {
    let model: TrackModel

    var body: some View {
        HStack {
            Button("Skip Back") {
                model.skipBack()
            }

            Button("Play/Pause") {
                model.playPause()
            }
            .handGestureShortcut(.primaryAction)

            Button("Skip Forward") {
                model.skipForward()
            }
        }
    }
}
```

The target of a hand gesture shortcut is resolved in a leading-to-trailing traversal of the active scene.

## Parameters

- `shortcut`: The shortcut to associate with this control.
- `isEnabled`: A Boolean value that indicates whether the shortcut is   is enabled for this control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/handgestureshortcut(_:isenabled:))*