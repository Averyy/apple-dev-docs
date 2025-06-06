# appearance(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the appearance proxy for the receiver that has the passed trait collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func appearance(for trait: UITraitCollection) -> Self
```

#### Return Value

The appearance proxy for the receiver.

## Parameters

- `trait`: The trait collection used for matching.

## See Also

- [static func appearance() -> Self](uiappearance/appearance.md)
  Returns the appearance proxy for the receiver.
- [static func appearance(whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](uiappearance/appearance(whencontainedininstancesof:).md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [static func appearance(for: UITraitCollection, whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](uiappearance/appearance(for:whencontainedininstancesof:).md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearance/appearance(for:))*