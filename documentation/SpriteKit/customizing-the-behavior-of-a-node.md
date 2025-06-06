# Customizing the Behavior of a Node

**Framework**: SpriteKit

Organize your app’s logic and display code with nodes.

#### Overview

Delegate tasks to specific nodes as a way to organize your app’s logic and display code. Learn which customization approach to take based on the particular behavior or look you want to enable.

##### Subclass a Node to Add Custom Behavior

Subclass [`SKNode`](sknode.md) (or one of its subclasses) when you need to customize the node’s look or behavior. For example, you might subclass [`SKNode`](sknode.md) to implement a custom drawing layer. Or, you might subclass [`SKSpriteNode`](skspritenode.md) to add some AI logic. If you want a node to respond to user input, you must subclass it. [`SKScene`](skscene.md) is a subclass of [`SKNode`](sknode.md), and you subclass [`SKScene`](skscene.md) to provide a custom look and behavior for your app.

###### Subclass a Node to Implement Node Archiving

If you add properties to a subclass and that subclass needs to be archived, the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol needs to be implemented on your subclasses. See [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

###### Use a Shader Instead of Subclassing to Do Custom Node Drawing

Unlike views, you cannot subclass [`SKNode`](sknode.md) to perform custom drawing. Instead, you use a node subclass that supports [`SKShader`](skshader.md) and implement your graphical effects in custom shader source code. Alternatively, you can composite a hierarchy of nodes that collectively effect the look you’re going for.

##### Add Custom Logic to a Node

In many cases, expect to add methods that can be called during the scene’s preprocessing and postprocessing steps. Your scene coordinates these steps, but focused node subclasses perform the work.

##### Handle User Input with a Node

If you want to implement event handling in a node class, you must implement separate event-handling code for iOS and macOS. The [`SKNode`](sknode.md) class inherits from [`NSResponder`](https://developer.apple.com/documentation/AppKit/NSResponder) on macOS and [`UIResponder`](https://developer.apple.com/documentation/UIKit/UIResponder) on iOS. See [`Controlling User Interaction on Nodes`](controlling-user-interaction-on-nodes.md) for more information.

##### Delegate Tasks to a Node

In some app designs, you can rely on the fact that a particular combination of classes is always going to be used together in a specific scene. In other designs, you may want to create classes that can be used in multiple scenes. When two classes are dependent on each other, use [`delegation`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14-SW1) to break that dependency. Most often, you do this by defining a delegate on your node and a protocol for delegates to implement. Your scene (or another node, such as the node’s parent) implements this protocol. Your node class can then be reused in multiple scenes, without needing to know the scene’s class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/customizing-the-behavior-of-a-node)*