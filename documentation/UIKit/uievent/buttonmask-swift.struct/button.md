# button(_:)

**Framework**: UIKit  
**Kind**: method

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

## Parameters

- `buttonNumber`: The index of the button on the input device. Pass `1` to represent [`primary`](uievent/buttonmask-swift.struct/primary.md), and `2` to represent [`secondary`](uievent/buttonmask-swift.struct/secondary.md).

## See Also

- [init(rawValue: Int)](uievent/buttonmask-swift.struct/init(rawvalue:).md)
  Creates a button mask with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/buttonmask-swift.struct/button(_:))*