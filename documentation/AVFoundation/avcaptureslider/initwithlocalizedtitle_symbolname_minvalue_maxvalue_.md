# initWithLocalizedTitle:symbolName:minValue:maxValue:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a continuous slider control that selects a value from a bounded range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```objc
- (instancetype) initWithLocalizedTitle:(NSString *) localizedTitle symbolName:(NSString *) symbolName minValue:(float) minValue maxValue:(float) maxValue;
```

## Discussion

Use continuous sliders when your use case supports selecting any value in the specified range.

## Parameters

- `localizedTitle`: A localized title that describes the slider’s action.
- `symbolName`: A symbol name from the SF Symbols library.
- `minValue`: The lower bound of the range.
- `maxValue`: The upper bound of the range.

## See Also

### Creating a slider
- [- initWithLocalizedTitle:symbolName:minValue:maxValue:step:](./initwithlocalizedtitle_symbolname_minvalue_maxvalue_step_.md)
  Creates a discrete slider control that selects a stepped value from a bounded range.
- [- initWithLocalizedTitle:symbolName:values:](./initwithlocalizedtitle_symbolname_values_.md)
  Creates a discrete slider control that selects a value from a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:minvalue:maxvalue:)*