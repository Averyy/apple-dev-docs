# OSCreateSerializationFromBytes

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSSerializationPtr OSCreateSerializationFromBytes(const void * bytes, size_t length, OSSerializationFreeBufferHandlerfreeBuffer);
```

## See Also

- [createFromBytes](osserialization/createfrombytes.md)
  Allocates an OSSerialization object from the serialized data of a previous serialization.
- [createFromObject](osserialization/createfromobject.md)
  Allocates an OSSerialization object with the serialized data of an object.
- [OSCreateSerializationFromObject](oscreateserializationfromobject.md)
- [free](osserialization/free.md)
- [OSSerializationFreeBufferHandler](osserializationfreebufferhandler.md)
- [OSSerializationPtr](osserializationptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/oscreateserializationfrombytes)*