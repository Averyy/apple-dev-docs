# changeLayoutOrientation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action method that sets the layout orientation of the text.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func changeLayoutOrientation(_ sender: Any?)
```

```objc
- (void) changeLayoutOrientation:(id) sender;
```

#### Discussion

Calls [`setLayoutOrientation(_:)`](./setlayoutorientation%28_%29.md) with the sender’s tag as the orientation.

## Parameters

- `sender`: The sender.

## See Also

### Changing layout orientation
- [func setLayoutOrientation(NSLayoutManager.TextLayoutOrientation)](./setlayoutorientation%28_%29.md)
  Changes the receiver’s layout orientation and invalidates the contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/changelayoutorientation(_:))*