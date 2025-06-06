# uti

**Framework**: ImageCaptureCore  
**Kind**: property

The item’s uniform type identifier (UTI) string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var uti: String? { get }
```

#### Discussion

The `UTI` options are `kUTTypeFolder`, `kUTTypeImage`, `kUTTypeMovie`, `kUTTypeAudio`, or `kUTTypeData`.

## See Also

- [var name: String?](iccameraitem/name.md)
  The item’s name.
- [var ptpObjectHandle: UInt32](iccameraitem/ptpobjecthandle.md)
  The item’s `PTP` object handle value, if the camera uses the `PTP` protocol.
- [var isRaw: Bool](iccameraitem/israw.md)
  A Boolean value indicating whether the item is a raw image file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem/uti)*