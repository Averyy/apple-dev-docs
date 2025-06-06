# allow(withUpdateRules:)

**Framework**: Network Extension  
**Kind**: method

Create a verdict that indicates to the system that all of the flow’s data should be allowed to pass to its final destination, and that the filtering rules have been updated.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func allow(withUpdateRules updateRules: Bool) -> NEFilterControlVerdict
```

#### Return Value

An `NEFilterControlVerdict` object.

#### Discussion

When the Filter Control Provider passes this verdict to the completion handler passed to its [`handleNewFlow(_:completionHandler:)`](nefiltercontrolprovider/handlenewflow(_:completionhandler:).md) method, the system will allow all of the flow’s data to pass to its final destination. In addition, if the `updateRules` parameter is YES the system will call the Filter Data Provider’s [`handleRulesChanged()`](nefilterdataprovider/handleruleschanged().md) method.

## Parameters

- `updateRules`: A Boolean indicating if the Filter Control Provider updated the rules.

## See Also

- [class func drop(withUpdateRules: Bool) -> NEFilterControlVerdict](nefiltercontrolverdict/drop(withupdaterules:).md)
  Create a verdict that indicates to the system that all of the flow’s data should be dropped, and that the filtering rules have been updated.
- [class func updateRules() -> NEFilterControlVerdict](nefiltercontrolverdict/updaterules.md)
  Create a verdict that indicates to the system that the filtering rules have been updated, and that the Filter Data Provider needs to make a decision about the flow’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/allow(withupdaterules:))*