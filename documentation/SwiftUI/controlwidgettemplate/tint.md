# tint(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the tint color within this control widget template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func tint(_ tint: Color?) -> some ControlWidgetTemplate
```

#### Discussion

Controls do not respect the [`tint(_:)`](view/tint(_:).md) modifier when applied to control labels, nor do controls support arbitrary tint shape styles. Instead, define a tint color for your control by applying this modifier to its template:

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
            .tint(.orange)
        }
    }
}
```

## Parameters

- `tint`: The tint   to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgettemplate/tint(_:))*