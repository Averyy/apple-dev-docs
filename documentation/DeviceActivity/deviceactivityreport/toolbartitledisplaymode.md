# toolbarTitleDisplayMode(_:)

**Framework**: DeviceActivity  
**Kind**: method

Configures the toolbar title display mode for this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func toolbarTitleDisplayMode(_ mode: ToolbarTitleDisplayMode) -> some View
```

#### Discussion

Use this modifier to override the default toolbar title display mode.

```swift
NavigationStack {
    ContentView()
        .toolbarTitleDisplayMode(.inlineLarge)
}
```

See `ToolbarTitleDisplayMode` for more information on the different kinds of display modes. This modifier has no effect on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/toolbartitledisplaymode(_:))*