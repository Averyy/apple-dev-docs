# init(_:symbolName:values:)

**Framework**: AVFoundation  
**Kind**: init

Creates a discrete slider control that selects a value from a list.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
@nonobjc
convenience init(_ localizedTitle: String, symbolName: String, values: [Float])
```

#### Discussion

Use discrete sliders when your app supports selecting from a specific list of values.

## Parameters

- `localizedTitle`: A localized title that describes the slider’s action.
- `symbolName`: A symbol name from the SF Symbols library.
- `values`: An array of floating-point values.

## See Also

- [convenience init(String, symbolName: String, in: ClosedRange<Float>)](avcaptureslider/init(_:symbolname:in:).md)
  Creates a continuous slider control that selects a value from a bounded range.
- [convenience init(String, symbolName: String, in: ClosedRange<Float>, step: Float)](avcaptureslider/init(_:symbolname:in:step:).md)
  Creates a discrete slider control that selects a stepped value from a bounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/init(_:symbolname:values:))*