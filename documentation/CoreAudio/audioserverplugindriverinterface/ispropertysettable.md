# IsPropertySettable

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, int, const struct AudioObjectPropertyAddress *, unsigned char *) IsPropertySettable;
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

Queries an object about whether or not the given property can be set.

## Parameters

- `inDriver`: The plug-in that owns the object.
- `inObjectID`: The object to query.
- `inClientProcessID`: A pid_t indicating the process of the client. Note that this will often be zero indicating that the Host is making the request.
- `inAddress`: An AudioObjectPropertyAddress indicating the property being queried.
- `outIsSettable`: A Boolean indicating whether or not the property can be set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/ispropertysettable)*