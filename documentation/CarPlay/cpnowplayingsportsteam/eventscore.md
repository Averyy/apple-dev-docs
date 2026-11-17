# eventScore

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The number of points or current score for the team.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var eventScore: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * eventScore;
```

## Discussion

The amount of text CarPlay can show depends on the available space, but is typically no more than three to five characters.

## See Also

### Getting match-related details
- [var possessionIndicator: UIImage?](./possessionindicator.md)
  An optional image to display next to the team in possession of the ball.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam/eventscore)*