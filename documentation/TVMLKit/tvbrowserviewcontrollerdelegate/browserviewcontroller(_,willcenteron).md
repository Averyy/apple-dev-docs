# browserViewController(_:willCenterOn:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the specified view element is to be centered on the page.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func browserViewController(_ browserViewController: TVBrowserViewController, willCenterOn viewElement: TVViewElement)
```

```objc
- (void) browserViewController:(TVBrowserViewController *) browserViewController willCenterOnViewElement:(TVViewElement *) viewElement;
```

## See Also

### Managing Focus
- [func browserViewController(TVBrowserViewController, didCenterOn: TVViewElement)](./browserviewcontroller%28_,didcenteron%29.md)
  Tells the delegate how to respond when the specified view element completes the transition to becoming centered upon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontrollerdelegate/browserviewcontroller(_:willcenteron:))*