# init(idiom:)

**Framework**: UIKit  
**Kind**: init

Creates a new bar appearance object that targets the specified idiom.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(idiom: UIUserInterfaceIdiom)
```

#### Return Value

A new bar appearance object containing default values for the specified idiom.

## Parameters

- `idiom`: The device idiom to target. If you specify an idiom that doesn’t make sense for the current device, this method adjusts the idiom to an appropriate value.

## See Also

- [init(barAppearance: UIBarAppearance)](uibarappearance/init(barappearance:).md)
  Creates a new bar appearance object by copying relevant data from the specified appearance object.
- [convenience init()](uibarappearance/init.md)
  Creates a new bar appearance object containing default values.
- [init(coder: NSCoder)](uibarappearance/init(coder:).md)
  Creates an appearance object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarappearance/init(idiom:))*