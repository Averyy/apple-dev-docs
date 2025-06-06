# widgetURL(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Sets the URL to open in the containing app when the user clicks the widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/widgeturl(_:))*