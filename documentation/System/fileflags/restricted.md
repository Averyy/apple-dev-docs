# restricted

**Framework**: System  
**Kind**: property

File requires an entitlement for writing.

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
static var restricted: FileFlags { get }
```

#### Discussion

The corresponding C constant is `SF_RESTRICTED`.

> **Note**: This flag may only be changed by the superuser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/restricted)*