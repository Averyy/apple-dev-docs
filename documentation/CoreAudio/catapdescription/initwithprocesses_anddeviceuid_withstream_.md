# initWithProcesses:andDeviceUID:withStream:

**Framework**: Core Audio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
- (instancetype) initWithProcesses:(NSArray<NSNumber *> *) processesObjectIDsToIncludeInTap andDeviceUID:(NSString *) deviceUID withStream:(NSInteger) stream;
```

## Discussion

Mix all given process audio streams destined for the selected device stream

## Parameters

- `processesObjectIDsToIncludeInTap`: An NSArray of NSNumbers where each NSNumber holds an AudioObjectID of the process object to exclude from the tap. All other processes that output audio will be included in the tap.
- `deviceUID`: The device UID of the output device whose audio will be captured
- `stream`: NSInteger that represents the index of the stream on the device whose audio will be captured. The format of the tap will match the format of this stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/initwithprocesses:anddeviceuid:withstream:)*