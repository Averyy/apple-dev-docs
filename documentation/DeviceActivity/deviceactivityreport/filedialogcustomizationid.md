# fileDialogCustomizationID(_:)

**Framework**: DeviceActivity  
**Kind**: method

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileDialogCustomizationID(_ id: String) -> some View
```

#### Discussion

Among other parameters, it stores the current directory, view style (e.g., Icons, List, Columns), recent places, and expanded window size. It enables a refined user experience; for example, when importing an image, the user might switch to the Icons view, but the List view could be more convenient in another context. The file dialog stores these settings and applies them every time before presenting the panel. If not provided, on every launch, the file dialog uses the default configuration.

## Parameters

- `id`: An identifier of the configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/filedialogcustomizationid(_:))*