# ignoresSafeArea(_:edges:)

**Framework**: App Intents  
**Kind**: method

Expands the safe area of a view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func ignoresSafeArea(_ regions: SafeAreaRegions = .all, edges: Edge.Set = .all) -> some View
```

#### Return Value

A view with an expanded safe area.

#### Discussion

By default, the SwiftUI layout system sizes and positions views to avoid certain safe areas. This ensures that system content like the software keyboard or edges of the device don’t obstruct your views. To extend your content into these regions, you can ignore safe areas on specific edges by applying this modifier.

For examples of how to use this modifier, see doc:Adding-a-Background-to-Your-View.

## Parameters

- `regions`: The regions to expand the view’s safe area into. The   modifier expands into all safe area region types by default.
- `edges`: The set of edges to expand. Any edges that you   don’t include in this set remain unchanged. The set includes all   edges by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/ignoressafearea(_:edges:))*