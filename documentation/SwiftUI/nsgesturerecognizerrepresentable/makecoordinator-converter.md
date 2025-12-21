# makeCoordinator(converter:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeCoordinator(converter: Self.CoordinateSpaceConverter) -> Self.Coordinator
```

#### Discussion

You access the resulting coordinator via the `Context` passed into other methods in this protocol.

## Parameters

- `converter`: A structure used to convert locations  to/from   coordinate spaces in the hierarchy of the associated SwiftUI view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentable/makecoordinator(converter:))*