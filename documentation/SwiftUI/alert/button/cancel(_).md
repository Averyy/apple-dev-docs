# cancel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates an alert button that indicates cancellation, with a system-provided label.

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
static func cancel(_ action: (() -> Void)? = {}) -> Alert.Button
```

## Return Value

An alert button that indicates cancellation.

## Discussion

The system automatically chooses locale-appropriate text for the button’s label.

## Parameters

- `action`: A closure to execute when the user taps or presses the button.

## See Also

### Getting a button
- [static func `default`(Text, action: (() -> Void)?) -> Alert.Button](./default%28_,action%29.md)
  Creates an alert button with the default style.
- [static func cancel(Text, action: (() -> Void)?) -> Alert.Button](./cancel%28_,action%29.md)
  Creates an alert button that indicates cancellation, with a custom label.
- [static func destructive(Text, action: (() -> Void)?) -> Alert.Button](./destructive%28_,action%29.md)
  Creates an alert button with a style that indicates a destructive action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/button/cancel(_:))*