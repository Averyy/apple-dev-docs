# actionSets

**Framework**: HomeKit  
**Kind**: property

An array of the action sets in the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var actionSets: [HMActionSet] { get }
```

#### Discussion

Action sets are instances of [`HMActionSet`](hmactionset.md).

## See Also

- [func addActionSet(withName: String, completionHandler: (HMActionSet?, (any Error)?) -> Void)](hmhome/addactionset(withname:completionhandler:).md)
  Adds a new action set to the home.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmhome/removeactionset(_:completionhandler:).md)
  Removes an action set from the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmhome/executeactionset(_:completionhandler:).md)
  Executes all the actions in a specified action set.
- [func builtinActionSet(ofType: String) -> HMActionSet?](hmhome/builtinactionset(oftype:).md)
  Retrieves the builtin action set for the specified type.
- [class HMActionSet](hmactionset.md)
  A collection of actions that you trigger as a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/actionsets)*