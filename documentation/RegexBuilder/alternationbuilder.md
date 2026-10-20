# AlternationBuilder

**Framework**: RegexBuilder  
**Kind**: struct  
**Role**: Structure

A custom parameter attribute that constructs regular expression alternations from closures.

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
@resultBuilder
struct AlternationBuilder
```

#### Overview

When you use a `ChoiceOf` initializer, the initializer’s closure parameter has an `AlternationBuilder` attribute, allowing you to provide multiple regular expression statements as alternatives.

## Topics

### Type Methods
- [static func buildExpression<R>(R) -> R](./alternationbuilder/buildexpression%28_%29.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-1jq94.md)
- [static func buildPartialBlock<W0, C1, W1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-1oadq.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-1vk92.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-20ao.md)
- [static func buildPartialBlock<W0, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-28nze.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, C9, W1, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-2afed.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-2q3in.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-2yatq.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-30m9e.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3571v.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-38zc3.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-39yml.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3a1qj.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3ascd.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3b47j.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3eldc.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3ibe4.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, W1, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3nzbh.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3rkqj.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-3wkc9.md)
- [static func buildPartialBlock<W0, C1>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-42jgz.md)
- [static func buildPartialBlock(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<Substring>](./alternationbuilder/buildpartialblock%28accumulated,next%29-46i6m.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-4jwp3.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-4nz0t.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-4q1xd.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-53xav.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-576fa.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-57987.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-5afat.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, W1, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-5fcrr.md)
- [static func buildPartialBlock<W1, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-5me97.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-5qva.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-5wwt0.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6074o.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-653ta.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6842g.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6anqe.md)
- [static func buildPartialBlock<W1, C1>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6hkv5.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6nfpu.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6pfu4.md)
- [static func buildPartialBlock<W1, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6tz5g.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6vjm9.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6vp0.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6x6gg.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-6yu9n.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, W1, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-70usl.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-71zj2.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-7ihw4.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-7jsg7.md)
- [static func buildPartialBlock<W0, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-815py.md)
- [static func buildPartialBlock<W0, C1, C2, C3, W1, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4?, C5?, C6?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-8a7vx.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-8dd0v.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-8e0ap.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-8pz3c.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, W1, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-90yht.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-9f39x.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-9g62e.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, W1, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5?, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-9k7s0.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, W1, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-9op0h.md)
- [static func buildPartialBlock<W0, C1, C2, W1, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3?, C4?, C5?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-9s1co.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, W1, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-b6ks.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-klfl.md)
- [static func buildPartialBlock<W0, C1, C2, C3, C4, C5, C6, C7, C8, W1, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9?, C10?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-o7ny.md)
- [static func buildPartialBlock<W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-q4oo.md)
- [static func buildPartialBlock<W0, C1, W1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28accumulated,next%29-toh7.md)
- [static func buildPartialBlock<R, W, C1, C2>(first: R) -> ChoiceOf<(W, C1?, C2?)>](./alternationbuilder/buildpartialblock%28first%29-1kh7h.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?)>](./alternationbuilder/buildpartialblock%28first%29-271vl.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?)>](./alternationbuilder/buildpartialblock%28first%29-3f6z3.md)
- [static func buildPartialBlock<R, W, C1>(first: R) -> ChoiceOf<(W, C1?)>](./alternationbuilder/buildpartialblock%28first%29-520tx.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](./alternationbuilder/buildpartialblock%28first%29-5qbok.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?)>](./alternationbuilder/buildpartialblock%28first%29-63ah5.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?)>](./alternationbuilder/buildpartialblock%28first%29-6mjz0.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](./alternationbuilder/buildpartialblock%28first%29-6vt65.md)
- [static func buildPartialBlock<R>(first: R) -> ChoiceOf<R.RegexOutput>](./alternationbuilder/buildpartialblock%28first%29-7jdle.md)
- [static func buildPartialBlock<R, W, C1, C2, C3>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?)>](./alternationbuilder/buildpartialblock%28first%29-c2a6.md)
- [static func buildPartialBlock<R, W, C1, C2, C3, C4, C5, C6, C7, C8>(first: R) -> ChoiceOf<(W, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](./alternationbuilder/buildpartialblock%28first%29-uy7q.md)

## See Also

### Builders
- [enum RegexComponentBuilder](./regexcomponentbuilder.md)
  A custom parameter attribute that constructs regular expressions from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/alternationbuilder)*