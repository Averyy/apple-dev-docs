# init(_:retryOnInterrupt:)

**Framework**: System  
**Kind**: init

Creates a `Stat` struct from a `FileDescriptor`.

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
init(_ fd: FileDescriptor, retryOnInterrupt: Bool = true) throws(Errno)
```

#### Discussion

The corresponding C function is `fstat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/init(_:retryoninterrupt:))*