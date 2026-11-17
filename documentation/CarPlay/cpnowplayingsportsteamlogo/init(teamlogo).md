# init(teamLogo:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a logo object using a team-specific image.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
init(teamLogo: UIImage)
```

```objc
- (instancetype) initWithTeamLogo:(UIImage *) teamLogo;
```

## Return Value

An initialized logo object.

## Discussion

If the team doesn’t have an official logo, use the [`init(teamInitials:)`](./init%28teaminitials%29.md) method to specify the team’s initials instead.

## Parameters

- `teamLogo`: The official logo of the team. Specify an image that is 350 by 350 points in size. This method resizes larger or smaller images to fit the expected size.

## See Also

### Creating a team logo
- [init(teamInitials: String)](./init%28teaminitials%29.md)
  Creates a logo object using the team’s initials or the official abbreviation of the team name.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo/init(teamlogo:))*