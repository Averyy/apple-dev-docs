# focusItemContainer

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The container for the child focus items in this focus environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var focusItemContainer: (any UIFocusItemContainer)? { get }
```

#### Discussion

The value of this property is `nil` when no container exists.

## See Also

- [func contains(any UIFocusEnvironment) -> Bool](uifocusenvironment/contains(_:).md)
  Returns a Boolean value that indicates whether the focus environment contains the specified environment.
- [var parentFocusEnvironment: (any UIFocusEnvironment)?](uifocusenvironment/parentfocusenvironment.md)
  The parent focus environment for this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/focusitemcontainer)*