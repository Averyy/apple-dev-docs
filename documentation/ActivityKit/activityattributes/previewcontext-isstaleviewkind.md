# previewContext(_:isStale:viewKind:)

**Framework**: ActivityKit  
**Kind**: method

Generates a preview for a Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
func previewContext(_ contentState: Self.ContentState, isStale: Bool = false, viewKind: ActivityPreviewViewKind) -> some View
```

## Parameters

- `contentState`: The dynamic content of the Live Activity.
- `isStale`: A Boolean that indicates whether the content of a Live Activity is out of date.
- `viewKind`: A value that determines which Live Activity presentation to render for this preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityattributes/previewcontext(_:isstale:viewkind:))*