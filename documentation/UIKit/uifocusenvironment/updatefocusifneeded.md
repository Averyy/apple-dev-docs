# updateFocusIfNeeded()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the focus engine to force a focus update immediately.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateFocusIfNeeded()
```

#### Discussion

If any focus environment is currently pending an update (after calling [`setNeedsFocusUpdate()`](uifocusenvironment/setneedsfocusupdate().md)), then calling this method forces the focus engine to immediately update focus. Unlike [`setNeedsFocusUpdate()`](uifocusenvironment/setneedsfocusupdate().md), it does not matter if this environment currently contains focus, or if this environment is the one pending an update.

## See Also

- [func setNeedsFocusUpdate()](uifocusenvironment/setneedsfocusupdate.md)
  Submits a request to the focus engine for a focus update in this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/updatefocusifneeded())*