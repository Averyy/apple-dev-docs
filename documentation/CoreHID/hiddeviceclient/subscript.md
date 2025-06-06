# subscript(_:)

**Framework**: Core HID  
**Kind**: subscript

Get or set a property from the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
subscript(key: String) -> HIDDeviceClient.UnsafeProperty? { get set }
```

#### Return Value

The value of the requested property, if any. The return type and value are device implementation specific.

#### Overview

Properties can be inherently present on the device, or set manually. Any number of properties can be valid or invalid and return varying types, depending on the device specific implementation. Properties are typically only for advanced use cases when it’s known exactly what is returned when queried, or exactly what happens when set for a specific device.

Note: These methods are unsafe, as the returned type is unchecked `Sendable` for possibly non-Sendable objects. Concurrency safety is the responsibility of the developer.

## Parameters

- `key`: The property to get or set. Supported properties are device implementation specific.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/subscript(_:))*