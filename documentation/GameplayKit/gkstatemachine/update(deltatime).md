# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Tells the current state object to perform per-frame updates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func update(deltaTime sec: TimeInterval)
```

```objc
- (void) updateWithDeltaTime:(NSTimeInterval) sec;
```

## Discussion

When you call this method, the state machine sends the [`update(deltaTime:)`](../gkstate/update%28deltatime%29.md) message to its [`currentState`](./currentstate.md) object. In that method, your custom [`GKState`](../gkstate.md) subclasses can do work that needs to be done periodically while the machine is in a specific state. Typically, you call this method once for every frame your game processes or renders—such as in the [`update(_:)`](../../SpriteKit/skscene/update%28_%29.md) method of a SpriteKit scene or the [`renderer(_:updateAtTime:)`](../../SceneKit/scnscenerendererdelegate/renderer%28_,updateattime%29.md) method of a SceneKit render delegate. If your game uses Entity-Component design (see [Entities and Components](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172)), you can call this method from the [`update(deltaTime:)`](../gkcomponent/update%28deltatime%29.md) method of a [`GKComponent`](../gkcomponent.md) subclass.

Examples of per-frame state updates include:

- A state machine for an enemy character might have Idle and Chase states. The Chase state’s update method might check the location of the player character and move the enemy character in that direction.
- A state machine for an automated turret might have Ready, Firing, and Cooldown states. The Ready state’s update method might look for nearby enemies to attack and transition to the Firing state upon finding one. The Cooldown state’s update method might track the elapsed time since entering that state and transition to the Ready state after a specific amount of time has passed.
- A state machine that runs a game’s overall UI might have Menu, Playing, Paused, and GameOver states. The Playing state’s update method might delegate to per-frame update methods in other entities that drive gameplay.

## Parameters

- `sec`: The time step to use for any time-dependent actions performed by this method (typically, the elapsed time since the previous call to this method).

## See Also

### Working with States
- [var currentState: GKState?](./currentstate.md)
  The state machine’s current state.
- [func canEnterState(AnyClass) -> Bool](./canenterstate%28_%29.md)
  Returns a Boolean value indicating whether it is valid for the state machine to transition from its current state to a state of the specified class.
- [func enter(AnyClass) -> Bool](./enter%28_%29.md)
  Attempts to transition the state machine from its current state to a state of the specified class.
- [- stateForClass:](./stateforclass_.md)
  Returns the state object in the state machine corresponding to the specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/update(deltatime:))*