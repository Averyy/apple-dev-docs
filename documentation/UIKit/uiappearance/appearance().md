# appearance()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Returns the appearance proxy for the receiver.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
static func appearance() -> Self
```

```objc
+ (instancetype) appearance;
```

#### Return Value

The appearance proxy for the receiver.

## See Also

### Working with the appearance proxy
- [static func appearance(for: UITraitCollection) -> Self](./appearance%28for%29.md)
  Returns the appearance proxy for the receiver that has the passed trait collection.
- [static func appearance(whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](./appearance%28whencontainedininstancesof%29.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [static func appearance(for: UITraitCollection, whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](./appearance%28for,whencontainedininstancesof%29.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearance/appearance())*