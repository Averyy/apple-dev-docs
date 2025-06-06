# touchBar

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The property you implement to provide a Touch Bar object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var touchBar: NSTouchBar? { get }
```

#### Discussion

This property supports key-value observing, which is used by the system, for example, if you replace a running bar. Many subclasses of [`NSResponder`](nsresponder.md) implement this property and conform to the [`NSTouchBarProvider`](nstouchbarprovider.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbarprovider/touchbar)*