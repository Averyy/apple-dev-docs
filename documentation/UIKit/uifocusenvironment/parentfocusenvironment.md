# parentFocusEnvironment

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The parent focus environment for this environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
weak var parentFocusEnvironment: (any UIFocusEnvironment)? { get }
```

#### Discussion

The value of this property is `nil` when no parent container exists.

## See Also

- [var focusItemContainer: (any UIFocusItemContainer)?](uifocusenvironment/focusitemcontainer.md)
  The container for the child focus items in this focus environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/parentfocusenvironment)*