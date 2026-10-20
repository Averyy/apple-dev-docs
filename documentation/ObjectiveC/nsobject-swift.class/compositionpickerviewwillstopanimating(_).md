# compositionPickerViewWillStopAnimating(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Performs custom tasks when the composition picker view stops animating a composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func compositionPickerViewWillStopAnimating(_ pickerView: QCCompositionPickerView!)
```

```objc
- (void) compositionPickerViewWillStopAnimating:(QCCompositionPickerView *) pickerView;
```

#### Discussion

Quartz Composer invokes  this method whenever the composition picker view stops animating a composition. Implement this method if you want to perform custom tasks at that time.

## Parameters

- `pickerView`: The composition picker view in which the composition stopped animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionpickerviewwillstopanimating(_:))*