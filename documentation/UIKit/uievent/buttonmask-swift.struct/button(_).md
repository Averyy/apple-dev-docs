# button(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a button mask from the specified button index.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
static func button(_ buttonNumber: Int) -> UIEvent.ButtonMask
```

```c
extern UIEventButtonMask UIEventButtonMaskForButtonNumber(NSInteger buttonNumber);
```

## Parameters

- `buttonNumber`: The index of the button on the input device. Pass `1` to represent [`primary`](./primary.md), and `2` to represent [`secondary`](./secondary.md).

## See Also

### Creating button masks
- [init(rawValue: Int)](./init%28rawvalue%29.md)
  Creates a button mask with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/buttonmask-swift.struct/button(_:))*