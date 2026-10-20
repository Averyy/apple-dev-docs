# CFStreamErrorDomain.custom

**Framework**: Core Foundation  
**Kind**: case  
**Role**: Case

The error code is a custom error code.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: These constants are returned by [`CFReadStreamGetError(_:)`](../cfreadstreamgeterror%28_%29.md) and [`CFWriteStreamGetError(_:)`](../cfwritestreamgeterror%28_%29.md); use [`CFReadStreamCopyError(_:)`](../cfreadstreamcopyerror%28_%29.md) and [`CFWriteStreamCopyError(_:)`](../cfwritestreamcopyerror%28_%29.md) instead.

## Declaration

```swift
case custom
```

```c
kCFStreamErrorDomainCustom
```

## See Also

### Constants
- [CFStreamErrorDomain.POSIX](./posix.md)
  The error code is an error code defined in `errno.h`.
- [CFStreamErrorDomain.macOSStatus](./macosstatus.md)
  The error is an OSStatus value defined in `MacErrors.h`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain/custom)*