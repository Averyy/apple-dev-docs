# destructive(_:action:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates an alert button with a style that indicates a destructive action.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use View.alert(_:isPresented:presenting:actions:) instead.

## Declaration

```swift
static func destructive(_ label: Text, action: (() -> Void)? = {}) -> Alert.Button
```

## Return Value

An alert button that indicates a destructive action.

## Parameters

- `label`: The text to display on the button.
- `action`: A closure to execute when the user taps or presses the button.

## See Also

### Getting a button
- [static func `default`(Text, action: (() -> Void)?) -> Alert.Button](./default%28_,action%29.md)
  Creates an alert button with the default style.
- [static func cancel((() -> Void)?) -> Alert.Button](./cancel%28_%29.md)
  Creates an alert button that indicates cancellation, with a system-provided label.
- [static func cancel(Text, action: (() -> Void)?) -> Alert.Button](./cancel%28_,action%29.md)
  Creates an alert button that indicates cancellation, with a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/button/destructive(_:action:))*