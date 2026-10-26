# referenceMicroframeWithTime:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (uint64_t) referenceMicroframeWithTime:(IOUSBHostTime *) time error:(NSError **) error;
```

#### Return Value

A recent microframe number. Returns 0 on failure, with NSError populated with the IOReturn error code.

#### Discussion

Return a recent microframe number of the USB controller

This method will return a recent microframe number of the USB controller. This is most useful for scheduling future isochronous requests.

## Parameters

- `time`: If not nil, this will be updated with system time associated with the microframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/referencemicroframewithtime:error:)*