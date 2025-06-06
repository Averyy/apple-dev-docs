# HandleChangeCurrentStreamFormat

**Framework**: AudioDriverKit  
**Kind**: method

Tells the stream the format is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeCurrentStreamFormat(const IOUserAudioStreamBasicDescription * in_format);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetCurrentStreamFormat`](iouseraudiostream/setcurrentstreamformat.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_format`: The stream format to set, if possible, as an  .

## See Also

- [HandleChangeStreamIsActive](iouseraudiostream/handlechangestreamisactive.md)
  Tells the stream the activity state is changing.
- [DeviceSampleRateChanged](iouseraudiostream/devicesampleratechanged.md)
  Updates stream formats, in response to the owning audio device changing its sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/handlechangecurrentstreamformat)*