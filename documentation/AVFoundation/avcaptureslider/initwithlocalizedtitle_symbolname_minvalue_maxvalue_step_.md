# initWithLocalizedTitle:symbolName:minValue:maxValue:step:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a discrete slider control that selects a stepped value from a bounded range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```objc
- (instancetype) initWithLocalizedTitle:(NSString *) localizedTitle symbolName:(NSString *) symbolName minValue:(float) minValue maxValue:(float) maxValue step:(float) step;
```

#### Discussion

Use discrete sliders when your use case supports selecting stepped values within the specified range.

## Parameters

- `localizedTitle`: A localized title that describes the slider’s action.
- `symbolName`: A symbol name from the SF Symbols library.
- `minValue`: The lower bound of the range.
- `maxValue`: The upper bound of the range.
- `step`: The distance between each valid value. This specified value must be greater than `0` or the system throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md).

## See Also

### Creating a slider
- [- initWithLocalizedTitle:symbolName:minValue:maxValue:](./initwithlocalizedtitle_symbolname_minvalue_maxvalue_.md)
  Creates a continuous slider control that selects a value from a bounded range.
- [- initWithLocalizedTitle:symbolName:values:](./initwithlocalizedtitle_symbolname_values_.md)
  Creates a discrete slider control that selects a value from a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:minvalue:maxvalue:step:)*