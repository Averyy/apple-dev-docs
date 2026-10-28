# sideBySideButtons(title:message:primaryButton:secondaryButton:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a side by side button alert.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use a [`View`](../view.md) modifier like [`alert(_:isPresented:presenting:actions:message:)`](../view/alert%28_,ispresented,presenting,actions,message%29-8584l.md) instead.

## Declaration

```swift
static func sideBySideButtons(title: Text, message: Text? = nil, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert
```

## Discussion

The system determines the visual ordering of the buttons.

## Parameters

- `title`: The title of the alert.
- `message`: The message to display in the body of the alert.
- `primaryButton`: The first button to show in the alert.
- `secondaryButton`: The second button to show in the alert.

## See Also

### Creating an alert
- [init(title: Text, message: Text?, dismissButton: Alert.Button?)](./init%28title,message,dismissbutton%29.md)
  Creates an alert with one button.
- [init(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button)](./init%28title,message,primarybutton,secondarybutton%29.md)
  Creates an alert with two buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/sidebysidebuttons(title:message:primarybutton:secondarybutton:))*