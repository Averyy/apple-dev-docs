# createFromBytes

**Framework**: DriverKit  
**Kind**: method

Allocates an OSSerialization object from the serialized data of a previous serialization.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSerializationPtr createFromBytes(const void * bytes, size_t length, OSSerializationFreeBufferHandlerfreeBuffer);
```

#### Return Value

NULL on failure, otherwise the allocated OSSerialization with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSSerialization object from the serialized data of a previous serialization.

## Parameters

- `bytes`: The serialized data from a previous call to OSSerialization::finalizeBuffer().
- `length`: The length of the serialized data from a previous call to OSSerialization::finalizeBuffer().
- `freeBuffer`: A required block to be called when the OSSerialization is freed and the serialized data will no longer be accessed. Note that unserialized objects may retain the OSSerialization they were created from, so the OSSerialization will retain the data until they have been freed.

## See Also

- [createFromObject](osserialization/createfromobject.md)
  Allocates an OSSerialization object with the serialized data of an object.
- [OSCreateSerializationFromBytes](oscreateserializationfrombytes.md)
- [OSCreateSerializationFromObject](oscreateserializationfromobject.md)
- [free](osserialization/free.md)
- [OSSerializationFreeBufferHandler](osserializationfreebufferhandler.md)
- [OSSerializationPtr](osserializationptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/createfrombytes)*