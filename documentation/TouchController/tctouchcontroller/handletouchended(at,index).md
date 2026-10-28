# handleTouchEnded(at:index:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

Handles a touch ended event at the specified point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func handleTouchEnded(at point: CGPoint, index: Int) -> Bool
```

```objc
- (BOOL) handleTouchEndedAtPoint:(CGPoint) point index:(NSInteger) index;
```

## Return Value

`YES` if the touch was handled by a control, `NO` otherwise.

## Parameters

- `point`: The point where the touch ended.
- `index`: An integer representing a unique index for the touch

## See Also

### Handling a touch
- [func handleTouchBegan(at: CGPoint, index: Int) -> Bool](./handletouchbegan%28at,index%29.md)
  Handles a touch began event at the specified point.
- [func handleTouchMoved(at: CGPoint, index: Int) -> Bool](./handletouchmoved%28at,index%29.md)
  Handles a touch moved event at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/handletouchended(at:index:))*