# frameNumberWithTime:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Returns the current frame number of the USB controller.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (uint64_t) frameNumberWithTime:(IOUSBHostTime *) time;
```

## Return Value

The current frame number.

## Discussion

This method returns the current frame number of the USB controller, omitting the microframe. This is useful for scheduling future isochronous requests with [`enqueueIORequest(with:frameList:frameListCount:firstFrameNumber:completionHandler:)`](../iousbhostpipe/enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md) and [`sendIORequest(with:frameList:frameListCount:firstFrameNumber:)`](../iousbhostpipe/sendiorequest%28with,framelist,framelistcount,firstframenumber%29.md).

## Parameters

- `time`: An [`IOUSBHostTime`](../iousbhosttime.md) reference. If not `nil`, this updates with the current system time.

## See Also

### Getting Host Information
- [var deviceAddress: Int](./deviceaddress.md)
  The device’s bus address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/framenumberwithtime:)*