# updateRules()

**Framework**: Network Extension  
**Kind**: method

Create a verdict that indicates to the system that the filtering rules have been updated, and that the Filter Data Provider needs to make a decision about the flow’s data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func updateRules() -> NEFilterControlVerdict
```

#### Return Value

An `NEFilterControlVerdict` object.

## See Also

- [class func allow(withUpdateRules: Bool) -> NEFilterControlVerdict](nefiltercontrolverdict/allow(withupdaterules:).md)
  Create a verdict that indicates to the system that all of the flow’s data should be allowed to pass to its final destination, and that the filtering rules have been updated.
- [class func drop(withUpdateRules: Bool) -> NEFilterControlVerdict](nefiltercontrolverdict/drop(withupdaterules:).md)
  Create a verdict that indicates to the system that all of the flow’s data should be dropped, and that the filtering rules have been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/updaterules())*