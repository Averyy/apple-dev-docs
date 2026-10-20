# allow(withUpdateRules:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NEFilterControlVerdict *) allowVerdictWithUpdateRules:(BOOL) updateRules;
```

#### Return Value

An `NEFilterControlVerdict` object.

#### Discussion

When the Filter Control Provider passes this verdict to the completion handler passed to its [`handleNewFlow(_:completionHandler:)`](../nefiltercontrolprovider/handlenewflow%28_,completionhandler%29.md) method, the system will allow all of the flow’s data to pass to its final destination. In addition, if the `updateRules` parameter is YES the system will call the Filter Data Provider’s [`handleRulesChanged()`](../nefilterdataprovider/handleruleschanged%28%29.md) method.

## Parameters

- `updateRules`: A Boolean indicating if the Filter Control Provider updated the rules.

## See Also

### Creating control verdicts
- [class func drop(withUpdateRules: Bool) -> NEFilterControlVerdict](./drop%28withupdaterules%29.md)
  Create a verdict that indicates to the system that all of the flow’s data should be dropped, and that the filtering rules have been updated.
- [class func updateRules() -> NEFilterControlVerdict](./updaterules%28%29.md)
  Create a verdict that indicates to the system that the filtering rules have been updated, and that the Filter Data Provider needs to make a decision about the flow’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/allow(withupdaterules:))*