# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a view that represents the body of a button.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func makeBody(configuration: GlassButtonStyle.Configuration) -> some View
```

#### Discussion

The system calls this method for each [`Button`](button.md) instance in a view hierarchy where this style is the current button style.

## Parameters

- `configuration`: The properties of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbuttonstyle/makebody(configuration:))*