# setValueForXAxis(_:yAxis:)

**Framework**: Game Controller  
**Kind**: method

Sets the input values of a snapshot of a directional pad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setValueForXAxis(_ xAxis: Float, yAxis: Float)
```

#### Discussion

This method does nothing if the associated controller isn’t a snapshot (its [`isSnapshot`](gccontroller/issnapshot.md) property is [`false`](https://developer.apple.com/documentation/swift/false)`)`. Otherwise, this method sets the value of the direction pad’s buttons as well.

## Parameters

- `xAxis`: A normalized value of the x-axis ranging from   to  .
- `yAxis`: A normalized value for the y-axis ranging from   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/setvalueforxaxis(_:yaxis:))*