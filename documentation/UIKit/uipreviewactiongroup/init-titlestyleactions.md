# init(title:style:actions:)

**Framework**: UIKit  
**Kind**: init

Creates a peek quick action group using a specified title, style, and array of peek quick actions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
convenience init(title: String, style: UIPreviewAction.Style, actions: [UIPreviewAction])
```

#### Return Value

A newly initialized peek quick action group with your specified title, style, and submenu of peek quick actions.

## Parameters

- `title`: The peek quick action group’s title
- `style`: When the system presents the group’s submenu, each child quick action is displayed using its own style. The available styles are described in the UIPreviewActionStyle enumeration in  .
- `actions`: An array of   objects, displayed as the child quick actions for the peek quick action group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewactiongroup/init(title:style:actions:))*