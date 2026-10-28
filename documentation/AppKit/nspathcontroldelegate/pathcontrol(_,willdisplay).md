# pathControl(_:willDisplay:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implement this method to customize the Open panel shown by a pop-up–style path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathControl(_ pathControl: NSPathControl, willDisplay openPanel: NSOpenPanel)
```

```objc
- (void) pathControl:(NSPathControl *) pathControl willDisplayOpenPanel:(NSOpenPanel *) openPanel;
```

## Discussion

This method is called before the Open panel is shown but after its allowed file types are set to the cell’s allowed types. At this time, you can further customize the Open panel as required. This method is called only when the style is set to `NSPathStylePopUp`. Implementation of this method is optional.

## Parameters

- `pathControl`: The path control displaying the Open panel.
- `openPanel`: The Open panel to be displayed.

## See Also

### Customizing a Pop-Up–Style Path
- [func pathControl(NSPathControl, willPopUp: NSMenu)](./pathcontrol%28_,willpopup%29.md)
  Implement this method to customize the menu of a pop-up–style path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/pathcontrol(_:willdisplay:))*