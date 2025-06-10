# control(at:)

**Framework**: Touch Controls  
**Kind**: method

The control at the specified point, if any.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
func control(at point: CGPoint) -> (any TCControl)?
```

#### Return Value

The control at the specified point, or `nil` if no control is found.

## Parameters

- `point`: The point to check for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tctouchcontroller/control(at:))*