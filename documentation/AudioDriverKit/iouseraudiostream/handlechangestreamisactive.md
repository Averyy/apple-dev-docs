# HandleChangeStreamIsActive

**Framework**: AudioDriverKit  
**Kind**: method

Tells the stream the activity state is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeStreamIsActive(bool in_is_active);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetStreamIsActive`](iouseraudiostream/setstreamisactive.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_is_active`:   if the stream is to become active; otherwise,  .

## See Also

- [HandleChangeCurrentStreamFormat](iouseraudiostream/handlechangecurrentstreamformat.md)
  Tells the stream the format is changing.
- [DeviceSampleRateChanged](iouseraudiostream/devicesampleratechanged.md)
  Updates stream formats, in response to the owning audio device changing its sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/handlechangestreamisactive)*