# compositionPickerView(_:didSelect:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Performs custom tasks when the selected composition in the composition picker view changes.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func compositionPickerView(_ pickerView: QCCompositionPickerView!, didSelect composition: QCComposition!)
```

```objc
- (void) compositionPickerView:(QCCompositionPickerView *) pickerView didSelectComposition:(QCComposition *) composition;
```

#### Discussion

Quartz Composer invokes this method when the selected composition in the composition picker view changes. Implement this method if you want to perform custom tasks at that time.

## Parameters

- `pickerView`: The composition picker view in which the selection changed.
- `composition`: The selected composition or `nil` if the previously selected composition is no longer selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionpickerview(_:didselect:))*