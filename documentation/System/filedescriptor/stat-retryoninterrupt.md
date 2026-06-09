# stat(retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Creates a `Stat` struct for the file referenced by this `FileDescriptor`.

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
func stat(retryOnInterrupt: Bool = true) throws(Errno) -> Stat
```

#### Discussion

The corresponding C function is `fstat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/stat(retryoninterrupt:))*