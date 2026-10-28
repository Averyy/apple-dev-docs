# alignmentGuide(_:computeValue:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a view modified so that its value for the given `guide` is the result of passing the `ViewDimensions` of the underlying element to `computeValue`.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func alignmentGuide(_ g: DepthAlignment, computeValue: @escaping (ViewDimensions3D) -> CGFloat) -> some View
```

**Other overloads**:

```swift
@preconcurrency
nonisolated func alignmentGuide(_ g: HorizontalAlignment, computeValue: @escaping @Sendable (ViewDimensions) -> CGFloat) -> some View
```

```swift
@preconcurrency
nonisolated func alignmentGuide(_ g: VerticalAlignment, computeValue: @escaping @Sendable (ViewDimensions) -> CGFloat) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alignmentguide(_:computevalue:)-8n4it)*