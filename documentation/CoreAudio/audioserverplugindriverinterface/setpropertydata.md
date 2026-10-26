# SetPropertyData

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, int, const struct AudioObjectPropertyAddress *, unsigned int, const void *, unsigned int, const void *) SetPropertyData;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Tells an object to change the value of the given property.

Note that the value of the property cannot be considered set until the appropriate notification has been received by the Host.

## Parameters

- `inDriver`: The plug-in that owns the object.
- `inObjectID`: The object to change.
- `inClientProcessID`: A pid_t indicating the process of the client. Note that this will often be zero indicating that the Host is making the request.
- `inAddress`: An AudioObjectPropertyAddress indicating the property being changed.
- `inQualifierDataSize`: A UInt32 indicating the size of the buffer pointed to by inQualifierData. Note that not all properties require qualification, in which case this value will be 0.
- `inQualifierData,`: A buffer of data to be used in determining the data of the property being queried. Note that not all properties require qualification, in which case this value will be NULL.
- `inDataSize`: A UInt32 indicating the size of the buffer pointed to by inData.
- `inData`: The buffer containing the data for the property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/setpropertydata)*