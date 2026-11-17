# logo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image with the team’s logo.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@NSCopying
var logo: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * logo;
```

## Discussion

This property contains an image that is 350 by 350 points in size. If you initialize the logo object with the team’s initials, this property is `nil`.

## See Also

### Getting the logo content
- [var initials: String?](./initials.md)
  The team’s initials or official team-name abbreviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo/logo)*