# focusable(_:interactions:)

**Framework**: Familycontrols  
**Kind**: method

Specifies if the view is focusable, and if so, what focus-driven interactions it supports.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func focusable(_ isFocusable: Bool = true, interactions: FocusInteractions) -> some View
```

#### Return Value

A view that sets whether its child is focusable.

#### Discussion

By default, SwiftUI enables all possible focus interactions. However, on macOS and iOS it is conventional for button-like views to only accept focus when the user has enabled keyboard navigation system-wide in the Settings app. Clients can reproduce this behavior with custom views by only supporting `.activate` interactions.

```swift
MyTapGestureView(...)
    .focusable(interactions: .activate)
```

> **Note**: The focus interactions allowed for custom views changed in macOS 14—previously, custom views could only become focused with keyboard navigation enabled system-wide. Clients built using older SDKs will continue to see the older focus behavior, while custom views in clients built using macOS 14 or later will always be focusable unless the client requests otherwise by specifying a restricted set of focus interactions.

## Parameters

- `isFocusable`:   if the view should participate in focus;    otherwise. The default value is  .
- `interactions`: The types of focus interactions supported by the view.   The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/focusable(_:interactions:))*