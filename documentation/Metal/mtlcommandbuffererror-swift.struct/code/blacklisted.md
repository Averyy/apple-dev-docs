# MTLCommandBufferError.Code.blacklisted

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A former error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0 (renamed: MTLCommandBufferError.accessRevoked)
- iPadOS 8.0+ - Deprecated in 16.0 (renamed: MTLCommandBufferError.accessRevoked)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: MTLCommandBufferError.accessRevoked)
- macOS 10.11+ - Deprecated in 13.0 (renamed: MTLCommandBufferError.accessRevoked)
- tvOS - Deprecated in 16.0 (renamed: MTLCommandBufferError.accessRevoked)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MTLCommandBufferError.accessRevoked)

> **Deprecated**: Use [`accessRevoked`](./accessrevoked.md) instead.

## Declaration

```swift
case blacklisted
```

```c
MTLCommandBufferErrorBlacklisted
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/code/blacklisted)*