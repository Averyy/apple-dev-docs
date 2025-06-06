# playgroundLiveViewRepresentation

**Framework**: Appkit  
**Kind**: property

A custom `PlaygroundLiveViewRepresentation` for this instance.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var playgroundLiveViewRepresentation: PlaygroundLiveViewRepresentation { get }
```

#### Discussion

The value of this property can but does not need to be the same every time; PlaygroundLiveViewables may choose to create a new view or view controller every time.

> **Note**: `PlaygroundLiveViewRepresentation`


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsview/playgroundliveviewrepresentation)*