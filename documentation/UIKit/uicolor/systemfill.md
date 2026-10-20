# systemFill

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An overlay fill color for thin and small shapes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class var systemFill: UIColor { get }
```

```objc
@property (class, nonatomic, readonly) UIColor * systemFillColor;
```

#### Discussion

Use system fill colors for items situated on top of an existing background color. System fill colors incorporate transparency to allow the background color to show through.

Use this color to fill thin or small shapes, such as the track of a slider.

## See Also

### Fill colors
- [class var secondarySystemFill: UIColor](./secondarysystemfill.md)
  An overlay fill color for medium-size shapes.
- [class var tertiarySystemFill: UIColor](./tertiarysystemfill.md)
  An overlay fill color for large shapes.
- [class var quaternarySystemFill: UIColor](./quaternarysystemfill.md)
  An overlay fill color for large areas that contain complex content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/systemfill)*