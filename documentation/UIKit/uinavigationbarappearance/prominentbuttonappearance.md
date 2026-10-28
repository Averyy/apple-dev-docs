# prominentButtonAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance attributes for Prominent buttons.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var prominentButtonAppearance: UIBarButtonItemAppearance { get set }
```

```objc
@property (nonatomic, copy, readwrite) UIBarButtonItemAppearance * prominentButtonAppearance;
```

## Discussion

Use this property to configure the appearance of bar button items that use `UIBarButtonItemStyleProminent`. If the navigation bar doesn’t have any buttons using this style, this property has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/prominentbuttonappearance)*