# GetPropertyDataSize

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, int, const struct AudioObjectPropertyAddress *, unsigned int, const void *, unsigned int *) GetPropertyDataSize;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Queries an object to find the size of the data for the given property.

## Parameters

- `inDriver`: The plug-in that owns the object.
- `inObjectID`: The object to query.
- `inAddress`: An AudioObjectPropertyAddress indicating the property being queried.
- `inClientProcessID`: A pid_t indicating the process of the client. Note that this will often be zero indicating that the Host is making the request.
- `inQualifierDataSize`: A UInt32 indicating the size of the buffer pointed to by inQualifierData. Note that not all properties require qualification, in which case this value will be 0.
- `inQualifierData,`: A buffer of data to be used in determining the data of the property being queried. Note that not all properties require qualification, in which case this value will be NULL.
- `outDataSize`: A UInt32 indicating how many bytes the data for the given property occupies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/getpropertydatasize)*