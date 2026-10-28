# textLayoutManagers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of text layout managers associated with this text content manager.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var textLayoutManagers: [NSTextLayoutManager] { get }
```

```objc
@property (copy, readonly) NSArray<NSTextLayoutManager *> * textLayoutManagers;
```

## Discussion

This property is KVO-compliant.

## See Also

### Working with layout managers
- [var primaryTextLayoutManager: NSTextLayoutManager?](./primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var automaticallySynchronizesTextLayoutManagers: Bool](./automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func addTextLayoutManager(NSTextLayoutManager)](./addtextlayoutmanager%28_%29.md)
  Adds the layout manager you provide to the list of layout managers.
- [func removeTextLayoutManager(NSTextLayoutManager)](./removetextlayoutmanager%28_%29.md)
  Removes the layout manager you specifiy from the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](./synchronizetextlayoutmanagers%28_%29.md)
  Synchronizes changes to all nonprimary text layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/textlayoutmanagers)*