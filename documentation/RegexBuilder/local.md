# Local

**Framework**: RegexBuilder  
**Kind**: struct  
**Role**: Structure

A regex component that represents an atomic group.

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
struct Local<Output>
```

#### Overview

An atomic group opens a local backtracking scope which, upon successful exit, discards any remaining backtracking points from within the scope.

## Topics

### Initializers
- [init(some RegexComponent)](./local/init%28_%29-190tm.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(() -> some RegexComponent)](./local/init%28_%29-1pqmw.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent)](./local/init%28_%29-1z8ep.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4>(some RegexComponent)](./local/init%28_%29-2682m.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6>(() -> some RegexComponent)](./local/init%28_%29-3bh2x.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3>(some RegexComponent)](./local/init%28_%29-3igqu.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5>(() -> some RegexComponent)](./local/init%28_%29-3s7fi.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(() -> some RegexComponent)](./local/init%28_%29-53gbl.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(() -> some RegexComponent)](./local/init%28_%29-54x6o.md)
  Creates an atomic group with the given regex component.
- [init<W, C1>(some RegexComponent)](./local/init%28_%29-5xekw.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent)](./local/init%28_%29-6dp02.md)
  Creates an atomic group with the given regex component.
- [init(() -> some RegexComponent)](./local/init%28_%29-75o5i.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2>(() -> some RegexComponent)](./local/init%28_%29-7an8x.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4>(() -> some RegexComponent)](./local/init%28_%29-7b0cb.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3>(() -> some RegexComponent)](./local/init%28_%29-7c8wv.md)
  Creates an atomic group with the given regex component.
- [init<W, C1>(() -> some RegexComponent)](./local/init%28_%29-7o3al.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(() -> some RegexComponent)](./local/init%28_%29-8bmi6.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent)](./local/init%28_%29-8hppy.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent)](./local/init%28_%29-8i5e6.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent)](./local/init%28_%29-8nf0w.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2>(some RegexComponent)](./local/init%28_%29-8xd9f.md)
  Creates an atomic group with the given regex component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent)](./local/init%28_%29-anqj.md)
  Creates an atomic group with the given regex component.

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
- [struct OneOrMore](./oneormore.md)
  A regex component that matches one or more occurrences of its underlying component.
- [struct Repeat](./repeat.md)
  A regex component that matches a selectable number of occurrences of its underlying component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/local)*