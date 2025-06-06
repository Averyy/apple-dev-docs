# AlternatingRowBackgroundBehavior

**Framework**: SwiftUI  
**Kind**: struct

The styling of views with respect to alternating row backgrounds.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct AlternatingRowBackgroundBehavior
```

#### Overview

Use values of this type with the [`alternatingRowBackgrounds(_:)`](view/alternatingrowbackgrounds(_:).md) modifier.

## Topics

### Getting alternating row background behavior
- [static let automatic: AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior/automatic.md)
  The automatic alternating row background behavior.
- [static let enabled: AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior/enabled.md)
  Alternating rows will be enabled for applicable views.
- [static let disabled: AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior/disabled.md)
  Alternating rows will be disabled for applicable views.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func listRowBackground<V>(V?) -> some View](view/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](view/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [var backgroundProminence: BackgroundProminence](environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [struct BackgroundProminence](backgroundprominence.md)
  The prominence of backgrounds underneath other views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alternatingrowbackgroundbehavior)*