# format

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

A pointer to the first attribute format in the array.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var format: UnsafeMutablePointer<UInt32>?
```

```c
UInt32 * format;
```

## Discussion

Attribute formats are of type `CSSM_DB_ATTRIBUTE_FORMAT` (`CSSM_DB_ATTRIBUTE_FORMAT_STRING`, for example), and are defined in the `cssmtype.h` header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainattributeinfo/format)*