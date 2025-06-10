# maximum

**Framework**: UIKit  
**Kind**: property

The maximum range of motion for sliding and pin attachments.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var maximum: CGFloat
```

#### Discussion

For sliding attachments, it represents the number of points to move along the axis of translation in the positive direction. For pin attachments, it represents the number of radians to rotate in the clockwise direction. This value must be greater than or equal to `0`.

## See Also

- [var minimum: CGFloat](uifloatrange/minimum.md)
  The minimum range of motion for sliding and pin attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifloatrange/maximum)*