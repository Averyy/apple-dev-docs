# init(grantedCoherency:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates an upgrade-item result.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(grantedCoherency: FSVolume.KernelCacheCoherencyType)
```

```objc
- (instancetype) initWithGrantedCoherency:(FSKernelCacheCoherencyType) grantedCoherency;
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `grantedCoherency`: The [`FSVolume.KernelCacheCoherencyType`](../fsvolume/kernelcachecoherencytype.md) granted by the module after the upgrade.

## See Also

### Creating an upgrade-item result
- [FSVolume.KernelCacheCoherencyType](../fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsupgradeitemresult/init(grantedcoherency:))*