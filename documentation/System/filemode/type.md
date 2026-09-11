# type

**Framework**: System  
**Kind**: property

The file’s type, from the mode’s file-type bits.

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
var type: FileType { get set }
```

#### Discussion

Setting this property will mask the `newValue` with the file-type bit mask `S_IFMT`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filemode/type)*