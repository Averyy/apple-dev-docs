# possessionIndicator

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An optional image to display next to the team in possession of the ball.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@NSCopying
var possessionIndicator: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * possessionIndicator;
```

## Discussion

For sports that have a concept of possession, this property stores the image to display next to the team in possession of the ball. For example, one team in American football has possession of the ball and drives toward the goal while the other team plays defense. This property can be `nil` if the sport doesn’t have the concept of possession, or if displaying an indicator doesn’t make sense.

## See Also

### Getting match-related details
- [var eventScore: String](./eventscore.md)
  The number of points or current score for the team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam/possessionindicator)*