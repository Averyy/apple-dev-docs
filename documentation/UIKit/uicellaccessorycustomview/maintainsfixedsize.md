# maintainsFixedSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to preserve the frame size of the custom view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) BOOL maintainsFixedSize;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the system preserves the current frame size of the view. When the value of this property is [`false`](../../Swift/false.md), the system sizes the view during layout of the accessories.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Accessing Configuration Options
- [customView](./customview.md)
  The custom view to display for the accessory.
- [placement](./placement.md)
  The placement for the accessory.
- [position](./position.md)
  The index position of the cell accessory in relation to the other accessories in the accessories array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessorycustomview/maintainsfixedsize)*