# init(_:retryOnInterrupt:)

**Framework**: System  
**Kind**: init

Creates a `Stat` struct from a `FileDescriptor`.

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
init(_ fd: FileDescriptor, retryOnInterrupt: Bool = true) throws(Errno)
```

#### Discussion

The corresponding C function is `fstat()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/init(_:retryoninterrupt:))*