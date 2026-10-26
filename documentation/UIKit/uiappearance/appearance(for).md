# appearance(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Returns the appearance proxy for the receiver that has the passed trait collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static func appearance(for trait: UITraitCollection) -> Self
```

```objc
+ (instancetype) appearanceForTraitCollection:(UITraitCollection *) trait;
```

#### Return Value

The appearance proxy for the receiver.

## Parameters

- `trait`: The trait collection used for matching.

## See Also

### Working with the appearance proxy
- [static func appearance() -> Self](./appearance%28%29.md)
  Returns the appearance proxy for the receiver.
- [static func appearance(whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](./appearance%28whencontainedininstancesof%29.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [static func appearance(for: UITraitCollection, whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](./appearance%28for,whencontainedininstancesof%29.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.
- [+ appearanceWhenContainedIn:](./appearancewhencontainedin_.md)
  Returns the appearance proxy for object when it’s contained in the hierarchy the specified classes describe.
- [+ appearanceForTraitCollection:whenContainedIn:](./appearancefortraitcollection_whencontainedin_.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearance/appearance(for:))*