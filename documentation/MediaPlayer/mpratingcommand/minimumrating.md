# minimumRating

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The minimum rating for a command.

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
var minimumRating: Float { get set }
```

```objc
@property (nonatomic, assign) float minimumRating;
```

## Discussion

The `minimumRating` property must be less than the [`maximumRating`](./maximumrating.md) property.

## See Also

### Defining maximum and minimum ratings
- [var maximumRating: Float](./maximumrating.md)
  The maximum rating for a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpratingcommand/minimumrating)*