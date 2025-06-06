# localizedValueFormat

**Framework**: AVFoundation  
**Kind**: property

A localized string that defines the presentation of the slider’s value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var localizedValueFormat: String? { get set }
```

#### Discussion

Specify a format string to modify the presentation of a slider’s value. The format string may only contain `%@` and no other placeholders like `%d`, `%s`, and so on. Setting an Invalid format string results in the value’s default presentation.

Examples of valid format strings are:

- “%@%” for “40%”
- “%@ fps” for “60 fps”
- “+ %@” for “+ 20”

## See Also

- [var value: Float](avcaptureslider/value.md)
  The current value of the slider.
- [var prominentValues: [Float]](avcaptureslider/prominentvalues-199dz.md)
  Values in this array may receive unique visual representations or behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/localizedvalueformat)*