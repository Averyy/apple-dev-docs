# SCNExportJavaScriptModule(_:)

**Framework**: SceneKit  
**Kind**: func

Makes SceneKit classes and global constants available to the specified JavaScript context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func SCNExportJavaScriptModule(_ context: JSContext)
```

#### Discussion

By controlling SceneKit using JavaScript code supplied at run time, you can enable rapid development for parts of your game or app. For example, a designer can easily experiment with visual effects or game-character behaviors without needing to compile and deploy your complete Xcode project.

This function exports all SceneKit classes and global constants, and all methods and properties on those classes, to JavaScript using the rules defined in the [`JSExport`](https://developer.apple.com/documentation/JavaScriptCore/JSExport) protocol. For example, the JavaScript code below performs various operations on a SceneKit node:

```javascript
var aNode = SCNNode.node();
aNode.opacity = 0.5;
aNode.removeFromParentNode();
// Animate an opacity change.
SCNTransaction.begin();
SCNTransaction.setAnimationDuration(1.0);
aNode.opacity = 0.5;
SCNTransaction.commit();
```

For SceneKit APIs that involve vectors and matrices, use JavaScript object syntax to define those values in terms of their elements:

```javascript
aNode.scale = {x:2, y:2, z:2};
aNode.transform = {m11:1, m12:0, m13:0, /*...*/ m44:1};
```

SceneKit also exports the following special JavaScript objects and functions:

| Objective-C / Swift class | JavaScript constructor |
| --- | --- |
| [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) / [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) | `SCNColor.color(r,g,b,a)` |
| [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) / [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) | `SCNImage.imageWithURL(aURL)` |
|  | `SCNImage.imageWithPath(aPath)` |
| [`CABasicAnimation`](https://developer.apple.com/documentation/QuartzCore/CABasicAnimation) | `CABasicAnimation.animationWithKeyPath(aPath)` |
| [`CAKeyframeAnimation`](https://developer.apple.com/documentation/QuartzCore/CAKeyframeAnimation) | `CAKeyframeAnimation.animationWithKeyPath(aPath)` |
| [`CAAnimationGroup`](https://developer.apple.com/documentation/QuartzCore/CAAnimationGroup) | `new CAAnimationGroup()` |
| [`CAMediaTimingFunction`](https://developer.apple.com/documentation/QuartzCore/CAMediaTimingFunction) | `CAMediaTimingFunction.functionWithName(name)` |


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnexportjavascriptmodule(_:))*