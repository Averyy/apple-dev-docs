# dialogIcon(_:)

**Framework**: FamilyControls  
**Kind**: method

Configures the icon used by dialogs within this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 13.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func dialogIcon(_ icon: Image?) -> some View
```

#### Discussion

On macOS, this icon replaces the default icon of the app.

On watchOS, this icon will be shown in any dialogs presented.

This modifier has no effect on other platforms.

The following example configures a `confirmationDialog` with a custom image.

```swift
Button("Delete items") {
    isShowingDialog = true
}
.confirmationDialog(
    "Are you sure you want to erase these items?",
        isPresented: $isShowingDialog
) {
    Button("Erase", role: .destructive) {
        // Handle item deletion.
    }
    Button("Cancel", role: .cancel) {
        isShowingDialog = false
    }
}
.dialogIcon(Image(...))
```

## Parameters

- `icon`: The custom icon to use for confirmation dialogs and alerts.   Passing   will use the default app icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/dialogicon(_:))*