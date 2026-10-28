# initWithLocalizedTitle:symbolName:values:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a discrete slider control that selects a value from a list.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```objc
- (instancetype) initWithLocalizedTitle:(NSString *) localizedTitle symbolName:(NSString *) symbolName values:(NSArray<NSNumber *> *) values;
```

## Discussion

Use discrete sliders when your app supports selecting from a specific list of values.

## Parameters

- `localizedTitle`: A localized title that describes the slider’s action.
- `symbolName`: A symbol name from the SF Symbols library.
- `values`: An array of floating-point values.

## See Also

### Creating a slider
- [- initWithLocalizedTitle:symbolName:minValue:maxValue:](./initwithlocalizedtitle_symbolname_minvalue_maxvalue_.md)
  Creates a continuous slider control that selects a value from a bounded range.
- [- initWithLocalizedTitle:symbolName:minValue:maxValue:step:](./initwithlocalizedtitle_symbolname_minvalue_maxvalue_step_.md)
  Creates a discrete slider control that selects a stepped value from a bounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/initwithlocalizedtitle:symbolname:values:)*