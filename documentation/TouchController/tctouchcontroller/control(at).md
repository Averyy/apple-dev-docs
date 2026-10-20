# control(at:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

The control at the specified point, if any.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func control(at point: CGPoint) -> (any TCControl)?
```

```objc
- (id<TCControl>) controlAtPoint:(CGPoint) point;
```

#### Return Value

The control at the specified point, or `nil` if no control is found.

## Parameters

- `point`: The point to check for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/control(at:))*