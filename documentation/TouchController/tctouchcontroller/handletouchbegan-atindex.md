# handleTouchBegan(at:index:)

**Framework**: Touch Controller  
**Kind**: method

Handles a touch began event at the specified point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func handleTouchBegan(at point: CGPoint, index: Int) -> Bool
```

#### Return Value

`YES` if the touch was handled by a control; otherwise `NO`.

## Parameters

- `point`: The point where the touch began.
- `index`: An integer representing a unique index for the touch

## See Also

- [func handleTouchEnded(at: CGPoint, index: Int) -> Bool](tctouchcontroller/handletouchended(at:index:).md)
  Handles a touch ended event at the specified point.
- [func handleTouchMoved(at: CGPoint, index: Int) -> Bool](tctouchcontroller/handletouchmoved(at:index:).md)
  Handles a touch moved event at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/handletouchbegan(at:index:))*