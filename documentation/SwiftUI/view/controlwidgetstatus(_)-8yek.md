# controlWidgetStatus(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The status of the control described by the modified label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func controlWidgetStatus<S>(_ status: S) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func controlWidgetStatus(_ status: LocalizedStringResource) -> some View
```

```swift
@MainActor
@preconcurrency func controlWidgetStatus(_ status: Text) -> some View
```

```swift
@MainActor
@preconcurrency func controlWidgetStatus(_ statusKey: LocalizedStringKey) -> some View
```

## Discussion

This text appears in Control Center when your control’s state changes. You can customize the text by applying this modifier to the control’s value label:

```swift
// Status Text: "Do Not Disturb Until This Evening" / "Do Not Disturb Disabled"
ControlWidgetToggle("Do Not Disturb", ...) { isOn in
    Image(systemName: "moon")
        .controlWidgetStatus(isOn ? "Do Not Disturb Until This Evening" : "Do Not Disturb Disabled")
}
```

## Parameters

- `status`: The status to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/controlwidgetstatus(_:)-8yek)*