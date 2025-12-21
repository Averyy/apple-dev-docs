# callAsFunction()

**Framework**: SwiftUI  
**Kind**: method

Dismisses the currently opened immersive space.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func callAsFunction() async
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`dismissImmersiveSpace`](environmentvalues/dismissimmersivespace.md) action:

```swift
await dismissImmersiveSpace()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Methods-with-Special-Names) in .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismissimmersivespaceaction/callasfunction())*