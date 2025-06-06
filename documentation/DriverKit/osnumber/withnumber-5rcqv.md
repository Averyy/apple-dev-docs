# withNumber

**Framework**: DriverKit  
**Kind**: method

Allocates an OSNumber object with value and size.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSNumberPtr withNumber(uint64_t value, size_t numberOfBits);
```

#### Return Value

NULL on failure, otherwise the allocated OSNumber with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSNumber object with value and size.

## Parameters

- `value`: Value the OSNumber holds.
- `numberOfBits`: Size of the value. Only 8, 16, 32, or 64 are valid sizes.

## See Also

- [withNumber](osnumber/withnumber-2c6oe.md)
  Allocates an OSNumber object with value from a c-string and size.
- [OSNumberCreateWithUInt64Value](osnumbercreatewithuint64value.md)
- [free](osnumber/free.md)
- [OSNumberPtr](osnumberptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osnumber/withnumber-5rcqv)*