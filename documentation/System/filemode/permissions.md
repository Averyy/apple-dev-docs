# permissions

**Framework**: System  
**Kind**: property

The file’s permissions, from the mode’s permission bits.

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
var permissions: FilePermissions { get set }
```

#### Discussion

Setting this property will mask the `newValue` with the permissions bit mask `ALLPERMS`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filemode/permissions)*