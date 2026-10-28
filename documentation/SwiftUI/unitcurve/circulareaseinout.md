# circularEaseInOut

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.

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
static let circularEaseInOut: UnitCurve
```

## Discussion

The shape of the curve is defined by a piecewise combination of `circularEaseIn` and `circularEaseOut`.

## See Also

### Getting easing curves
- [static let easeIn: UnitCurve](./easein.md)
  A bezier curve that starts out slowly, then speeds up as it finishes.
- [static let easeOut: UnitCurve](./easeout.md)
  A bezier curve that starts out quickly, then slows down as it approaches the end.
- [static let easeInOut: UnitCurve](./easeinout.md)
  A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [static let circularEaseIn: UnitCurve](./circulareasein.md)
  A curve that starts out slowly, then speeds up as it finishes.
- [static let circularEaseOut: UnitCurve](./circulareaseout.md)
  A circular curve that starts out quickly, then slows down as it approaches the end.
- [static let easeInEaseOut: UnitCurve](./easeineaseout.md)
  A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unitcurve/circulareaseinout)*