# setObjectThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setObjectThreadgroupMemoryLength:(NSUInteger) length atIndex:(NSUInteger) index;
```

## Parameters

- `length`: The threadgroup memory length, in bytes.
- `index`: An integer that represents an entry in the object argument table.

## See Also

### Configuring persistent threadgroup memory
- [func setThreadgroupMemoryLength(Int, offset: Int, index: Int)](./setthreadgroupmemorylength%28_,offset,index%29.md)
  Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectthreadgroupmemorylength(_:index:))*