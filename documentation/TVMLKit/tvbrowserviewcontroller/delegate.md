# delegate

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate and handles callbacks for the browser view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
weak var delegate: (any TVBrowserViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<TVBrowserViewControllerDelegate> delegate;
```

## See Also

### Managing Interactions with the Browser
- [protocol TVBrowserViewControllerDelegate](../tvbrowserviewcontrollerdelegate.md)
  Methods for detecting events and performing actions on the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller/delegate)*