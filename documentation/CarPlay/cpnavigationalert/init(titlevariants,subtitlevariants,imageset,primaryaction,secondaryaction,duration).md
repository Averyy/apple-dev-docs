# init(titleVariants:subtitleVariants:imageSet:primaryAction:secondaryAction:duration:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a navigation alert.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
init(titleVariants: [String], subtitleVariants: [String]?, imageSet: CPImageSet?, primaryAction: CPAlertAction, secondaryAction: CPAlertAction?, duration: TimeInterval)
```

```objc
- (instancetype) initWithTitleVariants:(NSArray<NSString *> *) titleVariants subtitleVariants:(NSArray<NSString *> *) subtitleVariants imageSet:(CPImageSet *) imageSet primaryAction:(CPAlertAction *) primaryAction secondaryAction:(CPAlertAction *) secondaryAction duration:(NSTimeInterval) duration;
```

#### Return Value

A newly initialized navigation alert.

## Parameters

- `titleVariants`: An array of localized, displayable titles. The system selects the title that fits in the available display space.
- `subtitleVariants`: An array of localized, displayable subtitles. The system selects the title that fits in the available display space.
- `imageSet`: An image set displayed in the navigation alert. The navigation alert doesn’t support animated images. If you provide an animated image, the alert uses the first image in the animation sequence.
- `primaryAction`: The primary action and its button.
- `secondaryAction`: An optional, secondary action with its button.
- `duration`: The amount of time, in seconds, that the alert is visible. Setting the duration to 0 displays the alert until dismissed by the user.

## See Also

### Creating a Navigation Alert
- [init(titleVariants: [String], subtitleVariants: [String]?, image: UIImage?, primaryAction: CPAlertAction, secondaryAction: CPAlertAction?, duration: TimeInterval)](./init%28titlevariants,subtitlevariants,image,primaryaction,secondaryaction,duration%29.md)
  Creates a navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/init(titlevariants:subtitlevariants:imageset:primaryaction:secondaryaction:duration:))*