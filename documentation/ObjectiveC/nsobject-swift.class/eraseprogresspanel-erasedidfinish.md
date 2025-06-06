# eraseProgressPanel(_:eraseDidFinish:)

**Framework**: Objective-C Runtime  
**Kind**: method

Notification sent by the panel before display.

**Availability**:
- macOS ?+

## Declaration

```swift
func eraseProgressPanel(_ theErasePanel: DREraseProgressPanel!, eraseDidFinish erase: DRErase!) -> Bool
```

#### Discussion

This method allows the delegate to handle or modify the end-of-burn feedback performed by the progress panel. Return `YES` to indicate the delegate handled the burn completion and the standard feedback should be supressed. If this method returns `NO`, the normal end-of-burn handling is performed (displaying an error if appropriate, playing an “I’m done” sound, etc).

The delegate is messaged before the progress panel is ordered out so a sheet may be displayed on a progress panel displayed as a window.

## Parameters

- `theErasePanel`: The progress panel
- `erase`: The object that performed the erase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspanel(_:erasedidfinish:))*