# Optionally

**Framework**: RegexBuilder  
**Kind**: struct  
**Role**: Structure

A regex component that matches zero or one occurrences of its underlying component.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct Optionally<Output>
```

## Topics

### Initializers
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-12hxo.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-2jtrp.md)
  Creates a regex component that matches the given component zero or one times.
- [init(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-2zdez.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-4230v.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-44oku.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-4kz5l.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-5azqh.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-6j92l.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-6v0ti.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-7f3n1.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-7te1p.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-83pgy.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-84fcd.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-8j8dz.md)
  Creates a regex component that matches the given component zero or one times.
- [init(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-8kdq8.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-8l2ha.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-96725.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-9pgy7.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-9picp.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-9wu1h.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent, RegexRepetitionBehavior?)](./optionally/init%28_,_%29-bak6.md)
  Creates a regex component that matches the given component zero or one times.
- [init<W, C1, C2, C3, C4, C5, C6>(RegexRepetitionBehavior?, () -> some RegexComponent)](./optionally/init%28_,_%29-frqi.md)
  Creates a regex component that matches the given component zero or one times.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [RegexComponent](../Swift/regexcomponent.md)

## See Also

### Quantifiers
- [struct One](./one.md)
  A regex component that matches exactly one occurrence of its underlying component.
- [struct ZeroOrMore](./zeroormore.md)
  A regex component that matches zero or more occurrences of its underlying component.
- [struct OneOrMore](./oneormore.md)
  A regex component that matches one or more occurrences of its underlying component.
- [struct Repeat](./repeat.md)
  A regex component that matches a selectable number of occurrences of its underlying component.
- [struct Local](./local.md)
  A regex component that represents an atomic group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/optionally)*