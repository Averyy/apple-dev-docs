# LayoutDirectionBehavior.mirrors(in:)

**Framework**: SwiftUI  
**Kind**: case

A behavior that mirrors when the layout direction has the specified value.

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
case mirrors(in: LayoutDirection)
```

#### Discussion

If you develop your view or shape in an LTR context, you can use `.mirrors(in: .rightToLeft)` (which is equivalent to `.mirrors`) to mirror your content when the layout direction is RTL (and keep the original version in LTR). If you developer in an RTL context, you can use `.mirrors(in: .leftToRight)` to mirror your content when the layout direction is LTR (and keep the original version in RTL).

## See Also

- [LayoutDirectionBehavior.fixed](layoutdirectionbehavior/fixed.md)
  A behavior that doesn’t mirror when the layout direction changes.
- [static var mirrors: LayoutDirectionBehavior](layoutdirectionbehavior/mirrors.md)
  A behavior that mirrors when the layout direction is right-to-left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutdirectionbehavior/mirrors(in:))*