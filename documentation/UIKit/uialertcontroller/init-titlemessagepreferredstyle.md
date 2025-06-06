# init(title:message:preferredStyle:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a view controller for displaying an alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(title: String?, message: String?, preferredStyle: UIAlertController.Style)
```

#### Return Value

An initialized alert controller object.

#### Discussion

After creating the alert controller, configure any actions that you want people to be able to perform by calling the [`addAction(_:)`](uialertcontroller/addaction(_:).md) method one or more times. When specifying a preferred style of [`UIAlertController.Style.alert`](uialertcontroller/style/alert.md), you may also configure one or more text fields to display in addition to the actions.

## Parameters

- `title`: The title of the alert. Use this string to get people’s attention and communicate the reason for the alert.
- `message`: Descriptive text that provides additional details about the reason for the alert.
- `preferredStyle`: The style to use when presenting the alert controller. Use this parameter to configure the alert controller as an action sheet or as a modal alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/init(title:message:preferredstyle:))*