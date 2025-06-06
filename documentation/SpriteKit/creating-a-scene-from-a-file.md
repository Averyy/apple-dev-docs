# Creating a Scene from a File

**Framework**: SpriteKit

Load a scene that you configure in Xcode’s scene editor.

#### Overview

The most common way to load an [`SKScene`](skscene.md) is through an `.sks` file configured in Xcode’s scene editor. Making your base changes in the editor is faster than writing equivalent initalization code, and it  avoids repeating code if you create a scene in multiple places.

##### Create a New Scene File

First, add a new scene file to your project through Xcode’s File menu > New… > File > (choose your platform tab) > SpriteKit Scene.

![Sceenshot showing the New File dialog in Xcode. Pick your target platform tab, then choose SpriteKit Scene.](https://docs-assets.developer.apple.com/published/2320dc70648fa6bef55200d8dd0c6329/media-3020351%402x.png)

##### Configure the Scene Using the Editor

You configure your scene in the scene editor by clicking on the `.sks` file in Xcode’s file navigator pane, then adjusting properties in the Utility pane. For example, to set your scene’s background color, follow the steps highlighted in the figure below:

1. Select the `.sks` file in the file navigator pane.
2. Open the Utilities pane.
3. Choose the Attributes inspector.
4. Define a color under Scene.

![Screenshot showing setting the scene background color in Xcode’s SpriteKit scene editor. You select the .sks file in Xcode’s file navigator pane, then choose the Attributes inspector tab within the Utilities pane. ](https://docs-assets.developer.apple.com/published/aaa7a35d5c134a80656a0c533de3ca69/media-3020360%402x.png)

##### Load the Scene in Code

Load the newly configured scene file in code using [`init(fileNamed:)`](sknode/init(filenamed:).md).

```swift
let scene = SKScene(fileNamed: "MyScene")
        
// Now present the scene in a view.
skView.presentScene(scene)
```

> **Note**:  The `.sks` file extension is left out of the `String` name argument to [`init(fileNamed:)`](sknode/init(filenamed:).md).

 The `.sks` file extension is left out of the `String` name argument to [`init(fileNamed:)`](sknode/init(filenamed:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-a-scene-from-a-file)*