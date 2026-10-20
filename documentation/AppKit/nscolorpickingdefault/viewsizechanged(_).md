# viewSizeChanged(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the recever when the color panel’s view size changes in a way that might affect the color picker.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func viewSizeChanged(_ sender: Any?)
```

```objc
- (void) viewSizeChanged:(id) sender;
```

#### Discussion

Use this method to perform special preparation when resizing the color picker’s view. Because this method is invoked only as appropriate, it’s better to implement this method than to override the method `superviewSizeChanged:` for the `NSView` in which the color picker’s user interface is contained.

## Parameters

- `sender`: The `NSColorPanel` that contains the color picker.

## See Also

### Related Documentation
- [func provideNewView(Bool) -> NSView](../nscolorpickingcustom/providenewview%28_%29.md)
  Returns the view containing the receiver’s user interface.
### Handling Events
- [func alphaControlAddedOrRemoved(Any?)](./alphacontroladdedorremoved%28_%29.md)
  Sent when the color panel’s opacity controls have been hidden or displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/viewsizechanged(_:))*