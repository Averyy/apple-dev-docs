# writeBytes(_:count:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Copies the specified data bytes into the underlying Metal buffer for use by a shader.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func writeBytes(_ bytes: UnsafeRawPointer, count length: Int)
```

```objc
- (void) writeBytes:(const void *) bytes length:(NSUInteger) length;
```

## Parameters

- `bytes`: The memory address from which to copy data.
- `length`: The number of bytes to copy into the Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferstream/writebytes(_:count:))*