# id

**Framework**: TipKit  
**Kind**: property  
**Required**: Yes

The tip’s unique identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var id: String { get }
```

#### Overview

> **Note**: More information on custom tip identifiers can be found in WWDC24 Session 10070: [`Customize feature discovery with TipKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10070?time=312).

By default the type name of the `Tip` conforming struct will be used as the tip’s `id`. Specifying a custom `id` allows you to create reusable tips based on their content.

```swift
struct NewTrailTip: Tip {
    let newTrail: Trail
    
    var id: String {
        "NewTrailTip-\(newTrail.id)"
    }
}
    
struct TrailList: View {
    let newTrail: Trail
    
    var body: some View {
        // Creates a different tip for each new trail.
        let newTrailTip = NewTrailTip(newTrail)
        TipView(newTrailTip)
    }
}
```

## See Also

- [var title: Text](tip/title.md)
  A title that names the tip.
- [var message: Text?](tip/message.md)
  A short description of how to use the tip’s feature.
- [var image: Image?](tip/image.md)
  The image associated with the tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/id)*