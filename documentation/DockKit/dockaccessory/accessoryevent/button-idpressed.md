# DockAccessory.AccessoryEvent.button(id:pressed:)

**Framework**: DockKit  
**Kind**: case

A button press event on the dock accessory.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
case button(id: Int, pressed: Bool)
```

## Parameters

- `id`: A unique, vendor-specific identifier for the given button.
- `pressed`:   on button press down,   on button release up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/accessoryevent/button(id:pressed:))*