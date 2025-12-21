# ignoreClipping

**Framework**: ScreenCaptureKit  
**Kind**: property

A Boolean value that specifies whether to ignore framing on windows when using content filters.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var ignoreClipping: Bool { get set }
```

#### Discussion

Use `SCNPropertyFilter` in conjunction with this property to ignore window framing on specified apps and windows. Setting this value to `true` ignores shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/ignoreclipping)*