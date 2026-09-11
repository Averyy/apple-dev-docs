# type

**Framework**: System  
**Kind**: property

File type for the given mode

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

> **Note**: This property is equivalent to `mode.type`. Modifying this property will update the underlying `st_mode` accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/type)*