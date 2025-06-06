# streamingEarDidChangeNotification

**Framework**: Accessibility  
**Kind**: property

A notification that the system posts when there’s a change to which ears enable streaming.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let streamingEarDidChangeNotification: NSNotification.Name
```

#### Discussion

The system posts this notification when the value of [`streamingEar()`](axmfihearingdevice/streamingear().md) changes.

## See Also

- [AXMFiHearingDevice.Ear](axmfihearingdevice/ear.md)
  Constants that represent a hearing device ear.
- [static func streamingEar() -> AXMFiHearingDevice.Ear](axmfihearingdevice/streamingear.md)
  Returns which ears enable streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/streamingeardidchangenotification)*