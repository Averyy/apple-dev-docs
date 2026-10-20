# layoutManagers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout managers for the text storage object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var layoutManagers: [NSLayoutManager] { get }
```

```objc
@property (copy, readonly) NSArray<NSLayoutManager *> * layoutManagers;
```

## See Also

### Accessing the layout managers
- [func addLayoutManager(NSLayoutManager)](./addlayoutmanager%28_%29.md)
  Adds a layout manager to the text storage object’s set of layout managers.
- [func removeLayoutManager(NSLayoutManager)](./removelayoutmanager%28_%29.md)
  Removes a layout manager from the text storage object’s set of layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/layoutmanagers)*