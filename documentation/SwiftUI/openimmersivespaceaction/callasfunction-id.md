# callAsFunction(id:)

**Framework**: SwiftUI  
**Kind**: method

Presents an immersive space for the scene with the specified identifier.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@discardableResult
@MainActor func callAsFunction(id: String) async -> OpenImmersiveSpaceAction.Result
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`openImmersiveSpace`](environmentvalues/openimmersivespace.md) action with a string identifier:

```swift
await openImmersiveSpace(id: "planet")
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Methods-with-Special-Names) in .

## Parameters

- `id`: The identifier of the immersive space to present.

## See Also

- [func callAsFunction<D>(id: String, value: D) async -> OpenImmersiveSpaceAction.Result](openimmersivespaceaction/callasfunction(id:value:).md)
  Presents the immersive space that your app defines for the specified identifier and that handles the type of the presented value.
- [func callAsFunction<D>(value: D) async -> OpenImmersiveSpaceAction.Result](openimmersivespaceaction/callasfunction(value:).md)
  Presents the immersive space that handles the type of the presented value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openimmersivespaceaction/callasfunction(id:))*