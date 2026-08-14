# current(for:)

**Framework**: AudioAccessoryKit  
**Kind**: method

Retrieves the accessory’s current configuration.

**Availability**:
- iOS 26.4+

## Declaration

```swift
static func current(for accessory: ASAccessory) throws -> AccessoryControlDevice
```

#### Return Value

The accessory’s current configuration.

#### Discussion

> ❗ **Important**: Call this method only from your app extension.

This method throws an error if the accessory isn’t registered, or if communication fails.

## Parameters

- `accessory`: The accessory for which to get the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/current(for:))*