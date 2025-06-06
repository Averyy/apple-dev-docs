# writeBytes(_:count:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Copies the specified data bytes into the underlying Metal buffer for use by a shader.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func writeBytes(_ bytes: UnsafeRawPointer, count length: Int)
```

## Parameters

- `bytes`: The memory address from which to copy data.
- `length`: The number of bytes to copy into the Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferstream/writebytes(_:count:))*