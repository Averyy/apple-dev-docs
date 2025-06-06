# overrideTraitCollection

**Framework**: UIKit  
**Kind**: property

Interface traits for the presented view controller, to use in place of traits from the iOS environment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var overrideTraitCollection: UITraitCollection? { get set }
```

## Mentions

- [Choosing a specific interface style for your iOS app](choosing-a-specific-interface-style-for-your-ios-app.md)

#### Discussion

Use this property to provide an interface trait collection for the presented view controller, overriding one or more values in the iOS trait environment.

Each value you place in the [`overrideTraitCollection`](uipresentationcontroller/overridetraitcollection.md) property overrides the corresponding value in the iOS trait environment. For example, the following code snippet shows how to override the display scale for the presented view controller, leaving other traits as they are provided by the system. Place such code, typically, in the implementation file for the presenting view controller:

```objc
presentedVC.presentationController.overrideTraitCollection = [UITraitCollection traitCollectionWithDisplayScale: 1.5];
[self presentViewController: presentedVC animated: NO completion: nil];
```

The  view controller is not affected by use of this property.

The default value of the [`overrideTraitCollection`](uipresentationcontroller/overridetraitcollection.md) property is `nil`, which results in the full iOS trait environment being used by the presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/overridetraitcollection)*