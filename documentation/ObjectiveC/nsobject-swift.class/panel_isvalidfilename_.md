# panel:isValidFilename:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Gives the delegate the opportunity to validate selected items.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`panel(_:validate:)`](../../AppKit/nsopensavepaneldelegate/panel%28_,validate%29.md) ([`NSOpenSavePanelDelegate`](../../AppKit/nsopensavepaneldelegate.md)) instead. If both methods are implemented, the URL version will be called.

## Declaration

```objc
- (BOOL) panel:(id) sender isValidFilename:(NSString *) filename;
```

#### Return Value

[`YES`](../yes.md) if the filename is valid, or [`NO`](../no.md) if the save panel should stay in its modal loop and wait for the user to type in or select a different filename or names.

#### Discussion

The `NSSavePanel` object `sender` sends this message just before the end of a modal session for each filename displayed or selected (including filenames in multiple selections). If the delegate refuses a filename in a multiple selection, none of the filenames in the selection is accepted.

## Parameters

- `sender`: Panel requesting filename validation.
- `filename`: String representing the filename to validate.

## See Also

### Related Documentation
- [func panel(Any, validate: URL) throws](../../AppKit/nsopensavepaneldelegate/panel%28_,validate%29.md)
  Asks the delegate to validate the URL for a file that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:isvalidfilename:)*