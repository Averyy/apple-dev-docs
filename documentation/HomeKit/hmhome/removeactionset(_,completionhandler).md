# removeActionSet(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes an action set from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeActionSet(_ actionSet: HMActionSet) async throws
```

```objc
- (void) removeActionSet:(HMActionSet *) actionSet completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `actionSet`: The action set to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Creating action sets
- [var actionSets: [HMActionSet]](./actionsets.md)
  An array of the action sets in the home.
- [func addActionSet(withName: String, completionHandler: (HMActionSet?, (any Error)?) -> Void)](./addactionset%28withname,completionhandler%29.md)
  Adds a new action set to the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./executeactionset%28_,completionhandler%29.md)
  Executes all the actions in a specified action set.
- [func builtinActionSet(ofType: String) -> HMActionSet?](./builtinactionset%28oftype%29.md)
  Retrieves the builtin action set for the specified type.
- [class HMActionSet](../hmactionset.md)
  A collection of actions that you trigger as a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeactionset(_:completionhandler:))*