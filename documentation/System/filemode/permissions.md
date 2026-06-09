# permissions

**Framework**: System  
**Kind**: property

The file’s permissions, from the mode’s permission bits.

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
var permissions: FilePermissions { get set }
```

#### Discussion

Setting this property will mask the `newValue` with the permissions bit mask `ALLPERMS`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filemode/permissions)*