# Alert.Button

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A button that represents an operation of an alert presentation.

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
struct Button
```

## Topics

### Getting a button
- [static func `default`(Text, action: (() -> Void)?) -> Alert.Button](./button/default%28_,action%29.md)
  Creates an alert button with the default style.
- [static func cancel((() -> Void)?) -> Alert.Button](./button/cancel%28_%29.md)
  Creates an alert button that indicates cancellation, with a system-provided label.
- [static func cancel(Text, action: (() -> Void)?) -> Alert.Button](./button/cancel%28_,action%29.md)
  Creates an alert button that indicates cancellation, with a custom label.
- [static func destructive(Text, action: (() -> Void)?) -> Alert.Button](./button/destructive%28_,action%29.md)
  Creates an alert button with a style that indicates a destructive action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/button)*