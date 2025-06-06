# init(_:symbolName:in:step:)

**Framework**: AVFoundation  
**Kind**: init

Creates a discrete slider control that selects a stepped value from a bounded range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
@nonobjc
convenience init(_ localizedTitle: String, symbolName: String, in range: ClosedRange<Float>, step: Float)
```

#### Discussion

Use discrete sliders when your use case supports selecting stepped values within the specified range.

## Parameters

- `localizedTitle`: A localized title that describes the slider’s action.
- `symbolName`: A symbol name from the SF Symbols library.
- `range`: A bounded range of floating point values.
- `step`: The distance between each valid value. This specified value must be greater than   or the system throws an  .

## See Also

- [convenience init(String, symbolName: String, in: ClosedRange<Float>)](avcaptureslider/init(_:symbolname:in:).md)
  Creates a continuous slider control that selects a value from a bounded range.
- [convenience init(String, symbolName: String, values: [Float])](avcaptureslider/init(_:symbolname:values:).md)
  Creates a discrete slider control that selects a value from a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/init(_:symbolname:in:step:))*