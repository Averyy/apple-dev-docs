# preferredFocusEnvironments

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

An array of focus environments, ordered by priority, to which this environment prefers focus to be directed during a focus update.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredFocusEnvironments: [any UIFocusEnvironment] { get }
```

#### Discussion

The preferred focus environments listed in this property define where to search for the default focused item in an environment, such as when focus updates programmatically. Starting from the target environment, each preferred focus environment is recursively searched in the order it appears in the array until an eligible, focusable item is found. Preferred focus environments can include focusable and nonfocusable items, in addition to nonitem environments. Returning an empty array is equivalent to returning an array containing only `self`.

## See Also

- [var preferredFocusedView: UIView?](uifocusenvironment/preferredfocusedview.md)
  Specifies the view that should be focused if this environment is focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/preferredfocusenvironments)*