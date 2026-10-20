# removeLayoutManager(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a layout manager from the text storage object’s set of layout managers.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func removeLayoutManager(_ aLayoutManager: NSLayoutManager)
```

```objc
- (void) removeLayoutManager:(NSLayoutManager *) aLayoutManager;
```

## Parameters

- `aLayoutManager`: The layout manager to remove.

## See Also

### Accessing the layout managers
- [var layoutManagers: [NSLayoutManager]](./layoutmanagers.md)
  The layout managers for the text storage object.
- [func addLayoutManager(NSLayoutManager)](./addlayoutmanager%28_%29.md)
  Adds a layout manager to the text storage object’s set of layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/removelayoutmanager(_:))*