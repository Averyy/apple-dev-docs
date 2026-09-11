# init(_:flags:retryOnInterrupt:)

**Framework**: System  
**Kind**: init

Creates a `Stat` struct from a `FilePath` and `Flags`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ path: FilePath, flags: Stat.Flags, retryOnInterrupt: Bool = true) throws(Errno)
```

#### Discussion

If `path` is relative, it is resolved against the current working directory.

The corresponding C function is `fstatat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/init(_:flags:retryoninterrupt:)-349q0)*