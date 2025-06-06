# layoutIfNeeded()

**Framework**: AppKit  
**Kind**: method

Updates the layout of views in the window based on the current views and constraints.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func layoutIfNeeded()
```

#### Discussion

Before displaying a window that uses constraints-based layout the system invokes this method to ensure that the layout of all views is up to date. This method updates the layout if needed, first invoking [`updateConstraintsIfNeeded()`](nswindow/updateconstraintsifneeded().md) to ensure that all constraints are up to date. This method is called automatically by the system, but may be invoked manually if you need to examine the most up to date layout.

Subclasses should not override this method.

## See Also

- [func updateConstraintsIfNeeded()](nswindow/updateconstraintsifneeded.md)
  Updates the constraints based on changes to views in the window since the last layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/layoutifneeded())*