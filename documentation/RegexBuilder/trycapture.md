# TryCapture

**Framework**: RegexBuilder  
**Kind**: struct

A regex component that attempts to transform a matched substring, saving the result if successful and backtracking if the transformation fails.

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
struct TryCapture<Output>
```

#### Overview

You use a `TryCapture` component to capture part of a match as a transformed value, when a failure to transform should mean the regex continues matching, backtracking from that point if necessary.

The code below demonstrates using `TryCapture` to include a test that the `Double` value of a capture is over a limit. In the example, `regex` matches a dollar sign (`"$"`) followed by one or more digits, a period (`"."`), and then two additional digits, as long as that pattern appears at the end of the line. The `TryCapture` block wraps the digits and period, capturing that part of the match separately and passing it to its `transform` closure. That closure converts the captured portion of the match, converts it to a `Double`, and only returns a non-`nil` value if it is over the transaction limit.

```swift
let transactions = """
    CREDIT     109912311421    Payroll   $69.73
    CREDIT     105912031123    Travel   $121.54
    DEBIT      107733291022    Refund    $8.42
    """
let transactionLimit = 100.0

let regex = Regex {
    "$"
    TryCapture {
        OneOrMore(.digit)
        "."
        Repeat(.digit, count: 2)
    } transform: { str -> Double? in
        let value = Double(str)!
        if value > transactionLimit {
            return value
        }
        return nil
    }
    Anchor.endOfLine
}
```

When the `TryCapture` block’s `transform` closure processes the three different amounts in the list of transactions, it only returns a non-`nil` value for the $121.54 transaction. Even though the capture returns an optional `Double` value, the captured value is non-optional.

```swift
// The type of each match's output is `(Substring, Double)`.
for match in transactions.matches(of: regex) {
    print("Transaction amount: \(match.1)")
}
// Prints "Transaction amount: 121.54"
```

Throwing an error from a `transform` closure aborts matching and propagates the error out to the caller. If you want to capture the `nil` results of a failable transformation, instead of continuing a search, use [`Capture`](capture.md) instead of `TryCapture`.

## Topics

### Initializers
- [init<W, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-2a4o2.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-2bjbf.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-41r67.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-4kzw6.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-674ml.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-7tqt7.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-88lf1.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-89xrg.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-8m89r.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-9p9ig.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, NewCapture>(some RegexComponent, as: Reference<NewCapture>, transform: (W) throws -> NewCapture?)](trycapture/init(_:as:transform:)-z449.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-18te8.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-1oiex.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-1q8tj.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-2akes.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-2cmjm.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-2o3dd.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-35erc.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-49jj.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-4ctec.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-4fb8m.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-55y26.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-5blap.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-5f28q.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-5qk0r.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-631wm.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-7vgez.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-7w4kc.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-8d6xo.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-8kgfm.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, NewCapture>(() -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-951zx.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, C2, C3, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-9oonc.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, C1, NewCapture>(some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(_:transform:)-t0lx.md)
  Creates a capture for the given component, attempting to transform with the given closure.
- [init<W, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-2nfnn.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-5tqfd.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-6vy4m.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-7di2q.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-7j2mj.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-7pe1b.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, C6, C7, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-85qkx.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-8byjf.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-8xl17.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, C2, C3, C4, C5, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-b8x0.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
- [init<W, C1, NewCapture>(as: Reference<NewCapture>, () -> some RegexComponent, transform: (W) throws -> NewCapture?)](trycapture/init(as:_:transform:)-p58t.md)
  Creates a capture for the given component using the specified reference, attempting to transform with the given closure.
### Instance Properties
- [var regex: Regex<Output>](trycapture/regex.md)
  The regular expression represented by this component.
### Type Aliases
- [TryCapture.RegexOutput](trycapture/regexoutput.md)
  The output type for this regular expression.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct Capture](capture.md)
  A regex component that saves the matched substring, or a transformed result, for access in a regex match.
- [struct Reference](reference.md)
  A reference to a captured portion of a regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/trycapture)*