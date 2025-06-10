# objectWillChange

**Framework**: SwiftUI  
**Kind**: property

A publisher that informs subscribers of changes to the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final let objectWillChange: PassthroughSubject<Void, Never>
```

#### Discussion

The renderer’s [`ObjectWillChangePublisher`](https://developer.apple.com/documentation/Combine/ObservableObject/ObjectWillChangePublisher) publishes `Void` elements. Subscribers should interpret any event as indicating that the contents of the image may have changed.

## See Also

- [var isObservationEnabled: Bool](imagerenderer/isobservationenabled.md)
  If observers of this observed object should be notified when the produced image changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/objectwillchange)*