# init(count:elements:)

**Framework**: GSS  
**Kind**: init

Initialize a new buffer set with the given buffers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(count: Int, elements: UnsafeMutablePointer<gss_buffer_desc>!)
```

## Parameters

- `count`: The number of buffers in the   array.
- `elements`: An array of buffers to be included in the new set.

## See Also

- [init()](gss_buffer_set_desc_struct/init.md)
  Initialize a new, empty buffer set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_buffer_set_desc_struct/init(count:elements:))*