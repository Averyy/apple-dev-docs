# symlinkNoFollowAny

**Framework**: System  
**Kind**: property

If the path ends with a symbolic link, return information about the link itself. If *any* symbolic link is encountered during path resolution, return an error.

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
static var symlinkNoFollowAny: Stat.Flags { get }
```

#### Discussion

The corresponding C constant is `AT_SYMLINK_NOFOLLOW_ANY`.

> **Note**: Only available on Darwin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct/symlinknofollowany)*