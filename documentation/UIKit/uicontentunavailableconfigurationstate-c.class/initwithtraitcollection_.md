# initWithTraitCollection:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a configuration state with the specified trait collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithTraitCollection:(UITraitCollection *) traitCollection;
```

#### Discussion

Typically, you don’t create a configuration state yourself. To access the current configuration state for a content-unavailable view, read [`contentUnavailableConfigurationState`](../uiviewcontroller/contentunavailableconfigurationstate-9bvga.md). View controller subclasses can override that property to customize the configuration state returned by the system.

## Parameters

- `traitCollection`: The trait collection describing the user interface environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableconfigurationstate-c.class/initwithtraitcollection:)*