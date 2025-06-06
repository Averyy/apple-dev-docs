# init(title:message:primaryButton:secondaryButton:)

**Framework**: SwiftUI  
**Kind**: init

Creates an alert with two buttons.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(title: Text, message: Text? = nil, primaryButton: Alert.Button, secondaryButton: Alert.Button)
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
- [static func sideBySideButtons(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert](alert/sidebysidebuttons(title:message:primarybutton:secondarybutton:).md)
  Creates a side by side button alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/init(title:message:primarybutton:secondarybutton:))*