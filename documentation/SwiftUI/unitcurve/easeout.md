# easeOut

**Framework**: SwiftUI  
**Kind**: property

A bezier curve that starts out quickly, then slows down as it approaches the end.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let easeOut: UnitCurve
```

#### Discussion

The start and end control points are located at (x: 0, y: 0) and (x: 0.58, y: 1).

## See Also

- [static let easeIn: UnitCurve](unitcurve/easein.md)
  A bezier curve that starts out slowly, then speeds up as it finishes.
- [static let easeInOut: UnitCurve](unitcurve/easeinout.md)
  A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [static let circularEaseIn: UnitCurve](unitcurve/circulareasein.md)
  A curve that starts out slowly, then speeds up as it finishes.
- [static let circularEaseOut: UnitCurve](unitcurve/circulareaseout.md)
  A circular curve that starts out quickly, then slows down as it approaches the end.
- [static let circularEaseInOut: UnitCurve](unitcurve/circulareaseinout.md)
  A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unitcurve/easeout)*