# init(grantedCoherency:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates an open-item result.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(grantedCoherency: FSVolume.KernelCacheCoherencyType)
```

```objc
- (instancetype) initWithGrantedCoherency:(FSKernelCacheCoherencyType) grantedCoherency;
```

## Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `grantedCoherency`: The [`FSVolume.KernelCacheCoherencyType`](../fsvolume/kernelcachecoherencytype.md) granted by the module for this item.

## See Also

### Creating an open-item result
- [FSVolume.KernelCacheCoherencyType](../fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsopenitemresult/init(grantedcoherency:))*