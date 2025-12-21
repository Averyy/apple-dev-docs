# amount

**Framework**: SwiftUI  
**Kind**: property

The current amount of immersion.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
let amount: Double?
```

#### Discussion

Your app can display virtual content using [`ImmersiveSpace`](immersivespace.md) and the different immersion styles to create immersive experiences. Depending on the immersion style, none of it, parts of it, or a all of video pass-through are occluded by your app while having an Immersive Space opened, and the amount of it is represented by this value.

Some immersion styles allow changing the amount interactively by turning the Digital Crown.

This value is `nil`, if your app currently does not provide any immersive experience at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionchangecontext/amount)*