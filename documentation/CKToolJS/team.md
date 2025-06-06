# Team

**Framework**: CKTool JS  
**Kind**: struct

Details of a developer team.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary Team {
	string teamId;
	string teamName;
	string? teamType;
};
```

#### Overview

You can find your team details in the Membership tab of the Apple Developer portal at `https://developer.apple.com`.

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { Team } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [teamId](team/teamid.md)
  Unique identifier of the developer team.
- [teamName](team/teamname.md)
  Name of the developer team.
- [teamType](team/teamtype.md)
  Type of the developer team.

## See Also

- [getSessionUser](promisesapi/getsessionuser.md)
  Returns details for the user in current session.
- [getTeams](promisesapi/getteams.md)
  Fetches a list of teams the current user is in.
- [TeamsResponse](teamsresponse.md)
  Response object for a list of teams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/team)*