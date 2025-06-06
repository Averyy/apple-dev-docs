# tapHandler

**Framework**: Social  
**Kind**: property

A custom tap handler block that handles user interaction with a configuration item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var tapHandler: SLComposeSheetConfigurationItemTapHandler! { get set }
```

#### Discussion

Called when the user taps the configuration item. Note that `tapHandler` is called on the main queue; to avoid a possible retain cycle, your block should not keep a strong reference to either the configuration item or the compose view controller.

## See Also

- [typealias SLComposeSheetConfigurationItemTapHandler](slcomposesheetconfigurationitemtaphandler.md)
  The method signature for a configuration item’s tap handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitem/taphandler)*