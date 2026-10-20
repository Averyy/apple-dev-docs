# map(_:_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Publishes the values of two key paths as a tuple.

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
func map<T0, T1>(_ keyPath0: KeyPath<Self.Output, T0>, _ keyPath1: KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>
```

#### Return Value

A publisher that publishes the values of two key paths as a tuple.

#### Discussion

In the following example, the [`map(_:_:)`](./map%28_,_%29.md) operator uses the Swift key path syntax to access the `die1` and `die2` members of the `DiceRoll` structure published by the [`Just`](../just.md) publisher.

The downstream sink subscriber receives only these two values (as an `(Int, Int)` tuple), not the entire `DiceRoll`.

```swift
struct DiceRoll {
    let die1: Int
    let die2: Int
}

cancellable = Just(DiceRoll(die1:Int.random(in:1...6),
                            die2: Int.random(in:1...6)))
    .map(\.die1, \.die2)
    .sink { values in
        print ("Rolled: \(values.0), \(values.1) (total: \(values.0 + values.1))")
    }
// Prints "Rolled: 6, 4 (total: 10)" (or other random values).
```

## Parameters

- `keyPath0`: The key path of a property on `Output`.
- `keyPath1`: The key path of another property on `Output`.

## See Also

### Identifying properties with key paths
- [func map<T>(KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>](./map%28_%29-6sm0a.md)
  Publishes the value of a key path.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](./map%28_,_,_%29.md)
  Publishes the values of three key paths as a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/map(_:_:))*