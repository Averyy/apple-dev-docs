# init(bytes:deallocator:)

**Framework**: Model I/O  
**Kind**: init

Initializes a buffer map object to manage access to the specified memory.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(bytes: UnsafeMutableRawPointer, deallocator: (() -> Void)? = nil)
```

#### Return Value

A new buffer map object.

## Parameters

- `bytes`: A pointer to the data buffer to be managed by the buffer map.
- `deallocator`: The block has no parameters and no return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap/init(bytes:deallocator:))*