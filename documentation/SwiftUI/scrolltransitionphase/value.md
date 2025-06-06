# value

**Framework**: SwiftUI  
**Kind**: property

A phase-derived value that can be used to scale or otherwise modify effects.

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

#### Discussion

Returns -1.0 when in the topLeading phase, zero when in the identity phase, and 1.0 when in the bottomTrailing phase.

## See Also

- [var isIdentity: Bool](scrolltransitionphase/isidentity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionphase/value)*