# init(length:value:)

**Framework**: GSS  
**Kind**: init  
**Role**: Initializer

Initialize a new buffer with the given array of elements.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(length: Int, value: UnsafeMutableRawPointer!)
```

## Parameters

- `length`: The number of elements in the new buffer.
- `value`: A pointer to the array of elements to be included in the new buffer.

## See Also

### Initialization
- [init()](./init%28%29.md)
  Initialize a new, empty buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_buffer_desc_struct/init(length:value:))*