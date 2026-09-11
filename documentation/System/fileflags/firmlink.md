# firmlink

**Framework**: System  
**Kind**: property

File is a firmlink.

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
static var firmlink: FileFlags { get }
```

#### Discussion

Firmlinks are used by macOS to create transparent links between the read-only system volume and writable data volume. For example, the `/Applications` folder on the system volume is a firmlink to the `/Applications` folder on the data volume, allowing the user to see both system- and user-installed applications in a single folder.

The corresponding C constant is `SF_FIRMLINK`.

> **Note**: This flag may only be changed by the superuser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/firmlink)*