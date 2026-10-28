# panel:shouldShowFilename:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Gives the delegate the opportunity to filter items that it doesn’t want the user to choose.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`panel(_:shouldEnable:)`](../../AppKit/nsopensavepaneldelegate/panel%28_,shouldenable%29.md) ([`NSOpenSavePanelDelegate`](../../AppKit/nsopensavepaneldelegate.md)).

## Declaration

```objc
- (BOOL) panel:(id) sender shouldShowFilename:(NSString *) filename;
```

## Return Value

[`YES`](../yes.md) if `filename` should be selectable, and [`NO`](../no.md) if the save panel should disable the file or directory.

## Discussion

The `NSSavePanel` object `sender` sends this message to the panel’s delegate for each file or directory (filename) it is about to load in the browser.

## Parameters

- `sender`: Panel that is querying whether it should show a certain file.
- `filename`: String representing the name of the file to be loaded in the browser.

## See Also

### Related Documentation
- [func panel(Any, shouldEnable: URL) -> Bool](../../AppKit/nsopensavepaneldelegate/panel%28_,shouldenable%29.md)
  Asks the delegate whether the specified URL should be enabled in the Open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:shouldshowfilename:)*