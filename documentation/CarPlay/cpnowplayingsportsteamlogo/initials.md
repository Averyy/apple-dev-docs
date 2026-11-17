# initials

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The team’s initials or official team-name abbreviation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var initials: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * initials;
```

## Discussion

This property contains only the first three characters of the string you specify at initialization time. If you initialize the logo object with an image, this property is `nil`.

## See Also

### Getting the logo content
- [var logo: UIImage?](./logo.md)
  The image with the team’s logo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo/initials)*