# setObjectThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a threadgroup memory buffer for an entry in the object argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setObjectThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length`: The threadgroup memory length, in bytes.
- `index`: An integer that represents an entry in the object argument table.

## See Also

- [func setThreadgroupMemoryLength(Int, offset: Int, index: Int)](mtlrendercommandencoder/setthreadgroupmemorylength(_:offset:index:).md)
  Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectthreadgroupmemorylength(_:index:))*