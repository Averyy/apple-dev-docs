# readOnly

**Framework**: Core Video  
**Kind**: property

A read-only buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var readOnly: CVPixelBufferLockFlags { get }
```

#### Discussion

Set this flag if you don’t plan to modify buffer data while holding the lock. Setting this flag improves performance by preventing Core Video from invalidating  existing caches of the buffer’s contents.

> ❗ **Important**:  If you pass this flag to the [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) function, you must also pass it to the [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags/readonly)*