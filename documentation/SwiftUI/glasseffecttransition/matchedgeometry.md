# matchedGeometry

**Framework**: SwiftUI  
**Kind**: property

Returns the matched geometry glass effect transition.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static var matchedGeometry: GlassEffectTransition { get }
```

#### Discussion

The matched geometry transition allows the geometries of glass shapes during an appearance or disappearance phase of a transition to be derived from the geometry of a nearby shape within the glass container.

For example, if a newly appearing shape is within the spacing of any existing shape, it will use that shapes geometry to transition out of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glasseffecttransition/matchedgeometry)*