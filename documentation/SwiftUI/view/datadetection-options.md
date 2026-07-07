# dataDetection(_:options:)

**Framework**: SwiftUI  
**Kind**: method

Asynchronously detects data in the view’s content and styles them to indicate they are clickable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func dataDetection(_ types: DataDetector.MatchType = .all, options: DataDetector.Options = .init()) -> some View
```

#### Return Value

A view with modified text attributes when matches are detected

## Parameters

- `types`: The data detector match types
- `options`: Data detector options


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/datadetection(_:options:))*