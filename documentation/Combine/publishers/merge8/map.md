# map(_:_:_:)

**Framework**: Combine  
**Kind**: method

Publishes the values of three key paths as a tuple.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func map<T0, T1, T2>(_ keyPath0: KeyPath<Self.Output, T0>, _ keyPath1: KeyPath<Self.Output, T1>, _ keyPath2: KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>
```

#### Return Value

A publisher that publishes the values of three key paths as a tuple.

#### Discussion

In the following example, the [`map(_:_:_:)`](publisher/map(_:_:_:).md) operator uses the Swift key path syntax to access the `die1`, `die2`, and `die3` members of the `DiceRoll` structure published by the [`Just`](just.md) publisher.

The downstream sink subscriber receives only these three values (as an `(Int, Int, Int)` tuple), not the entire `DiceRoll`.

```swift
struct DiceRoll {
    let die1: Int
    let die2: Int
    let die3: Int
}

cancellable = Just(DiceRoll(die1:Int.random(in:1...6),
                            die2: Int.random(in:1...6),
                            die3: Int.random(in:1...6)))
    .map(\.die1, \.die2, \.die3)
    .sink { values in
        print ("Rolled: \(values.0), \(values.1), \(values.2) (total \(values.0 + values.1 + values.2))")
    }
// Prints "Rolled: 5, 4, 2 (total 11)" (or other random values).
```

## Parameters

- `keyPath0`: The key path of a property on  .
- `keyPath1`: The key path of a second property on  .
- `keyPath2`: The key path of a third property on  .

## See Also

- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](publishers/merge8/map(_:)-1x70.md)
  Publishes the value of a key path.
- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](publishers/merge8/map(_:_:).md)
  Publishes the values of two key paths as a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge8/map(_:_:_:))*