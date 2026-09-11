# supportsSimultaneousSessions

**Framework**: Media Device  
**Kind**: property  
**Required**: Yes

Indicates whether the extension supports handling simultaneous media sessions via `MediaOutputSession`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
var supportsSimultaneousSessions: Bool { get }
```

#### Discussion

When `true`, the extension can receive multiple active [`MediaOutputSession`](mediaoutputsession.md) instances at once. When `false`, only one session is active at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/supportssimultaneoussessions)*