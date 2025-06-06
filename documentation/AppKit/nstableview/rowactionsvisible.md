# rowActionsVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether a table row’s actions are visible.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var rowActionsVisible: Bool { get set }
```

#### Discussion

This property contains a Boolean value indicating whether a table row’s actions are visible or not—the user has swiped the row to reveal the row actions. Set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false) to hide any visible row actions. Setting the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) is not supported, and will result in an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowactionsvisible)*