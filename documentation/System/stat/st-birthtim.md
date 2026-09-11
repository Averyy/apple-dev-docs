# st_birthtim

**Framework**: System  
**Kind**: property

Time of file creation, given as a C `timespec` since the Epoch.

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
var st_birthtim: timespec { get set }
```

#### Discussion

The corresponding C property is `st_birthtim` (or `st_birthtimespec` on Darwin).

> **Note**: Only available on Darwin and FreeBSD.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/st_birthtim)*