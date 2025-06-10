# handleTouchBegan(at:index:)

**Framework**: Touch Controls  
**Kind**: method

Handles a touch began event at the specified point.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
func handleTouchBegan(at point: CGPoint, index: NSNumber) -> Bool
```

#### Return Value

`YES` if the touch was handled by a control; otherwise `NO`.

## Parameters

- `point`: The point where the touch began.
- `index`: An NSNumber representing a unique index for the touch


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tctouchcontroller/handletouchbegan(at:index:))*