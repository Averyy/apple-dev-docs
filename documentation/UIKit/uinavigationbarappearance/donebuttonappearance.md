# doneButtonAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance attributes for Done buttons.

**Availability**:
- iOS 13.0+ - Deprecated in 26.0
- iPadOS 13.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 13.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
@NSCopying
var doneButtonAppearance: UIBarButtonItemAppearance { get set }
```

```objc
@property (nonatomic, copy, readwrite) UIBarButtonItemAppearance * doneButtonAppearance;
```

#### Discussion

Use this property to configure the appearance of bar button items that use the [`done`](../uibarbuttonitem/style-swift.enum/done.md) style, when appropriate. If the navigation bar doesn’t have a done button, setting the value of this property has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/donebuttonappearance)*