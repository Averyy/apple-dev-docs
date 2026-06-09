# asyncImageURLSession(_:)

**Framework**: SwiftUI  
**Kind**: method

A modifier that adds a URL session for asynchronous images contained in the view to use when fetching image data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func asyncImageURLSession(_ urlSession: URLSession) -> some View
```

## Parameters

- `urlSession`: An instance of [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) for [`AsyncImage`](asyncimage.md) instances to use for image download data tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/asyncimageurlsession(_:))*