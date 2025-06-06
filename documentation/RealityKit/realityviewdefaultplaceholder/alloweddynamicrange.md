# allowedDynamicRange(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a new view configured with the specified allowed dynamic range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func allowedDynamicRange(_ range: Image.DynamicRange?) -> some View
```

#### Return Value

A new view.

#### Discussion

The following example enables HDR rendering within a view hierarchy:

```None
MyView().allowedDynamicRange(.high)
```

## Parameters

- `range`: The requested dynamic range, or nil to   restore the default allowed range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/alloweddynamicrange(_:))*