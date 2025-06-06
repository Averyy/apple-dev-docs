# init(in:content:)

**Framework**: SwiftUI  
**Kind**: init

Produces a view constrained in the given axes from one of several alternatives provided by a view builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(in axes: Axis.Set = [.horizontal, .vertical], @ViewBuilder content: () -> Content)
```

## Parameters

- `axes`: A set of axes to constrain children to. The set may   contain  ,  , or both of these.    chooses the first child whose size fits within the   proposed size on these axes. If   is an empty set,    uses the first child view. By default,    uses both axes.
- `content`: A view builder that provides the child views for this   container, in order of preference. The builder chooses the first   child view that fits within the proposed width, height, or both,   as defined by  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewthatfits/init(in:content:))*