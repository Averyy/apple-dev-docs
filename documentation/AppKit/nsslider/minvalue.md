# minValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum value the slider can send to its target.

**Availability**:
- macOS

## Declaration

```swift
var minValue: Double { get set }
```

```objc
@property double minValue;
```

## Discussion

A horizontal slider sends the minimum value when the knob is all the way to the leading end of the bar. A vertical slider sends the minimum value when its knob is at the bottom.

## See Also

### Asking about the value limits
- [var maxValue: Double](./maxvalue.md)
  The maximum value the slider can send to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/minvalue)*