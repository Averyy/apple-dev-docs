# ptpObjectHandle

**Framework**: ImageCaptureCore  
**Kind**: property

The item’s `PTP` object handle value, if the camera uses the `PTP` protocol.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var ptpObjectHandle: UInt32 { get }
```

#### Discussion

The value of this property is set to `0` if the camera does not use PTP protocol.

## See Also

- [var uti: String?](iccameraitem/uti.md)
  The item’s uniform type identifier (UTI) string.
- [var name: String?](iccameraitem/name.md)
  The item’s name.
- [var isRaw: Bool](iccameraitem/israw.md)
  A Boolean value indicating whether the item is a raw image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/ptpobjecthandle)*