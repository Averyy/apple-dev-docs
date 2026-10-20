# buildBlock(_:_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<C0, C1, C2>(_ c0: C0, _ c1: C1, _ c2: C2) -> some SliderTickContent<V> where V == C0.Value, C0 : SliderTickContent, C1 : SliderTickContent, C2 : SliderTickContent, C0.Value == C1.Value, C1.Value == C2.Value
```

Available when `V` conforms to `BinaryFloatingPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickbuilder/buildblock(_:_:_:))*