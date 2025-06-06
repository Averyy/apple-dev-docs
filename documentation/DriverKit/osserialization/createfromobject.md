# createFromObject

**Framework**: DriverKit  
**Kind**: method

Allocates an OSSerialization object with the serialized data of an object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSerializationPtr createFromObject(OSObjectPtr const object);
```

#### Return Value

NULL on failure, otherwise the allocated OSSerialization with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSSerialization object with the serialized data of an object.

## Parameters

- `object`: Object to serialize. Only certain DriverKit classes may be serialized: OSData, OSString, OSNumber, OSBoolean, OSArray, OSDictionary.

## See Also

- [createFromBytes](osserialization/createfrombytes.md)
  Allocates an OSSerialization object from the serialized data of a previous serialization.
- [OSCreateSerializationFromBytes](oscreateserializationfrombytes.md)
- [OSCreateSerializationFromObject](oscreateserializationfromobject.md)
- [free](osserialization/free.md)
- [OSSerializationFreeBufferHandler](osserializationfreebufferhandler.md)
- [OSSerializationPtr](osserializationptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/createfromobject)*