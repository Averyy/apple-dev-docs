# toolPickerIsRulerActiveDidChange(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Tells the observer when a person shows or hides the ruler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func toolPickerIsRulerActiveDidChange(_ toolPicker: PKToolPicker)
```

```objc
- (void) toolPickerIsRulerActiveDidChange:(PKToolPicker *) toolPicker;
```

## Parameters

- `toolPicker`: The tool picker whose configuration changed.

## See Also

### Detecting tool configuration changes
- [func toolPickerSelectedToolItemDidChange(PKToolPicker)](./toolpickerselectedtoolitemdidchange%28_%29.md)
  Tells the observer when a person selects a new tool item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerobserver/toolpickerisruleractivedidchange(_:))*