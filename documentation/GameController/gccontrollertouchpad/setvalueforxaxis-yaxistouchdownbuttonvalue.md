# setValueForXAxis(_:yAxis:touchDown:buttonValue:)

**Framework**: Game Controller  
**Kind**: method

Sets the input values of a snapshot of a touchpad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setValueForXAxis(_ xAxis: Float, yAxis: Float, touchDown: Bool, buttonValue: Float)
```

#### Discussion

This method does nothing if the associated controller isn’t a snapshot (its [`isSnapshot`](gccontroller/issnapshot.md) property is [`false`](https://developer.apple.com/documentation/swift/false)`)`.

## Parameters

- `xAxis`: A normalized value of the x-axis ranging from   to  .
- `yAxis`: A normalized value of the y-axis ranging from   to  .
- `touchDown`: A Boolean value that indicates whether the user starts touching the surface. If  , the user is touching the surface; otherwise, the user isn’t.
- `buttonValue`: A normalized number between   (minimum) and   (maximum) that represents the level of pressure the user applies to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/setvalueforxaxis(_:yaxis:touchdown:buttonvalue:))*