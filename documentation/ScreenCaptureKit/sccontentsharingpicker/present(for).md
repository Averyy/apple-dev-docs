# present(for:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Displays the picker with an already running capture stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
func present(for stream: SCStream)
```

```objc
- (void) presentPickerForStream:(SCStream *) stream;
```

## Parameters

- `stream`: The capture stream to display in the picker.

## See Also

### Picker display
- [func present()](./present%28%29.md)
  Displays the picker with no active selection for capture.
- [func present(using: SCShareableContentStyle)](./present%28using%29.md)
  Displays the picker for a single type of capture selection.
- [func present(for: SCStream, using: SCShareableContentStyle)](./present%28for,using%29.md)
  Displays the picker with an existing capture stream, allowing for a single type of capture selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/present(for:))*