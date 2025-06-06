# present(using:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Displays the picker for a single type of capture selection.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
func present(using contentStyle: SCShareableContentStyle)
```

## Parameters

- `contentStyle`: The type of streaming content selection allowed through the presented picker.

## See Also

- [func present()](sccontentsharingpicker/present.md)
  Displays the picker with no active selection for capture.
- [func present(for: SCStream)](sccontentsharingpicker/present(for:).md)
  Displays the picker with an already running capture stream.
- [func present(for: SCStream, using: SCShareableContentStyle)](sccontentsharingpicker/present(for:using:).md)
  Displays the picker with an existing capture stream, allowing for a single type of capture selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/present(using:))*