# privacySensitive(_:)

**Framework**: SwiftUI  
**Kind**: method

Marks the control template as containing sensitive, private user data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func privacySensitive(_ sensitive: Bool = true) -> some ControlWidgetTemplate
```

#### Discussion

The system redacts controls marked with this modifier when those controls are displayed on the Lock Screen and the device is locked.

Controls also respect the [`privacySensitive(_:)`](view/privacysensitive(_:).md) modifier applied to the control’s label. That modifier only redacts the control content, however. To redact the content  the state of the control, apply this modifier to the control template:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(...) {
            ControlWidgetToggle(...) {
                Label(
                    $0 ? "Open" : "Closed",
                    systemImage: $0 ? "door.open" : "door.closed"
                )
            }
            .privacySensitive()
        }
    }
}
```

## Parameters

- `sensitive`: A Boolean value that determines whether this   control is sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgettemplate/privacysensitive(_:))*