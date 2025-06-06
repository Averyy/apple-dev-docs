# init(barAppearance:)

**Framework**: UIKit  
**Kind**: init

Creates a new bar appearance object by copying relevant data from the specified appearance object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(barAppearance: UIBarAppearance)
```

#### Return Value

A new bar appearance object containing the relevant properties from the other object.

#### Discussion

This method copies over the properties from `barAppearance` that are also relevant to the new bar appearance object.

## Parameters

- `barAppearance`: The bar appearance object from which to copy the relevant properties.

## See Also

- [init(idiom: UIUserInterfaceIdiom)](uibarappearance/init(idiom:).md)
  Creates a new bar appearance object that targets the specified idiom.
- [convenience init()](uibarappearance/init.md)
  Creates a new bar appearance object containing default values.
- [init(coder: NSCoder)](uibarappearance/init(coder:).md)
  Creates an appearance object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/init(barappearance:))*