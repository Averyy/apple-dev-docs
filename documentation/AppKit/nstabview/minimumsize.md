# minimumSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum size necessary for the tab view to display tabs in a useful way.

**Availability**:
- macOS

## Declaration

```swift
var minimumSize: NSSize { get }
```

```objc
@property (readonly) NSSize minimumSize;
```

## Discussion

You can use the value of this property to limit how much a user can resize a tab view.

## See Also

### Related Documentation
- [var tabViewType: NSTabView.TabType](./tabviewtype.md)
  The tab type to display the tabs.
### Determining the Size
- [var contentRect: NSRect](./contentrect.md)
  The rectangle describing the content area of the tab view.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/minimumsize)*