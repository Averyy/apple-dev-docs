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

## Discussion

A horizontal slider sends its maximum value when the knob is at the right end of the slider; a vertical slider sends it when the knob is at the top. The maximum selectable value for a circular slider is just below [`maxValue`](./maxvalue.md); for example, if [`maxValue`](./maxvalue.md) is 360, you can set the dial up to 359.999.

## See Also

### Managing Value Limits
- [var minValue: Double](./minvalue.md)
  The minimum value the slider can send to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/maxvalue)*