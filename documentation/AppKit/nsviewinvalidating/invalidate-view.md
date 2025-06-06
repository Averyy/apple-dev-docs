# invalidate(view:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
func invalidate(view: NSView)
```

#### Discussion

A type that conforms to `UIViewInvalidating` implements this method to perform any actions necessary to notify the system that an aspect of your view is invalid. For more info, see [`NSView.Invalidating`](nsview/invalidating.md).

## Parameters

- `view`: The view that requires invalidating.

## See Also

- [NSView.Invalidations](nsview/invalidations.md)
  Changes that cause aspects of a view to be invalid and require an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewinvalidating/invalidate(view:))*