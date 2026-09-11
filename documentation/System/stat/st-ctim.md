# st_ctim

**Framework**: System  
**Kind**: property

Time of last status (inode) change, given as a C `timespec` since the Epoch.

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
var st_ctim: timespec { get set }
```

#### Discussion

The corresponding C property is `st_ctim` (or `st_ctimespec` on Darwin).


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/st_ctim)*