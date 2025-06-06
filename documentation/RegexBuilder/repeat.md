# Repeat

**Framework**: RegexBuilder  
**Kind**: struct

A regex component that matches a selectable number of occurrences of its underlying component.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct Repeat<Output>
```

## Topics

### Initializers
- [init<W, C1, C2, C3, C4, C5, C6>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-1bcjh.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-1qgnj.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-24n0n.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-2ev8z.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-3ghwd.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-3mo6.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-545c4.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-76l8q.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-7adwb.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-7lskd.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-7qz0e.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-7sn7t.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-80rd3.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-83kcm.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-8574u.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-891vb.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-8cwmc.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-8zx0q.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-947au.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-9h724.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init(some RangeExpression<Int>, RegexRepetitionBehavior?, () -> some RegexComponent)](repeat/init(_:_:_:)-9tzos.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent, some RangeExpression<Int>, RegexRepetitionBehavior?)](repeat/init(_:_:_:)-rxdn.md)
  Creates a regex component that matches the given component repeated a number of times specified by the given range expression.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent, count: Int)](repeat/init(_:count:)-1qk17.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent, count: Int)](repeat/init(_:count:)-21lm6.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent, count: Int)](repeat/init(_:count:)-2domp.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent, count: Int)](repeat/init(_:count:)-2q199.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent, count: Int)](repeat/init(_:count:)-4dhzv.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2>(some RegexComponent, count: Int)](repeat/init(_:count:)-56csz.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1>(some RegexComponent, count: Int)](repeat/init(_:count:)-62ivb.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init(some RegexComponent, count: Int)](repeat/init(_:count:)-82evl.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4>(some RegexComponent, count: Int)](repeat/init(_:count:)-8cqm4.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3>(some RegexComponent, count: Int)](repeat/init(_:count:)-9b88v.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent, count: Int)](repeat/init(_:count:)-9racn.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-1g72m.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-1lb2y.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-5tyx7.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-7kfzx.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-7ueje.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-80zg2.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-8n0o0.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-8z2mq.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-96dkt.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-9nywm.md)
  Creates a regex component that matches the given component repeated the specified number of times.
- [init<W, C1, C2, C3, C4, C5>(count: Int, () -> some RegexComponent)](repeat/init(count:_:)-9snpn.md)
  Creates a regex component that matches the given component repeated the specified number of times.
### Instance Properties
- [var regex: Regex<Output>](repeat/regex.md)
  The regular expression represented by this component.
### Type Aliases
- [typealias RegexOutput](repeat/regexoutput.md)
  The output type for this regular expression.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct One](one.md)
  A regex component that matches exactly one occurrence of its underlying component.
- [struct Optionally](optionally.md)
  A regex component that matches zero or one occurrences of its underlying component.
- [struct ZeroOrMore](zeroormore.md)
  A regex component that matches zero or more occurrences of its underlying component.
- [struct OneOrMore](oneormore.md)
  A regex component that matches one or more occurrences of its underlying component.
- [struct Local](local.md)
  A regex component that represents an atomic group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/repeat)*