# buildBlock(_:_:_:_:_:_:)

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
static func buildBlock<C0, C1, C2, C3, C4, C5>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5) -> some SliderTickContent<V> where V == C0.Value, C0 : SliderTickContent, C1 : SliderTickContent, C2 : SliderTickContent, C3 : SliderTickContent, C4 : SliderTickContent, C5 : SliderTickContent, C0.Value == C1.Value, C1.Value == C2.Value, C2.Value == C3.Value, C3.Value == C4.Value, C4.Value == C5.Value
```

Available when `V` conforms to `BinaryFloatingPoint`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickbuilder/buildblock(_:_:_:_:_:_:))*