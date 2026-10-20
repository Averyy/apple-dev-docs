# color

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The color of the ink.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var color: UIColor { get }
```

*macOS*

```swift
var color: NSColor { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@property (nonatomic, readonly) UIColor * color;
```

*macOS*

```objc
@property (nonatomic, readonly) NSColor * color;
```

#### Discussion

The alpha of the final color may vary due to input from Apple Pencil. For example, light pressure from Apple Pencil introduces more transparency into the final color, while additional force increases opacity to create a more solid line.

## See Also

### Getting the inking tool attributes
- [var width: CGFloat](./width.md)
  The base line width for new content.
- [var ink: PKInk](./ink.md)
  The ink that this tool creates strokes with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/color)*