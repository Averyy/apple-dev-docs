# init(_:flags:retryOnInterrupt:)

**Framework**: System  
**Kind**: init

Creates a `Stat` struct from a `FilePath` and `Flags`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(_ path: FilePath, flags: Stat.Flags, retryOnInterrupt: Bool = true) throws(Errno)
```

#### Discussion

If `path` is relative, it is resolved against the current working directory.

The corresponding C function is `fstatat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/init(_:flags:retryoninterrupt:)-349q0)*