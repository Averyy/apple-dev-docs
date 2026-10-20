# present(using:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Displays the picker for a single type of capture selection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func present(using contentStyle: SCShareableContentStyle)
```

```objc
- (void) presentPickerUsingContentStyle:(SCShareableContentStyle) contentStyle;
```

## Parameters

- `contentStyle`: The type of streaming content selection allowed through the presented picker.

## See Also

### Picker display
- [func present()](./present%28%29.md)
  Displays the picker with no active selection for capture.
- [func present(for: SCStream)](./present%28for%29.md)
  Displays the picker with an already running capture stream.
- [func present(for: SCStream, using: SCShareableContentStyle)](./present%28for,using%29.md)
  Displays the picker with an existing capture stream, allowing for a single type of capture selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/present(using:))*