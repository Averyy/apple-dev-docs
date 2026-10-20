# init(title:message:dismissButton:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an alert with one button.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use a [`View`](../view.md) modifier like [`alert(_:isPresented:presenting:actions:message:)`](../view/alert%28_,ispresented,presenting,actions,message%29-8584l.md) instead.

## Declaration

```swift
init(title: Text, message: Text? = nil, dismissButton: Alert.Button? = nil)
```

## Parameters

- `title`: The title of the alert.
- `message`: The message to display in the body of the alert.
- `dismissButton`: The button that dismisses the alert.

## See Also

### Creating an alert
- [init(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button)](./init%28title,message,primarybutton,secondarybutton%29.md)
  Creates an alert with two buttons.
- [static func sideBySideButtons(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert](./sidebysidebuttons%28title,message,primarybutton,secondarybutton%29.md)
  Creates a side by side button alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/init(title:message:dismissbutton:))*