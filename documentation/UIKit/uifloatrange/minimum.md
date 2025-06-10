# minimum

**Framework**: UIKit  
**Kind**: property

The minimum range of motion for sliding and pin attachments.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var minimum: CGFloat
```

#### Discussion

For sliding attachments, it represents the number of points to move along the axis of translation in the negative direction. For pin attachments, it represents the number of radians to rotate in the counter-clockwise direction. This value must be less than or equal to `0`.

## See Also

- [var maximum: CGFloat](uifloatrange/maximum.md)
  The maximum range of motion for sliding and pin attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifloatrange/minimum)*