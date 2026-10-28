# view:stringForToolTip:point:userData:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the tool tip string to be displayed due to the cursor pausing at location `point` within the tool tip rectangle identified by `tag` in the view `view`.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (NSString *) view:(NSView *) view stringForToolTip:(NSToolTipTag) tag point:(NSPoint) point userData:(void *) data;
```

## Discussion

`userData` is additional information provided by the creator of the tool tip rectangle.

## See Also

### Related Documentation
- [Online Help](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/OnlineHelp.html#//apple_ref/doc/uid/10000009i)
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](../../AppKit/nsview/addtooltip%28_,owner,userdata%29.md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/view:stringfortooltip:point:userdata:)*