# overrideTraitCollection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Interface traits for the presented view controller, to use in place of traits from the iOS environment.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`traitOverrides`](./traitoverrides-629ka.md) instead.

## Declaration

```swift
@NSCopying
var overrideTraitCollection: UITraitCollection? { get set }
```

```objc
@property (nonatomic, copy, nullable) UITraitCollection * overrideTraitCollection;
```

## Mentions

- [Choosing a specific interface style for your iOS app](../choosing-a-specific-interface-style-for-your-ios-app.md)

## Discussion

Use this property to provide an interface trait collection for the presented view controller, overriding one or more values in the iOS trait environment.

Each value you place in the [`overrideTraitCollection`](./overridetraitcollection.md) property overrides the corresponding value in the iOS trait environment. For example, the following code snippet shows how to override the display scale for the presented view controller, leaving other traits as they are provided by the system. Place such code, typically, in the implementation file for the presenting view controller:

```objc
presentedVC.presentationController.overrideTraitCollection = [UITraitCollection traitCollectionWithDisplayScale: 1.5];
[self presentViewController: presentedVC animated: NO completion: nil];
```

The *presenting* view controller is not affected by use of this property.

The default value of the [`overrideTraitCollection`](./overridetraitcollection.md) property is `nil`, which results in the full iOS trait environment being used by the presented view controller.

## See Also

### Overriding trait values
- [var traitOverrides: UITraitOverrides](./traitoverrides-629ka.md)
- [struct UITraitOverrides](../uitraitoverrides-swift.struct.md)
  A mutable container of traits you use to set trait changes for an object and its descendants.
- [traitOverrides](./traitoverrides-9o0j4.md)
- [UITraitOverrides](../uitraitoverrides-c.protocol.md)
  A mutable container of traits you use to set trait changes for an object and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/overridetraitcollection)*