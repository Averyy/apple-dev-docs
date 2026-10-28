# init(_:symbolName:in:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a continuous slider control that selects a value from a bounded range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
@nonobjc
convenience init(_ localizedTitle: String, symbolName: String, in range: ClosedRange<Float>)
```

## Discussion

Use continuous sliders when your use case supports selecting any value in the specified range.

## Parameters

- `localizedTitle`: A localized title that describes the slider’s action.
- `symbolName`: A symbol name from the SF Symbols library.
- `range`: A bounded range of floating point values.

## See Also

### Creating a slider
- [convenience init(String, symbolName: String, in: ClosedRange<Float>, step: Float)](./init%28_,symbolname,in,step%29.md)
  Creates a discrete slider control that selects a stepped value from a bounded range.
- [convenience init(String, symbolName: String, values: [Float])](./init%28_,symbolname,values%29.md)
  Creates a discrete slider control that selects a value from a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/init(_:symbolname:in:))*