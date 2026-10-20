# init(toFollow:maxPredictionTime:forward:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Creates a goal whose effect is to both maintain position on and traverse the specified path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toFollow path: GKPath, maxPredictionTime: TimeInterval, forward: Bool)
```

```objc
+ (instancetype) goalToFollowPath:(GKPath *) path maxPredictionTime:(NSTimeInterval) maxPredictionTime forward:(BOOL) forward;
```

#### Return Value

A new goal object.

#### Discussion

This goal uses the shape and the [`radius`](../gkpath/radius.md) property of the specified path to define the agent’s desired movement. The agent first attempts to reach a location near the path’s start point (or end point if the forward parameter is [`false`](../../Swift/false.md)), to a tolerance determined by the path’s radius. Then, the agent attemps to move toward the next point in the path, again with a tolerance determined by the path’s radius. This sequence continues until the path terminates, or repeats indefinitely if the path’s [`isCyclical`](../gkpath/iscyclical.md) property is [`true`](../../Swift/true.md).

The `maxPredictionTime` parameter determines how far ahead of time the agent will predict its own movement to fulfill this goal. For example, with a larger value, an agent moving toward the path will begin to slow gradually so as to stop gently within the path’s radius. With a smaller value, the agent will attempt to stop more abruptly as it reaches the path (and depending on its properties, it might not be able to stop quickly enough to avoid overshooting).

## Parameters

- `path`: A path object.
- `maxPredictionTime`: The amount of time for which to predict an affected agent’s movement.
- `forward`: [`true`](../../Swift/true.md) to traverse in the order the path’s verties are defined; [`false`](../../Swift/false.md) to traverse the path in the opposite order.

## See Also

### Creating Goals for Path-Following Behavior
- [convenience init(toStayOn: GKPath, maxPredictionTime: TimeInterval)](./init%28tostayon,maxpredictiontime%29.md)
  Creates a goal whose effect is to maintain an agent’s position within the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(tofollow:maxpredictiontime:forward:))*