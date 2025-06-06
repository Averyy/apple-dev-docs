# default(_:action:)

**Framework**: SwiftUI  
**Kind**: method

Creates an alert button with the default style.

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
static func `default`(_ label: Text, action: (() -> Void)? = {}) -> Alert.Button
```

#### Return Value

An alert button with the default style.

## Parameters

- `label`: The text to display on the button.
- `action`: A closure to execute when the user taps or presses the   button.

## See Also

- [static func cancel((() -> Void)?) -> Alert.Button](alert/button/cancel(_:).md)
  Creates an alert button that indicates cancellation, with a system-provided label.
- [static func cancel(Text, action: (() -> Void)?) -> Alert.Button](alert/button/cancel(_:action:).md)
  Creates an alert button that indicates cancellation, with a custom label.
- [static func destructive(Text, action: (() -> Void)?) -> Alert.Button](alert/button/destructive(_:action:).md)
  Creates an alert button with a style that indicates a destructive action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/button/default(_:action:))*