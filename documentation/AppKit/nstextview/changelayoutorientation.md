# changeLayoutOrientation(_:)

**Framework**: AppKit  
**Kind**: method

An action method that sets the layout orientation of the text.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func changeLayoutOrientation(_ sender: Any?)
```

#### Discussion

Calls [`setLayoutOrientation(_:)`](nstextview/setlayoutorientation(_:).md) with the sender’s tag as the orientation.

## Parameters

- `sender`: The sender.

## See Also

- [func setLayoutOrientation(NSLayoutManager.TextLayoutOrientation)](nstextview/setlayoutorientation(_:).md)
  Changes the receiver’s layout orientation and invalidates the contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/changelayoutorientation(_:))*