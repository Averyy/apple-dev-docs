# AlternationBuilder

**Framework**: RegexBuilder  
**Kind**: struct

A custom parameter attribute that constructs regular expression alternations from closures.

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
@resultBuilder
struct AlternationBuilder
```

#### Overview

When you use a `ChoiceOf` initializer, the initializer’s closure parameter has an `AlternationBuilder` attribute, allowing you to provide multiple regular expression statements as alternatives.

## Topics

### Type Methods
- [static func buildExpression<R>(R) -> R](alternationbuilder/buildexpression(_:).md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?)>](alternationbuilder/buildpartialblock(accumulated:next:)-1jq94.md)
- [static func buildPartialBlock<W0, C1, W1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?)>](alternationbuilder/buildpartialblock(accumulated:next:)-1oadq.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-1vk92.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](alternationbuilder/buildpartialblock(accumulated:next:)-20ao.md)
- [static func buildPartialBlock<W0, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3)>](alternationbuilder/buildpartialblock(accumulated:next:)-28nze.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, C9, W1, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-2afed.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?)>](alternationbuilder/buildpartialblock(accumulated:next:)-2q3in.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?)>](alternationbuilder/buildpartialblock(accumulated:next:)-2yatq.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-30m9e.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3571v.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7)>](alternationbuilder/buildpartialblock(accumulated:next:)-38zc3.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-39yml.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3a1qj.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3ascd.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3b47j.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3eldc.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3ibe4.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, W1, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3nzbh.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3rkqj.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-3wkc9.md)
- [static func buildPartialBlock<W0, C1>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1)>](alternationbuilder/buildpartialblock(accumulated:next:)-42jgz.md)
- [static func buildPartialBlock(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<Substring>](alternationbuilder/buildpartialblock(accumulated:next:)-46i6m.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-4jwp3.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-4nz0t.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-4q1xd.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6)>](alternationbuilder/buildpartialblock(accumulated:next:)-53xav.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-576fa.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?)>](alternationbuilder/buildpartialblock(accumulated:next:)-57987.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-5afat.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, W1, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-5fcrr.md)
- [static func buildPartialBlock<W1, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?)>](alternationbuilder/buildpartialblock(accumulated:next:)-5me97.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-5qva.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5)>](alternationbuilder/buildpartialblock(accumulated:next:)-5wwt0.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6074o.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-653ta.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6842g.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6anqe.md)
- [static func buildPartialBlock<W1, C1>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6hkv5.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](alternationbuilder/buildpartialblock(accumulated:next:)-6nfpu.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6pfu4.md)
- [static func buildPartialBlock<W1, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6tz5g.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6vjm9.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6vp0.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6x6gg.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?)>](alternationbuilder/buildpartialblock(accumulated:next:)-6yu9n.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, W1, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-70usl.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-71zj2.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-7ihw4.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-7jsg7.md)
- [static func buildPartialBlock<W0, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2)>](alternationbuilder/buildpartialblock(accumulated:next:)-815py.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?)>](alternationbuilder/buildpartialblock(accumulated:next:)-8a7vx.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-8dd0v.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?)>](alternationbuilder/buildpartialblock(accumulated:next:)-8e0ap.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4)>](alternationbuilder/buildpartialblock(accumulated:next:)-8pz3c.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?)>](alternationbuilder/buildpartialblock(accumulated:next:)-90yht.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-9f39x.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-9g62e.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-9k7s0.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, W1, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8?)>](alternationbuilder/buildpartialblock(accumulated:next:)-9op0h.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?)>](alternationbuilder/buildpartialblock(accumulated:next:)-9s1co.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-b6ks.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?)>](alternationbuilder/buildpartialblock(accumulated:next:)-klfl.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, W1, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9?, C10?)>](alternationbuilder/buildpartialblock(accumulated:next:)-o7ny.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-q4oo.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(accumulated:next:)-toh7.md)
- [static func buildPartialBlock<R, W, C1, C2>(first: R) -> ChoiceOf<(W, C1?, C2?)>](alternationbuilder/buildpartialblock(first:)-1kh7h.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?)>](alternationbuilder/buildpartialblock(first:)-271vl.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?)>](alternationbuilder/buildpartialblock(first:)-3f6z3.md)
- [static func buildPartialBlock<R, W, C1>(first: R) -> ChoiceOf<(W, C1?)>](alternationbuilder/buildpartialblock(first:)-520tx.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](alternationbuilder/buildpartialblock(first:)-5qbok.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?)>](alternationbuilder/buildpartialblock(first:)-63ah5.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?)>](alternationbuilder/buildpartialblock(first:)-6mjz0.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](alternationbuilder/buildpartialblock(first:)-6vt65.md)
- [static func buildPartialBlock<R>(first: R) -> ChoiceOf<R.RegexOutput>](alternationbuilder/buildpartialblock(first:)-7jdle.md)
- [static func buildPartialBlock<R, W, C1, C2, C3>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?)>](alternationbuilder/buildpartialblock(first:)-c2a6.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7, C8>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](alternationbuilder/buildpartialblock(first:)-uy7q.md)

## See Also

- [enum RegexComponentBuilder](regexcomponentbuilder.md)
  A custom parameter attribute that constructs regular expressions from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/alternationbuilder)*