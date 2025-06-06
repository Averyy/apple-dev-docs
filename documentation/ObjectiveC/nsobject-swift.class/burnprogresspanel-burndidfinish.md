# burnProgressPanel(_:burnDidFinish:)

**Framework**: Objective-C Runtime  
**Kind**: method

Allows the delegate to handle the end-of-burn feedback.

**Availability**:
- macOS ?+

## Declaration

```swift
func burnProgressPanel(_ theBurnPanel: DRBurnProgressPanel!, burnDidFinish burn: DRBurn!) -> Bool
```

#### Return Value

 A `BOOL` indicating whether the normal end-of-burn feedback should occur.

#### Discussion

This method allows the delegate to handle or modify the end-of-burn feedback performed by the progress panel. Return `YES` to indicate the delegate handled the burn completion and the standard feedback should be supressed. If this method returns `NO`, the normal end-of-burn handling is performed (displaying an error if appropriate, playing an “I’m done” sound, etc).

The delegate is messaged before the progress panel is ordered out so a sheet may be displayed on a progress panel displayed as a window.

## Parameters

- `theBurnPanel`: The progress panel
- `burn`: The object that performed the burn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspanel(_:burndidfinish:))*