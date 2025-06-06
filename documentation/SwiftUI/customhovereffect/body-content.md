# body(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Defines the effect produced by this effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func body(content: Self.Content) -> Self.Body
```

#### Return Value

A custom effect.

#### Discussion

You implement this method to describe a custom effect to apply to a view. `content` is an empty effect you use to build your effect, which will later be applied to a View, or combined with other `CustomHoverEffect`s.

## Parameters

- `content`: An empty effect you use to compose the custom   effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/body(content:))*