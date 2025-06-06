# init(forDieWithSideCount:)

**Framework**: GameplayKit  
**Kind**: init

Creates a random distribution equivalent to a die with the specified number of sides.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(forDieWithSideCount sideCount: Int)
```

#### Return Value

A uniform random distribution that produces values in the range `[1, sideCount]`.

#### Discussion

Creating a random source with this method is equivalent to calling the [`init(randomSource:lowestValue:highestValue:)`](gkrandomdistribution/init(randomsource:lowestvalue:highestvalue:).md) initializer, passing a new instance of the [`GKARC4RandomSource`](gkarc4randomsource.md) class for the `source` parameter, and passing 1 and `sideCount` for the `lowestValue` and `highestValue` parameters. Because the newly created distribution uses its own [`GKRandomSource`](gkrandomsource.md) instance, the random behavior of the distribution is independent from that of other randomizers.

## Parameters

- `sideCount`: The count of sides for modeling a die; that is, the highest integer value for the random distribution to generate.

## See Also

- [class func d6() -> Self](gkrandomdistribution/d6.md)
  Creates a random distribution equivalent to a six-sided die.
- [class func d20() -> Self](gkrandomdistribution/d20.md)
  Creates a random distribution equivalent to a twenty-sided die.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/init(fordiewithsidecount:))*