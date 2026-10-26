# CopyFromStorage

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
int (*)(const struct AudioServerPlugInHostInterface *, const struct __CFString *, const void **) CopyFromStorage;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

This method will fetch the data associated with the named storage key.

## Parameters

- `inHost`: The AudioServerPlugInHostRef passed to the plug-in at initialization.
- `inKey`: A CFStringRef that contains the name of the key whose data is to be fetched. Note that the Host will make sure that the keys for one plug-in do not collide with the keys for other plug-ins.
- `outData`: The data associated with the named storage key in the form of CFPropertyList. The caller is responsible for releasing the returned CFObject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface/copyfromstorage)*