# makeCoordinator(converter:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates the custom object that you use to communicate state changes from your gesture recognizer to other parts of your SwiftUI interface.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeCoordinator(converter: Self.CoordinateSpaceConverter) -> Self.Coordinator
```

#### Discussion

You access the resulting coordinator via the `Context` passed into other methods in this protocol.

## Parameters

- `converter`: A structure used to convert locations  to/from coordinate spaces in the hierarchy of the associated SwiftUI view.

## Default Implementations

### UIGestureRecognizerRepresentable Implementations
- [func makeCoordinator(converter: Self.CoordinateSpaceConverter)](./makecoordinator%28converter%29-504ge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentable/makecoordinator(converter:))*