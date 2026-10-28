# controlWidgetActionHint(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The action hint of the control described by the modified label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func controlWidgetActionHint(_ hint: Text) -> some View
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func controlWidgetActionHint(_ hint: LocalizedStringResource) -> some View
```

```swift
@MainActor
@preconcurrency func controlWidgetActionHint(_ hintKey: LocalizedStringKey) -> some View
```

```swift
@MainActor
@preconcurrency func controlWidgetActionHint<S>(_ hint: S) -> some View where S : StringProtocol
```

## Discussion

This text appears next to the Action Button to describe what your control does when activated. By default, a control’s action hint is derived from its display name, the type of control, and value text, if any:

// Action Hint: “Hold for ‘Ping My Watch’” struct PingMyWatchButton: Control { static let displayName: LocalizedStringResource = “Ping My Watch” … }

// When this button’s action conforms to `OpenIntent`: // Action Hint: “Hold to Open Notes” struct NotesLauncher: Control { static let displayName: LocalizedStringResource = “Notes” … }

// Action Hint: “Hold to Turn On ‘Silent Mode’” / “Hold to Turn Off ‘Silent Mode’” struct SilentModeToggle: Control { static let displayName: LocalizedStringResource = “Silent Mode” … }

// Action Hint: “Hold for Silent” / “Hold for Ring” ControlWidgetToggle(…) { isOn in Label( isOn ? “Silent” : “Ring”, systemImage: isOn ? “bell.slash” : “bell” ) }

When the default action hint is insufficiently descriptive, you can customize the hint by applying this modifier to the control’s label. For instance, describe what a person uses a `NotesLauncher` control to do, “Compose a Note”, instead of the default “Hold to Open Notes” hint, like this:

ControlWidgetButton(…) { Image(systemName: “note.text”) .controlWidgetActionHint(“Compose a Note”) }

## Parameters

- `hint`: The hint to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/controlwidgetactionhint(_:)-5yoyh)*