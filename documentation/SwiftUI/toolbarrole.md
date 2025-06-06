# ToolbarRole

**Framework**: SwiftUI  
**Kind**: struct

The purpose of content that populates the toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ToolbarRole
```

#### Overview

A toolbar role provides a description of the purpose of content that populates the toolbar. The purpose of the content influences how a toolbar renders its content. For example, a [`browser`](toolbarrole/browser.md) will automatically leading align the title of a toolbar in iPadOS.

Provide this type to the [`toolbarRole(_:)`](view/toolbarrole(_:).md) modifier:

```swift
ContentView()
    .navigationTitle("Browser")
    .toolbarRole(.browser)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            AddButton()
        }
     }
```

## Topics

### Behavior-specific roles
- [static var browser: ToolbarRole](toolbarrole/browser.md)
  The browser role.
- [static var editor: ToolbarRole](toolbarrole/editor.md)
  The editor role.
- [static var navigationStack: ToolbarRole](toolbarrole/navigationstack.md)
  The navigationStack role.
### Automatic roles
- [static var automatic: ToolbarRole](toolbarrole/automatic.md)
  The automatic role.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func toolbarRole(ToolbarRole) -> some View](view/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarrole)*