# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a view that represents the body of a button.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeBody(configuration: CardButtonStyle.Configuration) -> some View
```

#### Discussion

The system calls this method for each [`Button`](button.md) instance in a view hierarchy in which [`CardButtonStyle`](cardbuttonstyle.md) is the current button style.

## Parameters

- `configuration`: The properties of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/cardbuttonstyle/makebody(configuration:))*