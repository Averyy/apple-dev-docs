# Create

**Framework**: AudioDriverKit  
**Kind**: method

Allocates and initializes an instance of the audio device class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
static OSSharedPtr<IOUserAudioDevice> Create(IOUserAudioDriver * in_driver, bool in_supports_prewarming, OSString * in_device_uid, OSString * in_model_uid, OSString * in_manufacturer_uid, uint32_t in_zero_timestamp_period);
```

#### Return Value

A poiner to an [`IOUserAudioDevice`](iouseraudiodevice.md), if allocation and initialization succeeded.

#### Discussion

If you subclass [`IOUserAudioDevice`](iouseraudiodevice.md) to override this class’ behavior, don’t use [`Create`](iouseraudiodevice/create.md) to allocate and initialize the custom subclass.

## Parameters

- `in_driver`: The   that owns this object.
- `in_supports_prewarming`: A Boolean value that specifies if the device supports prewarming I/O.
- `in_device_uid`: A pointer to an   containing the device UID.
- `in_model_uid`: A pointer to an   containing the module UID.
- `in_manufacturer_uid`: A pointer to an   containing the manufacturer UID.
- `in_zero_timestamp_period`: A   whose value indicates the number of sample frames the host can expect between successive timestamps returned from  . In other words, if   returns a sample time of  , the host can expect that the next valid timestamp it receives will be  .

## See Also

- [init](iouseraudiodevice/init.md)
  Initializes an instance of the audio device class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/create)*