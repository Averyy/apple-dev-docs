# TVBrowserViewControllerDelegate

**Framework**: TVMLKit  
**Kind**: protocol

Methods for detecting events and performing actions on the browser view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
protocol TVBrowserViewControllerDelegate : NSObjectProtocol
```

## Topics

### Managing Focus
- [func browserViewController(TVBrowserViewController, didCenterOn: TVViewElement)](tvbrowserviewcontrollerdelegate/browserviewcontroller(_:didcenteron:).md)
  Tells the delegate how to respond when the specified view element completes the transition to becoming centered upon.
- [func browserViewController(TVBrowserViewController, willCenterOn: TVViewElement)](tvbrowserviewcontrollerdelegate/browserviewcontroller(_:willcenteron:).md)
  Tells the delegate when the specified view element is to be centered on the page.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any TVBrowserViewControllerDelegate)?](tvbrowserviewcontroller/delegate.md)
  The object that acts as the delegate and handles callbacks for the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontrollerdelegate)*