# init(grantedCoherency:)

**Framework**: FSKit  
**Kind**: init

Creates an open-item result.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init(grantedCoherency: FSVolume.KernelCacheCoherencyType)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `grantedCoherency`: The [`FSVolume.KernelCacheCoherencyType`](fsvolume/kernelcachecoherencytype.md) granted by the module for this item.

## See Also

- [FSVolume.KernelCacheCoherencyType](fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsopenitemresult/init(grantedcoherency:))*