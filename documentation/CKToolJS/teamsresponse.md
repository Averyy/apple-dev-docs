# TeamsResponse

**Framework**: CKTool JS  
**Kind**: struct  
**Role**: Structure

Response object for a list of teams.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
dictionary TeamsResponse {
	Team[] teams;
	string? recentTeamId;
};
```

## Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { TeamsResponse } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [recentTeamId](./teamsresponse/recentteamid.md)
  Most recently used developer `teamId`.
- [teams](./teamsresponse/teams.md)
  The array of teams fetched.

## See Also

### User and Team
- [getSessionUser](./promisesapi/getsessionuser.md)
  Returns details for the user in current session.
- [getTeams](./promisesapi/getteams.md)
  Fetches a list of teams the current user is in.
- [Team](./team.md)
  Details of a developer team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/teamsresponse)*