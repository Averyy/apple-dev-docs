# init(seed:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a random source with the specified seed data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(seed: Data)
```

```objc
- (instancetype) initWithSeed:(NSData *) seed;
```

#### Return Value

A new, independent random source.

#### Discussion

Any two random sources initialized with the same seed data will generate the same sequence of random numbers. To replicate the behavior of an existing [`GKARC4RandomSource`](../gkarc4randomsource.md) instance, read that instance’s [`seed`](./seed.md) property and then create a new instance by passing the resulting data to the [`init(seed:)`](./init%28seed%29.md) initializer.

For a source of high-entropy seed data, see the [`SecRandomCopyBytes(_:_:_:)`](../../Security/secrandomcopybytes%28_,_,_%29.md) function.

## Parameters

- `seed`: A data object containing seed values for the random number generator.

## See Also

### Creating a Random Source
- [convenience init()](./init%28%29.md)
  Initializes a random source from a nondeterministic seed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkarc4randomsource/init(seed:))*