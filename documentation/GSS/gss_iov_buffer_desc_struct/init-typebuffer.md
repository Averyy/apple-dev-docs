# init(type:buffer:)

**Framework**: GSS  
**Kind**: init

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(type: OM_uint32, buffer: gss_buffer_desc)
```

#### Discussion

Initialize a new IOV buffer structure with the given configuration.

## Parameters

- `type`: The desired IOV buffer type.
- `buffer`: The buffer structure.

## See Also

- [init()](gss_iov_buffer_desc_struct/init.md)
  Initialize a new, empty IOV buffer structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_iov_buffer_desc_struct/init(type:buffer:))*