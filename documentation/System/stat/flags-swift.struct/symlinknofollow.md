# symlinkNoFollow

**Framework**: System  
**Kind**: property

If the path ends with a symbolic link, return information about the link itself.

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
static var symlinkNoFollow: Stat.Flags { get }
```

#### Discussion

The corresponding C constant is `AT_SYMLINK_NOFOLLOW`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct/symlinknofollow)*