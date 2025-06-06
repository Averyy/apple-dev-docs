# viewController

**Framework**: AppKit  
**Kind**: property

The view controller that the split view item represents.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var viewController: NSViewController { get set }
```

#### Discussion

Don’t set this property while adding the split view item to a split view controller. If you do, the system raises an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/viewcontroller)*