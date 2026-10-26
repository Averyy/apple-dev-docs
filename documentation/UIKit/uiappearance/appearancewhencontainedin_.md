# appearanceWhenContainedIn:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns the appearance proxy for object when it’s contained in the hierarchy the specified classes describe.

**Availability**:
- iOS 5.0+ - Deprecated in 9.0
- iPadOS 5.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```objc
+ (instancetype) appearanceWhenContainedIn:(Class<UIAppearanceContainer> *) ContainerClass;
```

#### Return Value

The appearance proxy to use for the object.

#### Discussion

Set the `ContainerClass` array to an ascending hierarchical list of containing types. For example, if you want a navigation bar to take on a specific appearance when contained in a navigation controller inside a tab bar controller, set `ContainerClass` to `@[[UINavigationController class], [UITabBarController class], nil]`.

Do not set `ContainerClass` to an unrelated list of types or to a list that does not match the containment hierarchy of your user interface.

This method throws an exception for any item in the var-args list that is not a Class object that conforms to the `UIAppearanceContainer` protocol.

## Parameters

- `ContainerClass`: A nil-terminated list of appearance container classes, in ascending hierarchical order.

## See Also

### Working with the appearance proxy
- [static func appearance() -> Self](./appearance%28%29.md)
  Returns the appearance proxy for the receiver.
- [static func appearance(for: UITraitCollection) -> Self](./appearance%28for%29.md)
  Returns the appearance proxy for the receiver that has the passed trait collection.
- [static func appearance(whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](./appearance%28whencontainedininstancesof%29.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [static func appearance(for: UITraitCollection, whenContainedInInstancesOf: [any UIAppearanceContainer.Type]) -> Self](./appearance%28for,whencontainedininstancesof%29.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.
- [+ appearanceForTraitCollection:whenContainedIn:](./appearancefortraitcollection_whencontainedin_.md)
  Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiappearance/appearancewhencontainedin:)*