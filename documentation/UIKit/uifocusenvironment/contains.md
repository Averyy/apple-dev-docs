# contains(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether the focus environment contains the specified environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func contains(_ environment: any UIFocusEnvironment) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `environment` is contained by the current focus environment or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

## Parameters

- `environment`: The focus environment to check.

## See Also

- [var parentFocusEnvironment: (any UIFocusEnvironment)?](uifocusenvironment/parentfocusenvironment.md)
  The parent focus environment for this environment.
- [var focusItemContainer: (any UIFocusItemContainer)?](uifocusenvironment/focusitemcontainer.md)
  The container for the child focus items in this focus environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/contains(_:))*