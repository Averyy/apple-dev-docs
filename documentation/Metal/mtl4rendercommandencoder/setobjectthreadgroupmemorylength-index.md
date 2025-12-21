# setObjectThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setObjectThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes.
- `index`: An integer that corresponds to the index of the argument you annotate with attribute    in the shader function.

## See Also

- [func setThreadgroupMemoryLength(Int, offset: Int, index: Int)](mtl4rendercommandencoder/setthreadgroupmemorylength(_:offset:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setobjectthreadgroupmemorylength(_:index:))*