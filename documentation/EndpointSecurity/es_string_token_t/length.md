# length

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The size of the data buffer, in bytes.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var length: Int
```

```c
size_t length;
```

## Discussion

This value doesn’t include the null terminator.

## See Also

### Inspecting the Token
- [var data: UnsafePointer<CChar>!](./data.md)
  The string data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_string_token_t/length)*