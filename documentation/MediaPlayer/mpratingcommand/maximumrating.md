# maximumRating

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The maximum rating for a command.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var maximumRating: Float { get set }
```

```objc
@property (nonatomic, assign) float maximumRating;
```

#### Discussion

The `maximumRating` property must be greater than the [`minimumRating`](./minimumrating.md) property.

## See Also

### Defining maximum and minimum ratings
- [var minimumRating: Float](./minimumrating.md)
  The minimum rating for a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpratingcommand/maximumrating)*