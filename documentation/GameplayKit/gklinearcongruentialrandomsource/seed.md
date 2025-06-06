# seed

**Framework**: GameplayKit  
**Kind**: property

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

#### Discussion

Any two random sources initialized with the same seed value will generate the same sequence of random numbers. To replicate the behavior of an existing [`GKLinearCongruentialRandomSource`](gklinearcongruentialrandomsource.md) instance, read this property and then create a new instance by passing the resulting value to the [`init(seed:)`](gklinearcongruentialrandomsource/init(seed:).md) initializer.

For a source of high-entropy seed data, see the [`SecRandomCopyBytes(_:_:_:)`](https://developer.apple.com/documentation/Security/SecRandomCopyBytes(_:_:_:)) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gklinearcongruentialrandomsource/seed)*