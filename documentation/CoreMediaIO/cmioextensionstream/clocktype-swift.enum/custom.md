# CMIOExtensionStream.ClockType.custom

**Framework**: Core Media I/O  
**Kind**: case  
**Role**: Case

Indicates that the stream’s clock is specific to the device hosting the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
case custom
```

```c
CMIOExtensionStreamClockTypeCustom
```

#### Discussion

The extension doesn’t set this type directly. Instead, the system sets it automatically when you specify a [`CMIOExtensionStreamCustomClockConfiguration`](../../cmioextensionstreamcustomclockconfiguration.md) when you create a [`CMIOExtensionStream`](../../cmioextensionstream.md).

## See Also

### Clock Types
- [CMIOExtensionStream.ClockType.hostTime](./hosttime.md)
  Indicates that the stream uses the host time clock.
- [CMIOExtensionStream.ClockType.linkedCoreAudioDeviceUID](./linkedcoreaudiodeviceuid.md)
  Indicates that the stream uses the clock of the linked Core Audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/clocktype-swift.enum/custom)*