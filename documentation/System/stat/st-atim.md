# st_atim

**Framework**: System  
**Kind**: property

Time of last access, given as a C `timespec` since the Epoch.

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
var st_atim: timespec { get set }
```

#### Discussion

The corresponding C property is `st_atim` (or `st_atimespec` on Darwin).


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/st_atim)*