# OSSerializationGetBytes

**Framework**: DriverKit  
**Kind**: func  
**Role**: Function

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
const void *OSSerializationGetBytes(OSSerializationPtr serial, size_t *length);
```

## See Also

### Getting the Serialized Content
- [copyObject](./osserialization/copyobject.md)
  Obtain the result of the deserialization performed by createFromBytes().
- [OSCreateObjectFromSerialization](./oscreateobjectfromserialization.md)
- [finalizeBuffer](./osserialization/finalizebuffer.md)
  Obtain the result of the serialization performed by createFromObject().


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserializationgetbytes)*