# map(_:)

**Framework**: RealityKit  
**Kind**: method

Publishes the value of a key path.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func map<T>(_ keyPath: KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>
```

#### Return Value

A publisher that publishes the value of the key path.

#### Discussion

In the following example, the `Publisher/map(_:)-6sm0a` operator uses the Swift key path syntax to access the `die` member of the `DiceRoll` structure published by the `Just` publisher.

The downstream sink subscriber receives only the value of this `Int`, not the entire `DiceRoll`.

```None
struct DiceRoll {
    let die: Int
}

cancellable = Just(DiceRoll(die:Int.random(in:1...6)))
    .map(\.die)
    .sink {
        print ("Rolled: \($0)")
    }
// Prints "Rolled: 3" (or some other random value).
```

## Parameters

- `keyPath`: The key path of a property on  .

## See Also

- [func map<T0, T1>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>) -> Publishers.MapKeyPath2<Self, T0, T1>](scene/publisher/map(_:_:).md)
  Publishes the values of two key paths as a tuple.
- [func map<T0, T1, T2>(KeyPath<Self.Output, T0>, KeyPath<Self.Output, T1>, KeyPath<Self.Output, T2>) -> Publishers.MapKeyPath3<Self, T0, T1, T2>](scene/publisher/map(_:_:_:).md)
  Publishes the values of three key paths as a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/map(_:)-74mga)*