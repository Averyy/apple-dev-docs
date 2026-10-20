# OneOrMore

**Framework**: RegexBuilder  
**Kind**: struct  
**Role**: Structure

A regex component that matches one or more occurrences of its underlying component.

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
struct OneOrMore<Output>
```

## Topics

### Initializers
- [init<W, C1, C2, C3>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-17cwr.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-1bnur.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-1fq85.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-21xfx.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-2o52m.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-2odtm.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-32m10.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-3flos.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-3tvh3.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-4qbv9.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-5helk.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-68oxd.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-6fm8e.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1>(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-6mkp4.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-6pzxz.md)
  Creates a regex component that matches the given component one or more times.
- [init(RegexRepetitionBehavior?, () -> some RegexComponent)](./oneormore/init%28_,_%29-7o7ll.md)
  Creates a regex component that matches the given component one or more times.
- [init(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-82w2k.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-84ep2.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-9eoi5.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-9f4e8.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-9qi4l.md)
  Creates a regex component that matches the given component one or more times.
- [init<W, C1, C2, C3, C4>(some RegexComponent, RegexRepetitionBehavior?)](./oneormore/init%28_,_%29-yc32.md)
  Creates a regex component that matches the given component one or more times.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [RegexComponent](../Swift/regexcomponent.md)

## See Also

### Quantifiers
- [struct One](./one.md)
  A regex component that matches exactly one occurrence of its underlying component.
- [struct Optionally](./optionally.md)
  A regex component that matches zero or one occurrences of its underlying component.
- [struct ZeroOrMore](./zeroormore.md)
  A regex component that matches zero or more occurrences of its underlying component.
- [struct Repeat](./repeat.md)
  A regex component that matches a selectable number of occurrences of its underlying component.
- [struct Local](./local.md)
  A regex component that represents an atomic group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/oneormore)*