# addLayoutManager(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a layout manager to the text storage object’s set of layout managers.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func addLayoutManager(_ aLayoutManager: NSLayoutManager)
```

```objc
- (void) addLayoutManager:(NSLayoutManager *) aLayoutManager;
```

## Parameters

- `aLayoutManager`: The layout manager to add.

## See Also

### Accessing the layout managers
- [var layoutManagers: [NSLayoutManager]](./layoutmanagers.md)
  The layout managers for the text storage object.
- [func removeLayoutManager(NSLayoutManager)](./removelayoutmanager%28_%29.md)
  Removes a layout manager from the text storage object’s set of layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/addlayoutmanager(_:))*