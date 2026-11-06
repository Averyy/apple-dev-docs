# directTouchSystemGesturesDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Disables direct-touch system gestures.

**Availability**:
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func directTouchSystemGesturesDisabled(_ prefersDisabled: Bool = true) -> some View
```

## Discussion

On a Mac display that accepts direct touch, such as an iPad running Sidecar, multi-touch system gestures can take precedence over gestures in your app. Use this modifier when your app recognizes several simultaneous touches that the system would otherwise consume.

The following mixer shows a row of faders, each of which a person can drag at the same time. Three simultaneous drags would otherwise begin a system gesture, so the mixer disables system gestures that require three or more touches:

```swift
struct MixerView: View {
    @Binding var channels: [Channel]

    var body: some View {
        HStack {
            ForEach($channels) { $channel in
                FaderView(level: $channel.level)
            }
        }
        .directTouchSystemGesturesDisabled()
    }
}
```

Pass `false` to allow system gestures again, such as while your app presents UI that doesn’t require multi-touch gestures:

```swift
.directTouchSystemGesturesDisabled(false)
```

Although you apply this modifier to a view, it affects the window that contains the view: if any view in a window disables system gestures, they’re disabled throughout that window. A descendant can’t allow system gestures that an ancestor disables or vice versa.

This modifier has no effect on indirect gestures, such as those a person performs on a trackpad.

> **Note**: You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

## Parameters

- `prefersDisabled`: A Boolean value that indicates whether to disable multitouch system gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/directtouchsystemgesturesdisabled(_:))*