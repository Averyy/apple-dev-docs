# init(teamInitials:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a logo object using the team’s initials or the official abbreviation of the team name.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
init(teamInitials: String)
```

```objc
- (instancetype) initWithTeamInitials:(NSString *) teamInitials;
```

## Return Value

An initialized logo object.

## Discussion

Use this initializer when you don’t have relevant artwork to display for the team’s logo.

## Parameters

- `teamInitials`: An abbreviation of the team name. If the team name has an official abbreviation in the league, specify that abbreviation. Otherwise, specify the team’s initials. Specify no more than three characters in this string. If your string contains more than three characters, this method uses only the first three.

## See Also

### Creating a team logo
- [init(teamLogo: UIImage)](./init%28teamlogo%29.md)
  Creates a logo object using a team-specific image.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo/init(teaminitials:))*