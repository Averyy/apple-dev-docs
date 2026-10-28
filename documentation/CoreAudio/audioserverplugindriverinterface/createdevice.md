# CreateDevice

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
int (*)(struct AudioServerPlugInDriverInterface **, const struct __CFDictionary *, const struct AudioServerPlugInClientInfo *, unsigned int *) CreateDevice;
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

Tells the plug-in to create a new device based on the given description.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDescription`: A CFDictionaryRef that contains a description of the device to create.
- `inClientInfo`: A pointer to an AudioServerPlugInClientInfo structure describing the client creating the device. Note that the mClientID field will be set to kAudioServerPlugInHostClientID since the device hasn’t been created yet. The client info is passed here to give enough context to allow for the creation of private devices.
- `outDeviceObjectID`: On successful exit, this will contain the object ID of the newly created device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/createdevice)*