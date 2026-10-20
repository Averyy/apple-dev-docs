# removeActionSet(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes an action set from the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
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

### Managing Action Sets
- [var actionSets: [HMActionSet]](./actionsets.md)
  Array of all action sets that will be executed by the trigger.
- [func addActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./addactionset%28_,completionhandler%29.md)
  Adds an action set to the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/removeactionset(_:completionhandler:))*