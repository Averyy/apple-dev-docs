# basedOnSize

**Framework**: SwiftUI  
**Kind**: property

The scrollable view bounces when its content is large enough to require scrolling.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
static var basedOnSize: ScrollBounceBehavior { get }
```

#### Discussion

The scrollable view bounces along the specified axis if the size of the content exceeeds the size of the scrollable view in that axis.

## See Also

- [static var automatic: ScrollBounceBehavior](scrollbouncebehavior/automatic.md)
  The automatic behavior.
- [static var always: ScrollBounceBehavior](scrollbouncebehavior/always.md)
  The scrollable view always bounces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollbouncebehavior/basedonsize)*