# addFeedbackHandler(_:)

**Framework**: Metal  
**Kind**: method

Registers a commit feedback handler that Metal calls with feedback data when available.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func addFeedbackHandler(_ block: @escaping MTL4CommitFeedbackHandler)
```

## Parameters

- `block`:   that Metal invokes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commitoptions/addfeedbackhandler(_:))*