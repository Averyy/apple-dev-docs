# SettingsLink

**Framework**: SwiftUI  
**Kind**: struct

A view that opens the Settings scene defined by an app.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct SettingsLink<Label> where Label : View
```

#### Overview

On macOS, clicking on the link opens the window for the scene or orders it to the front if it is already open.

## Topics

### Creating a settings link
- [init()](settingslink/init.md)
  Creates a settings link with the default system label.
- [init(label: () -> Label)](settingslink/init(label:).md)
  Creates a settings link with a custom label.
### Supporting types
- [struct DefaultSettingsLinkLabel](defaultsettingslinklabel.md)
  The default label to use for a settings link.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct Settings](settings.md)
  A scene that presents an interface for viewing and modifying an app’s settings.
- [struct OpenSettingsAction](opensettingsaction.md)
  An action that presents the settings scene for an app.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/settingslink)*