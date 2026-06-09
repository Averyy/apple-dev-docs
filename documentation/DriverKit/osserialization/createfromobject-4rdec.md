# createFromObject

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSerializationPtr createFromObject(OSObjectPtr const object, OSSerializationPortCopyOutHandler copyOutHandler);
```

#### Return Value

NULL on failure, otherwise the allocated OSSerialization with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSSerialization object with the serialized data of an object.

Allocates an OSSerialization object with the serialized data of an object.

## Parameters

- `object`: Object to serialize. Only certain DriverKit classes may be serialized: OSData, OSString, OSNumber, OSBoolean, OSArray, OSDictionary.
- `copyOutHandler`: An optional handler that allows an object to be replaced with a port name before being serialized


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/createfromobject-4rdec)*