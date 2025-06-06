# Controlling Actions Precisely by Using Names

**Framework**: SpriteKit

Set an action’s name property so you can access it later without needing an instance variable.

#### Overview

Normally, you can’t see which actions a node is executing, and if you want to remove actions, you must remove all of them. If you need to see whether a particular action is executing, or if you want to remove a specific action, use named actions. A named action is characterized by a unique string that identifies the action. Using named actions, you can start, remove, find and replace the actions of a node.

##### Create and Run a Named Action

The following code creates and runs a new action identified with the `ignition` key.

The following key-based methods are available:

- [`run(_:withKey:)`](sknode/run(_:withkey:).md) method to run the action. If an action with the same key is already executing, it is removed before the new action is added.
- [`action(forKey:)`](sknode/action(forkey:).md) method to determine if an action with that key is already running.
- [`removeAction(forKey:)`](sknode/removeaction(forkey:).md) method to remove the action.

##### Find and Replace an in Flight Action

The code below shows how you use a name to replace an action that’s currently running. The code determines where a mouse click occurred and then runs an action that moves a sprite to the click location. The action duration is calculated ahead of time to move the sprite at a fixed speed. Because this code uses [`run(_:withKey:)`](sknode/run(_:withkey:).md), any previous move that’s still executing is stopped and replaced by the new action with the same name.

```swift
override func mouseDown(with event: NSEvent) {
	guard let playerNodeParent = self.playerNode.parent else { return }

	let clickPoint = event.location(in: playerNodeParent)

	let charPos = playerNode.position

	let distance = hypot(clickPoint.x-charPos.x, 
		clickPoint.y-charPos.y)

	let moveToClick = SKAction.move(to: clickPoint, 
		duration: TimeInterval(distance / characterSpeed))

	self.playerNode.run(moveToClick, withKey: "moveToClick")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/controlling-actions-precisely-by-using-names)*