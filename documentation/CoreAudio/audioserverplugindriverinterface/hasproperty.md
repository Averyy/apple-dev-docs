# HasProperty

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
unsigned char (*)(struct AudioServerPlugInDriverInterface **, unsigned int, int, const struct AudioObjectPropertyAddress *) HasProperty;
```

#### Return Value

A Boolean indicating whether or not the object has the given property.

#### Discussion

Queries an object about whether or not it has the given property.

## Parameters

- `inDriver`: The plug-in that owns the object.
- `inObjectID`: The object to query.
- `inClientProcessID`: A pid_t indicating the process of the client. Note that this will often be zero indicating that the Host is making the request.
- `inAddress`: An AudioObjectPropertyAddress indicating the property being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/hasproperty)*