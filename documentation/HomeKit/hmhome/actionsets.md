# actionSets

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSArray<HMActionSet *> * actionSets;
```

## Discussion

Action sets are instances of [`HMActionSet`](../hmactionset.md).

## See Also

### Creating action sets
- [func addActionSet(withName: String, completionHandler: (HMActionSet?, (any Error)?) -> Void)](./addactionset%28withname,completionhandler%29.md)
  Adds a new action set to the home.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./removeactionset%28_,completionhandler%29.md)
  Removes an action set from the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./executeactionset%28_,completionhandler%29.md)
  Executes all the actions in a specified action set.
- [func builtinActionSet(ofType: String) -> HMActionSet?](./builtinactionset%28oftype%29.md)
  Retrieves the builtin action set for the specified type.
- [class HMActionSet](../hmactionset.md)
  A collection of actions that you trigger as a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/actionsets)*