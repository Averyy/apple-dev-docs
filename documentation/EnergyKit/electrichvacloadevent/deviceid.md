# deviceID

**Framework**: EnergyKit  
**Kind**: property

The device’s unique stable identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let deviceID: String
```

#### Discussion

The max length is `64 UTF-8` bytes. UUID strings are permitted. The following are enforced as preconditions:

- Isn’t empty, and less than or equal to 64 UTF-8 bytes.
- Uses only alphanumeric, space, hyphen, and apostrophe characters.
- Starts and ends with an alphanumeric character.

## See Also

- [var deviceName: String](electrichvacloadevent/devicename.md)
  A human-readable name for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/deviceid)*