# seed

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The seed data that determines the random source’s behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var seed: Data { get set }
```

```objc
@property (nonatomic, copy) NSData * seed;
```

## Discussion

Any two random sources initialized with the same seed data will generate the same sequence of random numbers. To replicate the behavior of an existing [`GKARC4RandomSource`](../gkarc4randomsource.md) instance, read this property and then create a new instance by passing the resulting data to the [`init(seed:)`](./init%28seed%29.md) initializer.

For a source of high-entropy seed data, see the [`SecRandomCopyBytes(_:_:_:)`](../../Security/secrandomcopybytes%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkarc4randomsource/seed)*