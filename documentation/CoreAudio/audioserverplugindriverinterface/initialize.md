# Initialize

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
int (*)(struct AudioServerPlugInDriverInterface **, const struct AudioServerPlugInHostInterface *) Initialize;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

This method is called to initialize the instance of the plug-in.

As part of initialization, the plug-in should publish all the objects it knows about at the time.

## Parameters

- `inDriver`: The plug-in to initialize.
- `inHost`: An AudioServerPlugInHostInterface struct that the plug-in is to use for communication with the Host. The Host guarantees that the storage pointed to by inHost will remain valid for the lifetime of the plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/initialize)*