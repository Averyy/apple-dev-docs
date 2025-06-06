# tabState

**Framework**: AppKit  
**Kind**: property

Returns the current display state of the tab associated with the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
var tabState: NSTabViewItem.State { get }
```

#### Discussion

The possible values are `NSSelectedTab`, `NSBackgroundTab`, or `NSPressedTab`. Your application does not directly set the tab state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/tabstate)*