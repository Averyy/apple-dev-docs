# Alert.Button

**Framework**: SwiftUI  
**Kind**: struct

A button that represents an operation of an alert presentation.

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
struct Button
```

## Topics

### Getting a button
- [static func `default`(Text, action: (() -> Void)?) -> Alert.Button](alert/button/default(_:action:).md)
  Creates an alert button with the default style.
- [static func cancel((() -> Void)?) -> Alert.Button](alert/button/cancel(_:).md)
  Creates an alert button that indicates cancellation, with a system-provided label.
- [static func cancel(Text, action: (() -> Void)?) -> Alert.Button](alert/button/cancel(_:action:).md)
  Creates an alert button that indicates cancellation, with a custom label.
- [static func destructive(Text, action: (() -> Void)?) -> Alert.Button](alert/button/destructive(_:action:).md)
  Creates an alert button with a style that indicates a destructive action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert/button)*