# callAsFunction(for:)

**Framework**: Foveated Streaming  
**Kind**: method

Presents the foveated streaming space that your app defines for the specified foveated streaming session.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@discardableResult
@MainActor func callAsFunction(for session: FoveatedStreamingSession) async -> OpenImmersiveSpaceAction.Result
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`openFoveatedStreamingSpace`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openFoveatedStreamingSpace) action:

```swift
await openFoveatedStreamingSpace()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `session`: The foveated streaming session associated with the foveated streaming space to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/openfoveatedstreamingspaceaction/callasfunction(for:))*