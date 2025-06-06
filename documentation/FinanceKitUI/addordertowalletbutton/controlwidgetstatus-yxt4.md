# controlWidgetStatus(_:)

**Framework**: FinanceKitUI  
**Kind**: method

The status of the control described by the modified label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func controlWidgetStatus(_ statusKey: LocalizedStringKey) -> some View
```

#### Discussion

This text will appear in Control Center when your control’s state changes. You can customize the text by applying this modifier to the control’s value label:

```None
// Status Text: "Do Not Disturb Until This Evening" / "Do Not Disturb Disabled"
ControlWidgetToggle("Do Not Disturb", ...) { isOn in
    Image(systemName: "moon")
        .controlWidgetStatus(isOn ? "Do Not Disturb Until This Evening" : "Do Not Disturb Disabled")
}
```

## Parameters

- `statusKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/controlwidgetstatus(_:)-yxt4)*