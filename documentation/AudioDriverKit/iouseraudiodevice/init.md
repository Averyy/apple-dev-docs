# init

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes an instance of the audio device class.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual bool init(IOUserAudioDriver *in_driver, bool in_supports_prewarming, OSString *in_device_uid, OSString *in_model_uid, OSString *in_manufacturer_uid, uint32_t in_zero_timestamp_period);
```

#### Return Value

`true` if initialization succeeded; `false` otherwise.

## Parameters

- `in_driver`: The [`IOUserAudioDriver`](../iouseraudiodriver.md) that owns this object.
- `in_supports_prewarming`: A Boolean value that specifies whether the device supports prewarming I/O.
- `in_device_uid`: A pointer to an [`OSString`](../../DriverKit/osstring.md) containing the device UID.
- `in_model_uid`: A pointer to an [`OSString`](../../DriverKit/osstring.md) containing the module UID.
- `in_manufacturer_uid`: A pointer to an [`OSString`](../../DriverKit/osstring.md) containing the manufacturer UID.
- `in_zero_timestamp_period`: A [`uint32_t`](../../kernel/uint32_t.md) whose value indicates the number of sample frames the host can expect between successive timestamps returned from `GetZeroTimeStamp()`. In other words, if `GetZeroTimeStamp()` returns a sample time of `x`, the host can expect that the next valid timestamp it receives will be `x + in_zero_timestamp_period`.

## See Also

### Creating an Audio Device
- [Create](./create.md)
  Allocates and initializes an instance of the audio device class.
- [IOUserAudioDriver](../iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/init)*