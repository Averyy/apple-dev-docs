# addActionSet(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a new action set to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addActionSet(withName actionSetName: String, completionHandler completion: @escaping @Sendable (HMActionSet?, (any Error)?) -> Void)
```

```swift
func addActionSet(named actionSetName: String) async throws -> HMActionSet
```

```objc
- (void) addActionSetWithName:(NSString *) actionSetName completionHandler:(void (^)(HMActionSet *actionSet, NSError *error)) completion;
```

## Parameters

- `actionSetName`: The name of the new action set. Must not be `nil`, and must not be the name of an action set already in the home.
- `completion`: The block executed after the request is processed.

  - **actionSet**: The newly created action set.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Creating action sets
- [var actionSets: [HMActionSet]](./actionsets.md)
  An array of the action sets in the home.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./removeactionset%28_,completionhandler%29.md)
  Removes an action set from the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./executeactionset%28_,completionhandler%29.md)
  Executes all the actions in a specified action set.
- [func builtinActionSet(ofType: String) -> HMActionSet?](./builtinactionset%28oftype%29.md)
  Retrieves the builtin action set for the specified type.
- [class HMActionSet](../hmactionset.md)
  A collection of actions that you trigger as a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addactionset(withname:completionhandler:))*