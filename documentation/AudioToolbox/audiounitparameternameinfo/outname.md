# outName

**Framework**: Audio Toolbox  
**Kind**: property

When getting an audio unit property that uses this data structure for its value, the short version of the parameter name provided by the audio unit. The host application then owns the string and is responsible for releasing it.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var outName: Unmanaged<CFString>?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameternameinfo/outname)*