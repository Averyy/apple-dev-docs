# ignoreClipping

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that specifies whether to ignore framing on windows when using content filters.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var ignoreClipping: Bool { get set }
```

#### Discussion

Use [`SCContentFilter`](sccontentfilter.md) in conjunction with this property to ignore window framing on specified apps and windows. Setting this value to `true` ignores shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/ignoreclipping)*