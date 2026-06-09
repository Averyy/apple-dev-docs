# firmlink

**Framework**: System  
**Kind**: property

File is a firmlink.

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
static var firmlink: FileFlags { get }
```

#### Discussion

Firmlinks are used by macOS to create transparent links between the read-only system volume and writable data volume. For example, the `/Applications` folder on the system volume is a firmlink to the `/Applications` folder on the data volume, allowing the user to see both system- and user-installed applications in a single folder.

The corresponding C constant is `SF_FIRMLINK`.

> **Note**: This flag may only be changed by the superuser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/firmlink)*