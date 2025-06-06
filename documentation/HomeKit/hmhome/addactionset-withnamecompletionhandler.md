# addActionSet(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a new action set to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addActionSet(named actionSetName: String) async throws -> HMActionSet
```

## Parameters

- `actionSetName`: The name of the new action set. Must not be  , and must not be the name of an action set already in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var actionSets: [HMActionSet]](hmhome/actionsets.md)
  An array of the action sets in the home.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmhome/removeactionset(_:completionhandler:).md)
  Removes an action set from the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmhome/executeactionset(_:completionhandler:).md)
  Executes all the actions in a specified action set.
- [func builtinActionSet(ofType: String) -> HMActionSet?](hmhome/builtinactionset(oftype:).md)
  Retrieves the builtin action set for the specified type.
- [class HMActionSet](hmactionset.md)
  A collection of actions that you trigger as a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addactionset(withname:completionhandler:))*