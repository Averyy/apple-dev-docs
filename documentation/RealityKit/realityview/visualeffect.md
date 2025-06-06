# visualEffect(_:)

**Framework**: RealityKit  
**Kind**: method

Applies effects to this view, while providing access to layout information through a geometry proxy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func visualEffect(_ effect: @escaping (EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View
```

#### Return Value

A view with the effect applied.

#### Discussion

You return new effects by calling functions on the first argument provided to the `effect` closure. In this example, `ContentView` is offset by its own size, causing its top left corner to appear where the bottom right corner was originally located:

```swift
ContentView()
    .visualEffect { content, geometryProxy in
        content.offset(geometryProxy.size)
    }
```

## Parameters

- `effect`: A closure that returns the effect to be applied. The first   argument provided to the closure is a placeholder representing   this view. The second argument is a  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/visualeffect(_:))*