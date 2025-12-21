# Capture

**Framework**: RegexBuilder  
**Kind**: struct

A regex component that saves the matched substring, or a transformed result, for access in a regex match.

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
struct Capture<Output>
```

#### Overview

Use a `Capture` component to capture one part of a regex to access separately after matching. In the example below, `regex` matches a dollar sign (`"$"`) followed by one or more digits, a period (`"."`), and then two additional digits, as long as that pattern appears at the end of the line. Because the `Capture` block wraps the digits and period, that part of the match is captured separately.

```swift
let transactions = """
    CREDIT     109912311421    Payroll   $69.73
    CREDIT     105912031123    Travel   $121.54
    DEBIT      107733291022    Refund    $8.42
    """

let regex = Regex {
    "$"
    Capture {
      OneOrMore(.digit)
      "."
      Repeat(.digit, count: 2)
    }
    Anchor.endOfLine
}

// The type of each match's output is `(Substring, Substring)`.
for match in transactions.matches(of: regex) {
    print("Transaction amount: \(match.1)")
}
// Prints "Transaction amount: 69.73"
// Prints "Transaction amount: 121.54"
// Prints "Transaction amount: 8.42"
```

Each `Capture` block increases the number of components in the regex’s output type. In the example above, the capture type of each match is `(Substring, Substring)`.

By providing a transform function to the `Capture` block, you can change the type of the captured value from `Substring` to the result of the transform. This example declares `doubleValueRegex`, which converts the captured amount to a `Double`:

```swift
let doubleValueRegex = Regex {
    "$"
    Capture {
        OneOrMore(.digit)
        "."
        Repeat(.digit, count: 2)
    } transform: { Double($0)! }
    Anchor.endOfLine
}

// The type of each match's output is `(Substring, Double)`.
for match in transactions.matches(of: doubleValueRegex) {
    if match.1 >= 100.0 {
        print("Large amount: \(match.1)")
    }
}
// Prints "Large amount: 121.54"
```

Throwing an error from a `transform` closure aborts matching and propagates the error out to the caller. If you instead want to use a failable transformation, where a `nil` result participates in matching, use [`TryCapture`](trycapture.md) instead of `Capture`.

## Topics

### Initializers
- [init<W, C1>(some RegexComponent)](capture/init(_:)-1tmsz.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4>(some RegexComponent)](capture/init(_:)-2f52u.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(() -> some RegexComponent)](capture/init(_:)-3fgv4.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent)](capture/init(_:)-3iklm.md)
  Creates a capture for the given component.
- [init<W>(() -> some RegexComponent)](capture/init(_:)-3o4p2.md)
  Creates a capture for the given component.
- [init<W, C1, C2>(() -> some RegexComponent)](capture/init(_:)-46rdv.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent)](capture/init(_:)-4guoe.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent)](capture/init(_:)-53k6l.md)
  Creates a capture for the given component.
- [init<W, C1, C2>(some RegexComponent)](capture/init(_:)-5wvbp.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4>(() -> some RegexComponent)](capture/init(_:)-6972d.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5>(() -> some RegexComponent)](capture/init(_:)-6gd4p.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3>(() -> some RegexComponent)](capture/init(_:)-6w2zh.md)
  Creates a capture for the given component.
- [init<W>(some RegexComponent)](capture/init(_:)-751s0.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent)](capture/init(_:)-7adb5.md)
  Creates a capture for the given component.
- [init<W, C1>(() -> some RegexComponent)](capture/init(_:)-7gbb2.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6>(() -> some RegexComponent)](capture/init(_:)-7o3nk.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent)](capture/init(_:)-8e156.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(() -> some RegexComponent)](capture/init(_:)-8hde2.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent)](capture/init(_:)-9a7se.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(() -> some RegexComponent)](capture/init(_:)-9u8yf.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(() -> some RegexComponent)](capture/init(_:)-dm5i.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3>(some RegexComponent)](capture/init(_:)-zp0c.md)
  Creates a capture for the given component.
- [init<W, C1, C2, C3, C4, C5, C6>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-1ugzr.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-25etj.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-3466q.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-5mhxe.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-5xnic.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-6w075.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-7rcvh.md)
  Creates a capture for the given component using the specified reference.
- [init<W>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-82c2j.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-8zsdh.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-9f35e.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3>(some RegexComponent, as: Reference<W>)](capture/init(_:as:)-sg1w.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-14ci9.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-1k7ca.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-2h2hm.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-50rsk.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-57wgq.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-7pm1.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-8qyac.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-8yapk.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-9j2it.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-i2lv.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture)](capture/init(_:as:transform:)-kflo.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-186es.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-18ik6.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-1kfgs.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-1ns5b.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-1t85c.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-1vbtc.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-2fsxr.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-36nfu.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-36y0i.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-4bhm9.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-54rby.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-58e84.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-5loer.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-5nqht.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-5qnr.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-69jbe.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-6u44c.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-7ndmv.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-8l6vq.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-98vy5.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-9yayx.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(_:transform:)-qygd.md)
  Creates a capture for the given component, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-3d6el.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-3vlcx.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-4l8eh.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-51as9.md)
  Creates a capture for the given component using the specified reference.
- [init<W>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-56h1c.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-6esnr.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-7fs07.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-7rh88.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-8s7ds.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5, C6>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-9isum.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, C5>(as: Reference<W>, () -> some RegexComponent)](capture/init(as:_:)-9y6av.md)
  Creates a capture for the given component using the specified reference.
- [init<W, C1, C2, C3, C4, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-15sg2.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-1cz24.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-1e5w2.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-4elzn.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-617oo.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-68hzv.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-6h4i.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-6tdp8.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-82pi.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-c8qs.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture)](capture/init(as:_:transform:)-jvkx.md)
  Creates a capture for the given component using the specified reference, transforming with the given closure.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct TryCapture](trycapture.md)
  A regex component that attempts to transform a matched substring, saving the result if successful and backtracking if the transformation fails.
- [struct Reference](reference.md)
  A reference to a captured portion of a regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/capture)*