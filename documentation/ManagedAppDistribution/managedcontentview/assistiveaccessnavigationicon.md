# assistiveAccessNavigationIcon(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Configures the view’s icon for purposes of navigation.

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
func assistiveAccessNavigationIcon(_ icon: Image) -> some View
```

#### Discussion

In an Assistive Access scene on iOS and iPadOS, the icon is displayed adjacent to the navigation title. Otherwise, the icon is unused.

## Parameters

- `icon`: The icon image to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/assistiveaccessnavigationicon(_:))*