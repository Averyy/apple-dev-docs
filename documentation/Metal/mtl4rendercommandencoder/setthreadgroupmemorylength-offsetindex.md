# setThreadgroupMemoryLength(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, offset: Int, index: Int)
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes.
- `offset`: An integer that represents the location, in bytes, from the start of the threadgroup memory buffer   at   where the threadgroup memory begins.
- `index`: An integer that corresponds to the index of the argument you annotate with attribute    in the shader function.

## See Also

- [func setObjectThreadgroupMemoryLength(Int, index: Int)](mtl4rendercommandencoder/setobjectthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setthreadgroupmemorylength(_:offset:index:))*