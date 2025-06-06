# init(seed:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a random source with the specified seed value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(seed: UInt64)
```

#### Return Value

A new, independent random source.

#### Discussion

Any two random sources initialized with the same seed data will generate the same sequence of random numbers. To replicate the behavior of an existing [`GKLinearCongruentialRandomSource`](gklinearcongruentialrandomsource.md) instance, read that instance’s [`seed`](gklinearcongruentialrandomsource/seed.md) property and then create a new instance by passing the resulting data to the [`init(seed:)`](gklinearcongruentialrandomsource/init(seed:).md) initializer.

For a source of high-entropy seed data, see the [`SecRandomCopyBytes(_:_:_:)`](https://developer.apple.com/documentation/Security/SecRandomCopyBytes(_:_:_:)) function.

## Parameters

- `seed`: A seed value for the random number generator.

## See Also

- [convenience init()](gklinearcongruentialrandomsource/init.md)
  Initializes a random source from a nondeterministic seed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gklinearcongruentialrandomsource/init(seed:))*