# BackgroundProminence

**Framework**: SwiftUI  
**Kind**: struct

The prominence of backgrounds underneath other views.

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
struct BackgroundProminence
```

#### Overview

Background prominence should influence foreground styling to maintain sufficient contrast against the background. For example, selected rows in a `List` and `Table` can have increased prominence backgrounds with accent color fills when focused; the foreground content above the background should be adjusted to reflect that level of prominence.

This can be read and written for views with the `EnvironmentValues.backgroundProminence` property.

## Topics

### Getting background prominence
- [static let standard: BackgroundProminence](backgroundprominence/standard.md)
  The standard prominence of a background
- [static let increased: BackgroundProminence](backgroundprominence/increased.md)
  A more prominent background that likely requires some changes to the views above it.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func listRowBackground<V>(V?) -> some View](view/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](view/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [struct AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md)
  The styling of views with respect to alternating row backgrounds.
- [var backgroundProminence: BackgroundProminence](environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundprominence)*