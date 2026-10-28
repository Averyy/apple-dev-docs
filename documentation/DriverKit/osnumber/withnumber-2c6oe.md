# withNumber

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

Allocates an OSNumber object with value from a c-string and size.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static OSNumberPtr withNumber(const char *valueString, size_t numberOfBits);
```

## Return Value

NULL on failure, otherwise the allocated OSNumber with reference count 1 to be released by the caller.

## Discussion

Allocates an OSNumber object with value from a c-string and size.

## Parameters

- `valueString`: A c-string which will be parsed with strtoll(,,0).
- `numberOfBits`: Size of the value. Only 8, 16, 32, or 64 are valid sizes.

## See Also

### Creating a Number Object
- [withNumber](./withnumber-5rcqv.md)
  Allocates an OSNumber object with value and size.
- [OSNumberCreateWithUInt64Value](../osnumbercreatewithuint64value.md)
- [free](./free.md)
- [OSNumberPtr](../osnumberptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osnumber/withnumber-2c6oe)*