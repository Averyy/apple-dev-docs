# compositionPickerViewDidStartAnimating(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Performs custom tasks when the composition picker view starts animating a composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func compositionPickerViewDidStartAnimating(_ pickerView: QCCompositionPickerView!)
```

#### Discussion

Quartz Composer invokes  this method when  the composition picker view starts animating a composition. Implement this method if you want to perform custom tasks at that time.

## Parameters

- `pickerView`: The composition picker view in which the composition started animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionpickerviewdidstartanimating(_:))*