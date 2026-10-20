# updateFocusIfNeeded()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
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
func updateFocusIfNeeded()
```

```objc
- (void) updateFocusIfNeeded;
```

#### Discussion

If any focus environment is currently pending an update (after calling [`setNeedsFocusUpdate()`](./setneedsfocusupdate%28%29.md)), then calling this method forces the focus engine to immediately update focus. Unlike [`setNeedsFocusUpdate()`](./setneedsfocusupdate%28%29.md), it does not matter if this environment currently contains focus, or if this environment is the one pending an update.

## See Also

### Requesting focus update
- [func setNeedsFocusUpdate()](./setneedsfocusupdate%28%29.md)
  Submits a request to the focus engine for a focus update in this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/updatefocusifneeded())*