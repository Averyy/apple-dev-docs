# HandleChangeCurrentStreamFormat

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the stream the format is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeCurrentStreamFormat(const IOUserAudioStreamBasicDescription *in_format);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The default implementation calls [`SetCurrentStreamFormat`](./setcurrentstreamformat.md) and returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) upon success.

## Parameters

- `in_format`: The stream format to set, if possible, as an `IOUserAudioStreamBasicDescription`.

## See Also

### Managing Stream Changes
- [HandleChangeStreamIsActive](./handlechangestreamisactive.md)
  Tells the stream the activity state is changing.
- [DeviceSampleRateChanged](./devicesampleratechanged.md)
  Updates stream formats, in response to the owning audio device changing its sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/handlechangecurrentstreamformat)*