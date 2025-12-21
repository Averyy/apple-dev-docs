# widgetURL(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the URL to open in the containing app when the user clicks the widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency func widgetURL(_ url: URL?) -> some View
```

#### Return Value

A view that opens the specified URL when the user clicks the widget.

#### Discussion

Widgets support one `widgetURL` modifier in their view hierarchy. If multiple views have `widgetURL` modifiers, the behavior is undefined.

## Parameters

- `url`: The URL to open in the containing app.

## See Also

- [func onOpenURL(perform: (URL) -> ()) -> some View](view/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/widgeturl(_:))*