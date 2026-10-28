# ActionSheet.Button

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

A button representing an operation of an action sheet presentation.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use a [`View`](../view.md) modifier like [`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`](../view/confirmationdialog%28_,ispresented,titlevisibility,presenting,actions,message%29-8y541.md) instead.

## Declaration

```swift
typealias Button = Alert.Button
```

## Discussion

The [`ActionSheet`](../actionsheet.md) button is type-aliased to the [`Alert`](../alert.md) button type, which provides default, cancel, and destructive styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/actionsheet/button)*