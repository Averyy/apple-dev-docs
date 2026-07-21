# cancelTextAnimations(identifiers:)

**Framework**: AppKit  
**Kind**: method

Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func cancelTextAnimations(identifiers: [UUID])
```

#### Discussion

The UUIDs passed in should be those returned when starting the animations. To cancel all ahimations, use [`stopWritingTools()`](nswritingtoolscoordinator/stopwritingtools().md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/canceltextanimations(identifiers:))*