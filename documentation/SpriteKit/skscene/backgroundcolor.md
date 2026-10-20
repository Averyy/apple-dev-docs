# backgroundColor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The background color of the scene.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var backgroundColor: UIColor { get set }
```

*macOS*

```swift
var backgroundColor: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain) UIColor * backgroundColor;
```

*macOS*

```objc
@property (nonatomic, retain) NSColor * backgroundColor;
```

## Mentions

- [Creating a Scene with a Transparent Background](../creating-a-scene-with-a-transparent-background.md)

#### Discussion

The default value is a gray color (RGBA `0.15, 0.15, 0.15, 1.0)`.

## See Also

### Setting the Background Appearance
- [Creating a Scene with a Transparent Background](../creating-a-scene-with-a-transparent-background.md)
  Set a transparent background color to show the content of the views below.
- [var view: SKView?](./view.md)
  The view that is currently presenting the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/backgroundcolor)*