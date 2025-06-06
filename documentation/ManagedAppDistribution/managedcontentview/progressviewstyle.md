# progressViewStyle(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets the style for progress views in this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func progressViewStyle<S>(_ style: S) -> some View where S : ProgressViewStyle
```

#### Discussion

For example, the following code creates a progress view that uses the “circular” style:

```None
ProgressView()
    .progressViewStyle(.circular)
```

## Parameters

- `style`: The progress view style to use for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/progressviewstyle(_:))*