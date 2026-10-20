# toolPickerSelectedToolDidChange(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Tells the observer when a person selects a new tool.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`toolPickerSelectedToolItemDidChange(_:)`](./toolpickerselectedtoolitemdidchange%28_%29.md) instead.

## Declaration

```swift
optional func toolPickerSelectedToolDidChange(_ toolPicker: PKToolPicker)
```

```objc
- (void) toolPickerSelectedToolDidChange:(PKToolPicker *) toolPicker;
```

## Parameters

- `toolPicker`: The tool picker whose configuration changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerobserver/toolpickerselectedtooldidchange(_:))*