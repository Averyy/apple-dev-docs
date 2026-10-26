# GetPropertyData

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, int, const struct AudioObjectPropertyAddress *, unsigned int, const void *, unsigned int, unsigned int *, void *) GetPropertyData;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Fetches the data of the given property and places it in the provided buffer.

## Parameters

- `inDriver`: The plug-in that owns the object.
- `inObjectID`: The object to query.
- `inClientProcessID`: A pid_t indicating the process of the client. Note that this will often be zero indicating that the Host is making the request.
- `inAddress`: An AudioObjectPropertyAddress indicating the property being queried.
- `inQualifierDataSize`: A UInt32 indicating the size of the buffer pointed to by inQualifierData. Note that not all properties require qualification, in which case this value will be 0.
- `inQualifierData,`: A buffer of data to be used in determining the data of the property being queried. Note that not all properties require qualification, in which case this value will be NULL.
- `inDataSize`: A UInt32 that indicates the size of the buffer pointed to by outData
- `outDataSize`: A UInt32 which on exit indicates how much of the buffer pointed to by outData was used.
- `outData`: The buffer into which the data for the given property will be put.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/getpropertydata)*