# init(minimum:maximum:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a new float range structure from the given components.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
init(minimum: CGFloat, maximum: CGFloat)
```

```c
static UIFloatRange UIFloatRangeMake(CGFloat minimum, CGFloat maximum);
```

#### Discussion

Float ranges are used in [`UIAttachmentBehavior`](../uiattachmentbehavior.md) objects to define the maximum range of translation or rotation for animations.

## Parameters

- `minimum`: The minimum range value, which is typically less than or equal to `0`.
- `maximum`: The maximum range value, which is typically greater than or equal to `0`.

## See Also

### Creating a float range
- [UIFloatRangeInfinite](./infinite.md)
  A range whose range is minus infinity to infinity.
- [UIFloatRangeZero](./zero.md)
  A range whose minimum and maximum are both `0.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifloatrange/init(minimum:maximum:)-1vgoo)*