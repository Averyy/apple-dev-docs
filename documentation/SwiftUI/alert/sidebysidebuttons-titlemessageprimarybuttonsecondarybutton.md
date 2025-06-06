# sideBySideButtons(title:message:primaryButton:secondaryButton:)

**Framework**: SwiftUI  
**Kind**: method

Creates a side by side button alert.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
static func sideBySideButtons(title: Text, message: Text? = nil, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert
```

#### Discussion

The system determines the visual ordering of the buttons.

## Parameters

- `title`: The title of the alert.
- `message`: The message to display in the body of the alert.
- `primaryButton`: The first button to show in the alert.
- `secondaryButton`: The second button to show in the alert.

## See Also

- [init(title: Text, message: Text?, dismissButton: Alert.Button?)](alert/init(title:message:dismissbutton:).md)
  Creates an alert with one button.
- [init(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button)](alert/init(title:message:primarybutton:secondarybutton:).md)
  Creates an alert with two buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/sidebysidebuttons(title:message:primarybutton:secondarybutton:))*