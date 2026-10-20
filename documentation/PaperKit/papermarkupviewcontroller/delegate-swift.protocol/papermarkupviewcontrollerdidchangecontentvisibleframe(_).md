# paperMarkupViewControllerDidChangeContentVisibleFrame(_:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate when a person scrolls or zooms the content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func paperMarkupViewControllerDidChangeContentVisibleFrame(_ paperMarkupViewController: PaperMarkupViewController)
```

## Parameters

- `paperMarkupViewController`: The `PaperMarkupViewController` the person is interacting with.

## Default Implementations

### PaperMarkupViewController.Delegate Implementations
- [func paperMarkupViewControllerDidChangeContentVisibleFrame(PaperMarkupViewController)](./papermarkupviewcontrollerdidchangecontentvisibleframe%28_%29-5k7zk.md)
  Tells the delegate when a person scrolls or zooms the content.

## See Also

### Responding to markup changes
- [func paperMarkupViewControllerDidChangeMarkup(PaperMarkupViewController)](./papermarkupviewcontrollerdidchangemarkup%28_%29.md)
  Tells the delegate when the markup changes.
- [func paperMarkupViewControllerDidChangeSelection(PaperMarkupViewController)](./papermarkupviewcontrollerdidchangeselection%28_%29.md)
  Tells the delegate when the selection changes.
- [func paperMarkupViewControllerDidBeginDrawing(PaperMarkupViewController)](./papermarkupviewcontrollerdidbegindrawing%28_%29.md)
  Tells the delegate when a person begins drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.protocol/papermarkupviewcontrollerdidchangecontentvisibleframe(_:))*