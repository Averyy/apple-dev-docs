# type

**Framework**: System  
**Kind**: property

The file’s type, from the mode’s file-type bits.

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
var type: FileType { get set }
```

#### Discussion

Setting this property will mask the `newValue` with the file-type bit mask `S_IFMT`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filemode/type)*