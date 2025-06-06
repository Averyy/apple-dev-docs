# appearance()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the appearance proxy for the receiver.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
static func appearance() -> Self
```

#### Return Value

The appearance proxy for the receiver.

## See Also

- [static func appearance(for: UITraitCollection) -> Self](uiappearance/appearance(for:).md)
  Returns the appearance proxy for the receiver that has the passed trait collection.
- [static func appearance(whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](uiappearance/appearance(whencontainedininstancesof:).md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [static func appearance(for: UITraitCollection, whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](uiappearance/appearance(for:whencontainedininstancesof:).md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearance/appearance())*