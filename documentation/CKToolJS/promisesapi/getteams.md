# getTeams

**Framework**: CKTool JS  
**Kind**: method

Fetches a list of teams the current user is in.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise getTeams();
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: TeamsResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

If successful, the result contains a `TeamsResponse` object. For more information about teams, see `Team`.

## See Also

- [getSessionUser](promisesapi/getsessionuser.md)
  Returns details for the user in current session.
- [Team](team.md)
  Details of a developer team.
- [TeamsResponse](teamsresponse.md)
  Response object for a list of teams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/getteams)*