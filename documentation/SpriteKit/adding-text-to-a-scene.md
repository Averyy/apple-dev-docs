# Adding Text to a Scene

**Framework**: SpriteKit

Draw text in your scene, such as a health indicator or a “Game Over” banner, by using a label node.

#### Overview

Most apps need to display text at some point, and implementing it correctly yourself can take a significant amount of work. But the [`SKLabelNode`](sklabelnode.md) class does all of the work necessary to load fonts and create text for display.

Create a new label node by calling the [`labelNodeWithFontNamed:`](sklabelnode/labelnodewithfontnamed:.md) class method. Then configure the other label properties, especially the [`text`](sklabelnode/text.md) property. The size of a label node is determined implicitly by its [`fontName`](sklabelnode/fontname.md), [`fontSize`](sklabelnode/fontsize.md), and [`text`](sklabelnode/text.md) properties.

By default, the text label is centered horizontally on the label node’s origin, with the font’s baseline passing through the origin. The [`verticalAlignmentMode`](sklabelnode/verticalalignmentmode.md) and [`horizontalAlignmentMode`](sklabelnode/horizontalalignmentmode.md) properties can be used to adjust the label’s position relative to the origin. The following code demonstrates how to create a new text label.

**Swift**:

```swift
let winner = SKLabelNode(fontNamed: "Chalkduster")
winner.text = "You Win!"
winner.fontSize = 65
winner.fontColor = SKColor.green
winner.position = CGPoint(x: frame.midX, y: frame.midY)
   
addChild(winner)
```

**Obj-C**:

```objc
SKLabelNode *winner = [SKLabelNode labelNodeWithFontNamed:@"Chalkduster"];winner.text = @"You Win!";winner.fontSize = 65;
winner.fontColor = [SKColor greenColor];
winner.position = CGPointMake(CGRectGetMidX(self.frame),
                              CGRectGetMidY(self.frame));   
[self addChild:winner];
```

Whenever you change the label node’s properties, the label node is automatically updated the next time the scene is rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/adding-text-to-a-scene)*