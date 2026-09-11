# asyncImageURLSession(_:)

**Framework**: SwiftUI  
**Kind**: method

A modifier that adds a URL session for asynchronous images contained in the view to use when fetching image data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
func asyncImageURLSession(_ urlSession: URLSession) -> some View
```

## Parameters

- `urlSession`: An instance of [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) for [`AsyncImage`](asyncimage.md) instances to use for image download data tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/asyncimageurlsession(_:))*