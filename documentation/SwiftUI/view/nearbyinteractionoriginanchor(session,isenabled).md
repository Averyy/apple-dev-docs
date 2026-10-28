# nearbyInteractionOriginAnchor(session:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies this view as the reference body for the nearby interaction session’s angle calculations.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
nonisolated
func nearbyInteractionOriginAnchor(session: NISession, isEnabled: Bool = true) -> some View
```

## Discussion

```swift
@State private var session = NISession()

var body: some View {
    MyView()
        .nearbyInteractionOriginAnchor(session: session)
}
```

If more than one view specifies itself as the body of the same session, the most recent one to do so becomes the body. Once a view stops being the body, whether because it disappeared or because `isEnabled` became `false`, the session has no body until some view specifies one again.

Use `isEnabled` to pick between views which are all on screen. For example, an app might anchor angles to a compact indicator, except while showing a full-screen finding experience, when it anchors to that instead:

```swift
ZStack {
    CompactIndicator()
        .nearbyInteractionOriginAnchor(
            session: session, isEnabled: !isFinding)
    FindingView()
        .nearbyInteractionOriginAnchor(
            session: session, isEnabled: isFinding)
}
```

## Parameters

- `session`: The session to specify this view as the body of.
- `isEnabled`: Whether this view should be the session’s body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/nearbyinteractionoriginanchor(session:isenabled:))*