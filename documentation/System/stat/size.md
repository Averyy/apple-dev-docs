# size

**Framework**: System  
**Kind**: property

Total size, in bytes

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
var size: Int64 { get set }
```

#### Discussion

The semantics of this property are tied to the underlying C `st_size` field, which can have file-system–dependent behavior. For example, this property can return different values for a file’s data fork and resource fork, and some file systems report logical size rather than actual disk usage for compressed or cloned files.

The corresponding C property is `st_size`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/size)*