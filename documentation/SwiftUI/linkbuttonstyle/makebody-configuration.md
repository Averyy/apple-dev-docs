# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a view that represents the body of a button.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func makeBody(configuration: LinkButtonStyle.Configuration) -> some View
```

#### Discussion

The system calls this method for each [`Button`](button.md) instance in a view hierarchy where this style is the current button style.

## Parameters

- `configuration`: The properties of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/linkbuttonstyle/makebody(configuration:))*