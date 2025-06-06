# init(toCohereWith:maxDistance:maxAngle:)

**Framework**: GameplayKit  
**Kind**: init

Creates a goal whose effect is to make an agent stay near the other agents in a specified group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toCohereWith agents: [GKAgent], maxDistance: Float, maxAngle: Float)
```

#### Return Value

A new goal object.

#### Discussion

The `agents` array can safely include the agent(s) affected by the goal—an agent pursuing this goal will ignore itself in the array. Therefore, you can use a single goal created with this method to cause an entire group of agents to mutually stay near one another.

Changing the `maxDistance` parameter determines how close to one another agents need to be in order for them to form a group. Changing the `maxAngle` parameter determines how tightly an agent will turn to maintain cohesion in the group.

You can combine separation, alignment, and cohesion goals to produce “flocking” behaviors in which a group of agents move together.

## Parameters

- `agents`: The agents with whom to stay close.
- `maxDistance`: The maximum distance from other agents required for this goal to take effect.
- `maxAngle`: The maximum angle, in radians, between an affected agent’s velocity and the direction toward the other agents required for this goal to take effect.

## See Also

- [convenience init(toSeparateFrom: [GKAgent], maxDistance: Float, maxAngle: Float)](gkgoal/init(toseparatefrom:maxdistance:maxangle:).md)
  Creates a goal whose effect is to make an agent maintain the specified distance from other agents in a specified group.
- [convenience init(toAlignWith: [GKAgent], maxDistance: Float, maxAngle: Float)](gkgoal/init(toalignwith:maxdistance:maxangle:).md)
  Creates a goal whose effect is to make an agent align its orientation with that of other agents in a specified group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(tocoherewith:maxdistance:maxangle:))*