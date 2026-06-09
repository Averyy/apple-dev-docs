# st_birthtim

**Framework**: System  
**Kind**: property

Time of file creation, given as a C `timespec` since the Epoch.

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
var st_birthtim: timespec { get set }
```

#### Discussion

The corresponding C property is `st_birthtim` (or `st_birthtimespec` on Darwin).

> **Note**: Only available on Darwin and FreeBSD.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/st_birthtim)*