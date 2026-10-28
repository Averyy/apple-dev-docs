# seed

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The seed value that determines the random source’s behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var seed: UInt64 { get set }
```

```objc
@property (nonatomic, assign) uint64_t seed;
```

## Discussion

Any two random sources initialized with the same seed value will generate the same sequence of random numbers. To replicate the behavior of an existing [`GKLinearCongruentialRandomSource`](../gklinearcongruentialrandomsource.md) instance, read this property and then create a new instance by passing the resulting value to the [`init(seed:)`](./init%28seed%29.md) initializer.

For a source of high-entropy seed data, see the [`SecRandomCopyBytes(_:_:_:)`](../../Security/secrandomcopybytes%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gklinearcongruentialrandomsource/seed)*