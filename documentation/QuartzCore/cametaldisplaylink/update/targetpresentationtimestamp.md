# targetPresentationTimestamp

**Framework**: Core Animation  
**Kind**: property

The time the system estimates until the display of the next frame.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var targetPresentationTimestamp: CFTimeInterval { get }
```

#### Discussion

Update your animations based on the time difference between this timestamp and the previous timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update/targetpresentationtimestamp)*