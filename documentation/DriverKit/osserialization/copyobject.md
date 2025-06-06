# copyObject

**Framework**: DriverKit  
**Kind**: method

Obtain the result of the deserialization performed by createFromBytes().

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSObjectPtr copyObject();
```

#### Return Value

NULL on failure, otherwise the allocated OSObject with reference count 1 to be released by the caller.

#### Discussion

Obtain the result of the deserialization performed by createFromBytes().

## See Also

- [OSCreateObjectFromSerialization](oscreateobjectfromserialization.md)
- [OSSerializationGetBytes](osserializationgetbytes.md)
- [finalizeBuffer](osserialization/finalizebuffer.md)
  Obtain the result of the serialization performed by createFromObject().


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/copyobject)*