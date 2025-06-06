# finalizeBuffer

**Framework**: DriverKit  
**Kind**: method

Obtain the result of the serialization performed by createFromObject().

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
const void * finalizeBuffer(size_t * length);
```

#### Return Value

NULL on failure, otherwise a pointer to the serialization data. It is valid only while the OSSerialization object is retained.

#### Discussion

Obtain the result of the serialization performed by createFromObject().

## Parameters

- `length`: The length of the serialization data.

## See Also

- [copyObject](osserialization/copyobject.md)
  Obtain the result of the deserialization performed by createFromBytes().
- [OSCreateObjectFromSerialization](oscreateobjectfromserialization.md)
- [OSSerializationGetBytes](osserializationgetbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/finalizebuffer)*