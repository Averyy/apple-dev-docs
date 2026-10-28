# sequence(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that runs a collection of actions sequentially.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class func sequence(_ actions: [SCNAction]) -> SCNAction
```

```objc
+ (SCNAction *) sequence:(NSArray<SCNAction *> *) actions;
```

## Return Value

A new sequence action object.

## Discussion

When the action executes, the first action in the sequence starts and runs to completion. Subsequent actions in the sequence run in a similar fashion until all of the actions in the sequence have executed. The duration of the sequence action is the sum of the durations of the actions in the sequence.

This action is reversible; it creates a new sequence action that reverses the order of the actions. Each action in the reversed sequence is itself reversed. For example, the actions `reverseSequence` and `sequenceReverse` in the code example below are equivalent:

```objc
SCNAction *sequence = [SCNAction sequence:@[ actionA, actionB, actionC ]];
SCNAction *reverseSequence = [SCNAction sequence:@[ [actionC reversedAction],
                                                    [actionB reversedAction],
                                                    [actionA reversedAction] ]];
SCNAction *sequenceReverse = [sequence reversedAction];
```

## Parameters

- `actions`: An array of [`SCNAction`](../scnaction.md) objects.

## See Also

### Creating Actions That Combine or Repeat Other Actions
- [class func group([SCNAction]) -> SCNAction](./group%28_%29.md)
  Creates an action that runs a collection of actions in parallel.
- [class func `repeat`(SCNAction, count: Int) -> SCNAction](./repeat%28_,count%29.md)
  Creates an action that repeats another action a specified number of times.
- [class func repeatForever(SCNAction) -> SCNAction](./repeatforever%28_%29.md)
  Creates an action that repeats another action forever.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/sequence(_:))*