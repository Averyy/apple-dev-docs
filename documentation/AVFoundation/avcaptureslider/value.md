# value

**Framework**: AVFoundation  
**Kind**: property

The current value of the slider.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var value: Float { get set }
```

#### Discussion

The default value is the slider’s minimum value. You may set a value only if it’s within the slider’s minimum and maximum values, otherwise the system throws an exception.

> ❗ **Important**:  Only modify a slider’s value from the same dispatch queue that you specified in the control’s [`setActionQueue:action:`](avcaptureslider/setactionqueue:action:.md) method.

## See Also

- [var prominentValues: [Float]](avcaptureslider/prominentvalues-199dz.md)
  Values in this array may receive unique visual representations or behaviors.
- [var localizedValueFormat: String?](avcaptureslider/localizedvalueformat.md)
  A localized string that defines the presentation of the slider’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/value)*