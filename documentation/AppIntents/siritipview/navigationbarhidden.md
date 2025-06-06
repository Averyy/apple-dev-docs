# navigationBarHidden(_:)

**Framework**: App Intents  
**Kind**: method

Hides the navigation bar for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func navigationBarHidden(_ hidden: Bool) -> some View
```

#### Discussion

Use `navigationBarHidden(_:)` to hide the navigation bar. This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

## Parameters

- `hidden`: A Boolean value that indicates whether to hide the   navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/navigationbarhidden(_:))*