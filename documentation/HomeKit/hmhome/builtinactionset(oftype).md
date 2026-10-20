# builtinActionSet(ofType:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the builtin action set for the specified type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func builtinActionSet(ofType actionSetType: String) -> HMActionSet?
```

```objc
- (HMActionSet *) builtinActionSetOfType:(NSString *) actionSetType;
```

#### Return Value

The builtin action set corresponding to the type argument.

#### Discussion

Returns `nil` if no action set is found.

## Parameters

- `actionSetType`: Type of the builtin action set. Supported action set types are [`HMActionSetTypeWakeUp`](../hmactionsettypewakeup.md), [`HMActionSetTypeSleep`](../hmactionsettypesleep.md), [`HMActionSetTypeHomeDeparture`](../hmactionsettypehomedeparture.md) and [`HMActionSetTypeHomeArrival`](../hmactionsettypehomearrival.md).

## See Also

### Creating action sets
- [var actionSets: [HMActionSet]](./actionsets.md)
  An array of the action sets in the home.
- [func addActionSet(withName: String, completionHandler: (HMActionSet?, (any Error)?) -> Void)](./addactionset%28withname,completionhandler%29.md)
  Adds a new action set to the home.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./removeactionset%28_,completionhandler%29.md)
  Removes an action set from the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./executeactionset%28_,completionhandler%29.md)
  Executes all the actions in a specified action set.
- [class HMActionSet](../hmactionset.md)
  A collection of actions that you trigger as a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/builtinactionset(oftype:))*