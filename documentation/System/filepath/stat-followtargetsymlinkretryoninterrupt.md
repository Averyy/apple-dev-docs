# stat(followTargetSymlink:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Creates a `Stat` struct for the file referenced by this `FilePath`.

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
func stat(followTargetSymlink: Bool = true, retryOnInterrupt: Bool = true) throws(Errno) -> Stat
```

#### Discussion

`followTargetSymlink` determines the behavior if `path` ends with a symbolic link. By default, `followTargetSymlink` is `true` and this initializer behaves like `stat()`. If `followTargetSymlink` is set to `false`, this initializer behaves like `lstat()` and returns information about the symlink itself.

The corresponding C function is `stat()` or `lstat()` as described above.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/stat(followtargetsymlink:retryoninterrupt:))*