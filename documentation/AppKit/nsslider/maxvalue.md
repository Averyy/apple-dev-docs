# maxValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum value the slider can send to its target.

**Availability**:
- macOS

## Declaration

```swift
var maxValue: Double { get set }
```

```objc
@property double maxValue;
```

#### Discussion

The slider’s maximum value. A horizontal slider sends the maximum value when the knob is all the way to the trailing end of the bar. A vertical slider sends the maximum value when the knob is at the top.

## See Also

### Asking about the value limits
- [var minValue: Double](./minvalue.md)
  The minimum value the slider can send to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/maxvalue)*