# OSSerializationFreeBufferHandler

**Framework**: DriverKit  
**Kind**: typealias

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (^)(const void *, unsigned long) OSSerializationFreeBufferHandler;
```

## See Also

- [createFromBytes](osserialization/createfrombytes.md)
  Allocates an OSSerialization object from the serialized data of a previous serialization.
- [createFromObject](osserialization/createfromobject.md)
  Allocates an OSSerialization object with the serialized data of an object.
- [OSCreateSerializationFromBytes](oscreateserializationfrombytes.md)
- [OSCreateSerializationFromObject](oscreateserializationfromobject.md)
- [free](osserialization/free.md)
- [OSSerializationPtr](osserializationptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserializationfreebufferhandler)*