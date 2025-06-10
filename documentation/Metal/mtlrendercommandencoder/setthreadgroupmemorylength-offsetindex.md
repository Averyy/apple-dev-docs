# setThreadgroupMemoryLength(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, offset: Int, index: Int)
```

#### Discussion

You can only change the threadgroup memory’s size between tile dispatches (see [`dispatchThreadsPerTile(_:)`](mtlrendercommandencoder/dispatchthreadspertile(_:).md)).

> ❗ **Important**:  Exceeding the threadgroup memory allocation for the render pass can trigger a debug error.

## Parameters

- `length`: The threadgroup memory length, in bytes.
- `offset`: An integer that represents the location, in bytes, from the start of the buffer at   where the threadgroup memory begins.
- `index`: An integer that represents an entry in the buffer argument table.

## See Also

- [func setObjectThreadgroupMemoryLength(Int, index: Int)](mtlrendercommandencoder/setobjectthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for an entry in the object argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setthreadgroupmemorylength(_:offset:index:))*