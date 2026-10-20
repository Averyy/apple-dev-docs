# browserViewController(_:didCenterOn:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate how to respond when the specified view element completes the transition to becoming centered upon.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
optional func browserViewController(_ browserViewController: TVBrowserViewController, didCenterOn viewElement: TVViewElement)
```

```objc
- (void) browserViewController:(TVBrowserViewController *) browserViewController didCenterOnViewElement:(TVViewElement *) viewElement;
```

## See Also

### Managing Focus
- [func browserViewController(TVBrowserViewController, willCenterOn: TVViewElement)](./browserviewcontroller%28_,willcenteron%29.md)
  Tells the delegate when the specified view element is to be centered on the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontrollerdelegate/browserviewcontroller(_:didcenteron:))*