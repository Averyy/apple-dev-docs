# init(title:message:buttons:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an action sheet with the provided buttons.

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
init(title: Text, message: Text? = nil, buttons: [ActionSheet.Button] = [.cancel()])
```

## Parameters

- `title`: The title of the action sheet.
- `message`: The message to display in the body of the action sheet.
- `buttons`: The buttons to show in the action sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/actionsheet/init(title:message:buttons:))*