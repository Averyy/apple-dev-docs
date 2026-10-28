# RegexComponentBuilder

**Framework**: RegexBuilder  
**Kind**: enum  
**Role**: Enumeration

A custom parameter attribute that constructs regular expressions from closures.

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
enum RegexComponentBuilder
```

## Overview

You typically see `RegexComponentBuilder` as a parameter attribute for `Regex`- or `RegexComponent`-producing closure parameters, allowing those closures to combine multiple regular expression components. Type initializers and string algorithm methods in the RegexBuilder framework include a builder closure parameter, so that you can use regular expression components together.

## Topics

### Type Methods
- [static func buildBlock() -> Regex<Substring>](./regexcomponentbuilder/buildblock%28%29.md)
- [static func buildExpression<R>(R) -> R](./regexcomponentbuilder/buildexpression%28_%29.md)
- [static func buildLimitedAvailability<W, C1, C2>(some RegexComponent) -> Regex<(Substring, C1?, C2?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-1l3rg.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-4at76.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4, C5, C6>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?, C5?, C6?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-4hn5e.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-59bdi.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-6pyeu.md)
- [static func buildLimitedAvailability<W, C1, C2, C3>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-75sld.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-79ri4.md)
- [static func buildLimitedAvailability<W, C1>(some RegexComponent) -> Regex<(Substring, C1?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-8v501.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-9xvwl.md)
- [static func buildLimitedAvailability(some RegexComponent) -> Regex<Substring>](./regexcomponentbuilder/buildlimitedavailability%28_%29-c1mb.md)
- [static func buildLimitedAvailability<W, C1, C2, C3, C4, C5>(some RegexComponent) -> Regex<(Substring, C1?, C2?, C3?, C4?, C5?)>](./regexcomponentbuilder/buildlimitedavailability%28_%29-d693.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-14sjx.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-1kun5.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-1l56o.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-1mvah.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-1qjvk.md)
- [static func buildPartialBlock<W0>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<Substring>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2hd06.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2nr1l.md)
- [static func buildPartialBlock<W0, W1, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2p8bg.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2qewj.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3, C4, C5)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2r4ca.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2rw87.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-2v43k.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-302jc.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-31uif.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-34auc.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3cwue.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3d4xq.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3fe4r.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3iyin.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3m9by.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3qdzk.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3r0w.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3rw1u.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3uzf8.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-3vbfl.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-439as.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-48ufn.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-49qyb.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4ej74.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4ev8q.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4htjq.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4qcho.md)
- [static func buildPartialBlock<W0, C0, C1>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4tecz.md)
- [static func buildPartialBlock<W0, C0, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4vll5.md)
- [static func buildPartialBlock<W0, W1, C1>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-4w1nu.md)
- [static func buildPartialBlock<W0, C0>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-560og.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-5613o.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-5l4bx.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6ayyo.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6j8dc.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6jekf.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6nfqh.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3, C4)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6qrtp.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6u75f.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6vgmh.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-6wei8.md)
- [static func buildPartialBlock<W0, W1, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-78luz.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-7oi4x.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-8nuq5.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-8o64q.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-8t85z.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-90brb.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-92aur.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-94cff.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-95d7s.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-9d7nj.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-9dfaj.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-9fl4.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-9lklo.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-9ne33.md)
- [static func buildPartialBlock<W0, C0, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C0, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-9upqy.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-dzro.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8, C9>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-fss2.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-k1e8.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7, C8>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7, C8)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-krsh.md)
- [static func buildPartialBlock<W0, W1, C1, C2, C3, C4, C5, C6, C7>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2, C3, C4, C5, C6, C7)>](./regexcomponentbuilder/buildpartialblock%28accumulated,next%29-oglj.md)
- [static func buildPartialBlock<R>(first: R) -> Regex<R.RegexOutput>](./regexcomponentbuilder/buildpartialblock%28first%29.md)

## See Also

### Builders
- [struct AlternationBuilder](./alternationbuilder.md)
  A custom parameter attribute that constructs regular expression alternations from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/regexcomponentbuilder)*