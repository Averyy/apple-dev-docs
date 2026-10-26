# DeleteFromStorage

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
int (*)(const struct AudioServerPlugInHostInterface *, const struct __CFString *) DeleteFromStorage;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

This method will remove the given key and any associated data from storage.

## Parameters

- `inHost`: The AudioServerPlugInHostRef passed to the plug-in at initialization.
- `inKey`: A CFStringRef that contains the name of the key to be deleted. Note that the Host will make sure that the keys for one plug-in do not collide with the keys for other plug-ins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface/deletefromstorage)*