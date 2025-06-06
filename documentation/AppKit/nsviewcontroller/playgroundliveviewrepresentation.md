# playgroundLiveViewRepresentation()

**Framework**: AppKit  
**Kind**: method

Returns the `XCPlaygroundLiveViewRepresentation` for the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func playgroundLiveViewRepresentation() -> XCPlaygroundLiveViewRepresentation
```

#### Discussion

The value returned from this method can but does not need to be the same every time; XCPlaygroundLiveViewables may choose to create a new view or view controller every time.

> **Note**: `XCPlaygroundLiveViewRepresentation`

`XCPlaygroundLiveViewRepresentation`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/playgroundliveviewrepresentation())*