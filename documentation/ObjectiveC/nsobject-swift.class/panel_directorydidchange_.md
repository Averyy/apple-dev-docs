# panel:directoryDidChange:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has changed the selected directory in the `NSSavePanel` object specified.

**Availability**:
- macOS 10.3+ - Deprecated in 10.6

> **Deprecated**: Use [`panel(_:didChangeToDirectoryURL:)`](../../AppKit/nsopensavepaneldelegate/panel%28_,didchangetodirectoryurl%29.md) ([`NSOpenSavePanelDelegate`](../../AppKit/nsopensavepaneldelegate.md)) instead.

## Declaration

```objc
- (void) panel:(id) sender directoryDidChange:(NSString *) path;
```

## Parameters

- `sender`: Panel whose directory has changed.
- `path`: String representing the new directory’s path.

## See Also

### Related Documentation
- [func panel(Any, didChangeToDirectoryURL: URL?)](../../AppKit/nsopensavepaneldelegate/panel%28_,didchangetodirectoryurl%29.md)
  Tells the delegate that the user changed the selected directory to the directory located at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:directorydidchange:)*