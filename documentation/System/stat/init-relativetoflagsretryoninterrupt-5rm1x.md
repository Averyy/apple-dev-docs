# init(_:relativeTo:flags:retryOnInterrupt:)

**Framework**: System  
**Kind**: init

Creates a `Stat` struct from an `UnsafePointer<CChar>` path and `Flags`, including a `FileDescriptor` to resolve a relative path.

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
init(_ path: UnsafePointer<CChar>, relativeTo fd: FileDescriptor, flags: Stat.Flags, retryOnInterrupt: Bool = true) throws(Errno)
```

#### Discussion

If `path` is absolute (starts with a forward slash), then `fd` is ignored. If `path` is relative, it is resolved against the directory given by `fd`.

The corresponding C function is `fstatat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/init(_:relativeto:flags:retryoninterrupt:)-5rm1x)*