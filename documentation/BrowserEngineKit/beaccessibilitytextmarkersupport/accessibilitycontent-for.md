# accessibilityContent(for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns the accessibility content for a text range.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS ?+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func accessibilityContent(for range: BEAccessibilityTextMarker.Range) -> String?
```

#### Return Value

The string of text within the marker range, or `nil` if there’s no text in the range.

## Parameters

- `range`: The text marker range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport/accessibilitycontent(for:))*