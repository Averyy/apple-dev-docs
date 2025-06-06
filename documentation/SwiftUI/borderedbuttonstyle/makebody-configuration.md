# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a view that represents the body of a button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeBody(configuration: BorderedButtonStyle.Configuration) -> some View
```

#### Discussion

The system calls this method for each [`Button`](button.md) instance in a view hierarchy where this style is the current button style.

## Parameters

- `configuration`: The properties of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/borderedbuttonstyle/makebody(configuration:))*