# WriteToStorage

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
int (*)(const struct AudioServerPlugInHostInterface *, const struct __CFString *, const void *) WriteToStorage;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

This method will associate the given data with the named storage key, replacing any existing data.

Note that any data stored this way is persists beyond the life span of the Host including across rebooting.

## Parameters

- `inHost`: The AudioServerPlugInHostRef passed to the plug-in at initialization.
- `inKey`: A CFStringRef that contains the name of the key whose data is to be written. Note that the Host will make sure that the keys for one plug-in do not collide with the keys for other plug-ins.
- `inData`: A CFPropertyListRef containing the data to associate with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface/writetostorage)*