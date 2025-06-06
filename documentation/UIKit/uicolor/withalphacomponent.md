# withAlphaComponent(_:)

**Framework**: UIKit  
**Kind**: method

Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withAlphaComponent(_ alpha: CGFloat) -> UIColor
```

#### Return Value

The new `UIColor` object.

#### Discussion

A subclass with explicit opacity components should override this method to return a color with the specified alpha.

## Parameters

- `alpha`: The opacity value of the new color object, specified as a value from 0.0 to 1.0. Alpha values below 0.0 are interpreted as 0.0, and values above 1.0 are interpreted as 1.0.

## See Also

- [convenience init(Color)](uicolor/init(_:).md)
  Creates a color object that encapsulates a SwiftUI color.
- [init(ciColor: CIColor)](uicolor/init(cicolor:).md)
  Creates a color object that encapsulates a Core Image color.
- [init(cgColor: CGColor)](uicolor/init(cgcolor:).md)
  Creates a color object using the specified Quartz color reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/withalphacomponent(_:))*