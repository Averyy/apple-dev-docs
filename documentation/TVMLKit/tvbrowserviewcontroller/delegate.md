# delegate

**Framework**: TVMLKit  
**Kind**: property

The object that acts as the delegate and handles callbacks for the browser view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
weak var delegate: (any TVBrowserViewControllerDelegate)? { get set }
```

## See Also

- [protocol TVBrowserViewControllerDelegate](tvbrowserviewcontrollerdelegate.md)
  Methods for detecting events and performing actions on the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller/delegate)*