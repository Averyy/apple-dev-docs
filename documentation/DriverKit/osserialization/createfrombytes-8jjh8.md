# createFromBytes

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSerializationPtr createFromBytes(const void *bytes, size_t length, OSSerializationFreeBufferHandler freeBuffer, OSSerializationPortCopyInHandler copyInHandler);
```

#### Return Value

NULL on failure, otherwise the allocated OSSerialization with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSSerialization object from the serialized data of a previous serialization.

Allocates an OSSerialization object from the serialized data of a previous serialization.

## Parameters

- `bytes`: The serialized data from a previous call to OSSerialization::finalizeBuffer().
- `length`: The length of the serialized data from a previous call to OSSerialization::finalizeBuffer().
- `freeBuffer`: A required block to be called when the OSSerialization is freed and the serialized data will no longer be accessed. Note that unserialized objects may retain the OSSerialization they were created from, so the OSSerialization will retain the data until they have been freed.
- `copyInHandler`: An optional handler that allows a port number to be replaced with an OSObject instance during unserialization


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/createfrombytes-8jjh8)*