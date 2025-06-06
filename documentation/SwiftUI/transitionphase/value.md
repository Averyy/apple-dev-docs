# value

**Framework**: SwiftUI  
**Kind**: property

A value that can be used to multiply effects that are applied differently depending on the phase.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var value: Double { get }
```

#### Return Value

Zero when in the `identity` case, -1.0 for `willAppear`, and 1.0 for `didDisappear`.

## See Also

- [var isIdentity: Bool](transitionphase/isidentity.md)
  A Boolean that indicates whether the transition should have an identity effect, i.e. not change the appearance of its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transitionphase/value)*