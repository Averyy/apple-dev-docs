# NSAppKitVersionNumberWithPatternColorLeakFix

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The specific version of the AppKit framework from OS X 10.1 that correctly autoreleases color objects.

**Availability**:
- macOS

## Declaration

```c
static const NSAppKitVersion NSAppKitVersionNumberWithPatternColorLeakFix;
```

#### Discussion

Developers do not need to use this constant unless they are writing applications for OS X 10.1 and earlier.

The constant represents the specific version of the AppKit framework that introduced the fix for correctly autoreleasing objects returned by the [`init(patternImage:)`](./nscolor/init%28patternimage%29.md) method.

## See Also

### Feature Introductions
- [NSAppKitVersionNumberWithColumnResizingBrowser](./nsappkitversionnumberwithcolumnresizingbrowser.md)
  The specific version of the AppKit framework that introduced support for resizing individual browser columns.
- [NSAppKitVersionNumberWithContinuousScrollingBrowser](./nsappkitversionnumberwithcontinuousscrollingbrowser.md)
  The specific version of the AppKit framework that introduced support the continuous scrolling in a browser view.
- [NSAppKitVersionNumberWithCursorSizeSupport](./nsappkitversionnumberwithcursorsizesupport.md)
  The specific version of the AppKit framework that introduced support for cursors larger than 16 x 16 pixels in size.
- [NSAppKitVersionNumberWithCustomSheetPosition](./nsappkitversionnumberwithcustomsheetposition.md)
  The specific version of the AppKit framework that introduced custom sheet positioning.
- [NSAppKitVersionNumberWithDeferredWindowDisplaySupport](./nsappkitversionnumberwithdeferredwindowdisplaysupport.md)
  The specific version of the AppKit framework that introduced support for deferred window display.
- [NSAppKitVersionNumberWithDirectionalTabs](./nsappkitversionnumberwithdirectionaltabs.md)
  The specific version of the AppKit framework that introduced support for directional tab items.
- [NSAppKitVersionNumberWithDockTilePlugInSupport](./nsappkitversionnumberwithdocktilepluginsupport.md)
  The specific version of the AppKit framework that introduced support for dock tile plug-ins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappkitversionnumberwithpatterncolorleakfix)*