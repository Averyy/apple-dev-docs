# GetZeroTimeStamp

**Framework**: Core Audio  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, unsigned int, double *, unsigned long long *, unsigned long long *) __attribute__((nonblocking)) GetZeroTimeStamp;
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

Retrieves the most recent zero time stamp for the device.

Devices that do not provide their own clock do not need to implement this call.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The device whose zero time stamp is being requested.
- `inClientID`: The ID of the client making the request. This will have been established with the device by a previous call to AddDeviceClient().
- `outSampleTime`: Upon return, the sample time portion of the zero time stamp.
- `outHostTime`: Upon return, the host time portion of the zero time stamp.
- `outSeed`: Upon return, the current seed value for the device’s clock. If successive calls return different seed values, the caller will assume that the device’s clock has established a new time line and that the caller should resynchronize to the new state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/getzerotimestamp)*