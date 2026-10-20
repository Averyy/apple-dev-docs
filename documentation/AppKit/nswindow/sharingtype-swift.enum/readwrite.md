# readWrite

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

**Availability**:
- macOS 10.5+ - Deprecated in 15.0

> **Deprecated**: Use NSWindowSharingReadOnly instead

## Declaration

```swift
static var readWrite: NSWindow.SharingType { get }
```

```c
static const NSWindowSharingType NSWindowSharingReadWrite;
```

#### Discussion

The window’s contents can be read and modified by another process.

## See Also

### Constants
- [NSWindow.SharingType.none](./none.md)
  A legacy constant that macOS no longer uses.
- [NSWindow.SharingType.readOnly](./readonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sharingtype-swift.enum/readwrite)*