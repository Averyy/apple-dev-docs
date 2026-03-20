# callAsFunction(foveatedStreaming:)

**Framework**: SwiftUI  
**Kind**: method

Presents the immersive space that your app defines for the specified foveated streaming session.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@discardableResult
@MainActor func callAsFunction(foveatedStreaming session: FoveatedStreamingSession) async -> OpenImmersiveSpaceAction.Result
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the `<doc://com.apple.documentation/documentation/swiftui/environmentvalues/openimmersivespace>` action with a foveated streaming session:

```swift
await openImmersiveSpace(foveatedStreaming: session)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in *The Swift Programming Language*.

## Parameters

- `session`: The foveated streaming session associated with the immersive space to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openimmersivespaceaction/callasfunction(foveatedstreaming:))*