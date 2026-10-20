# AlternatingRowBackgroundBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The styling of views with respect to alternating row backgrounds.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct AlternatingRowBackgroundBehavior
```

#### Overview

Use values of this type with the [`alternatingRowBackgrounds(_:)`](./view/alternatingrowbackgrounds%28_%29.md) modifier.

## Topics

### Getting alternating row background behavior
- [static let automatic: AlternatingRowBackgroundBehavior](./alternatingrowbackgroundbehavior/automatic.md)
  The automatic alternating row background behavior.
- [static let enabled: AlternatingRowBackgroundBehavior](./alternatingrowbackgroundbehavior/enabled.md)
  Alternating rows will be enabled for applicable views.
- [static let disabled: AlternatingRowBackgroundBehavior](./alternatingrowbackgroundbehavior/disabled.md)
  Alternating rows will be disabled for applicable views.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring backgrounds
- [func listRowBackground<V>(V?) -> some View](./view/listrowbackground%28_%29.md)
  Places a custom background view behind a list row item.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](./view/alternatingrowbackgrounds%28_%29.md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [var backgroundProminence: BackgroundProminence](./environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [struct BackgroundProminence](./backgroundprominence.md)
  The prominence of backgrounds underneath other views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alternatingrowbackgroundbehavior)*