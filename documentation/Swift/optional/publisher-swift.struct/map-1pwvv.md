# map(_:)

**Framework**: Swift  
**Kind**: method

Publishes the value of a key path.

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
func map<T>(_ keyPath: KeyPath<Self.Output, T>) -> Publishers.MapKeyPath<Self, T>
```

#### Return Value

A publisher that publishes the value of the key path.

#### Discussion

In the following example, the `Publisher/map(_:)-6sm0a` operator uses the Swift key path syntax to access the `die` member of the `DiceRoll` structure published by the `Just` publisher.

The downstream sink subscriber receives only the value of this `Int`, not the entire `DiceRoll`.

```swift
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/map(_:)-1pwvv)*