# stat(flags:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Creates a `Stat` struct for the file referenced by this `FilePath` using the given `Flags`.

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
func stat(flags: Stat.Flags, retryOnInterrupt: Bool = true) throws(Errno) -> Stat
```

#### Discussion

If `path` is relative, it is resolved against the current working directory.

The corresponding C function is `fstatat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/stat(flags:retryoninterrupt:))*