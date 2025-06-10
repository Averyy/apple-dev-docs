# writingDirection(strategy:)

**Framework**: ManagedAppDistribution  
**Kind**: method

A modifier for the default text writing direction strategy in the view hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View
```

#### Discussion

To control the writing direction explicitly, choose the `Text/WritingDirectionStrategy/layoutBased` mode and set the `EnvironmentValues/layoutDirection` to the appropriate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/writingdirection(strategy:))*