# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The automatic behavior.

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
static var automatic: ScrollBounceBehavior { get }
```

#### Discussion

The scrollable view automatically chooses whether content bounces when people scroll to the end of the view’s content. By default, scrollable views use the [`always`](./always.md) behavior.

## See Also

### Bounce behaviors
- [static var always: ScrollBounceBehavior](./always.md)
  The scrollable view always bounces.
- [static var basedOnSize: ScrollBounceBehavior](./basedonsize.md)
  The scrollable view bounces when its content is large enough to require scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollbouncebehavior/automatic)*