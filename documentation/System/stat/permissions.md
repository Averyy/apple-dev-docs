# permissions

**Framework**: System  
**Kind**: property

File permissions for the given mode

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

> **Note**: This property is equivalent to `mode.permissions`. Modifying this property will update the underlying `st_mode` accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/permissions)*