# init(toStayOn:maxPredictionTime:)

**Framework**: GameplayKit  
**Kind**: init

Creates a goal whose effect is to maintain an agent’s position within the specified path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toStayOn path: GKPath, maxPredictionTime: TimeInterval)
```

#### Return Value

A new goal object.

#### Discussion

This goal uses the shape and the [`radius`](gkpath/radius.md) property of the specified path to define the boundaries of an area for the agent to stay in. If an affected agent is outside that area, the agent will move into that area; if the agent is already in that area, this goal will not motivate the agent to move further.

The `maxPredictionTime` parameter determines how far ahead of time the agent will predict its own movement to fulfill this goal. For example, with a larger value, an agent moving toward the path will begin to slow gradually so as to stop gently within the path’s radius. With a smaller value, the agent will attempt to stop more abruptly as it reaches the path (and depending on its properties, it might not be able to stop quickly enough to avoid overshooting).

## Parameters

- `path`: A path object.
- `maxPredictionTime`: The amount of time for which to predict an affected agent’s movement.

## See Also

- [convenience init(toFollow: GKPath, maxPredictionTime: TimeInterval, forward: Bool)](gkgoal/init(tofollow:maxpredictiontime:forward:).md)
  Creates a goal whose effect is to both maintain position on and traverse the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(tostayon:maxpredictiontime:))*