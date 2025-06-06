# getSessionUser

**Framework**: CKTool JS  
**Kind**: method

Returns details for the user in current session.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise getSessionUser(
	GetSessionUserParams params
);
```

#### Return Value

A `CancellablePromise` with the following resolutions.

#### Discussion

If the promise is successful, it will resolve with one of the following dictionaries:

- `{ statusCode: 200; result: CKDBSessionUserResponse }`

The promise may reject and throw the following:

- `DocumentedResponseError`, if the HTTP status code is 421. The result member will be a dictionary conforming to AuthenticationRequiredError.
- `DocumentedResponseError`, if the HTTP status code is none of the above and in the range 400 to 599. The result member will be a dictionary conforming to RequestError.
- `ValidationError`, if the parameters to the method are incorrect.
- A `FetchError` descendant, if there is a problem with the network request. A reference to the request object can be used to examine the underlying cause.

#### Discussion

The `params` dictionary has the following properties:

```javascript
dictionary GetSessionUserParams {
  string containerId;
  CKEnvironment environment;
}
```

- `containerId`: The container identifier. See `Container`.
- `environment`: The container environment. For valid values, see `CKEnvironment`.

If successful, the returned response contains a `CKDBSessionUserResponse` object with the current user information. If the user hasn’t authenticated yet or if their authentication has expired, the server returns an `AuthenticationRequiredError` error with a `redirectUrl` that your app can use to re-authenticate the user.

## Parameters

- `params`: A dictionary as described in the Discussion section.

## See Also

- [getTeams](promisesapi/getteams.md)
  Fetches a list of teams the current user is in.
- [Team](team.md)
  Details of a developer team.
- [TeamsResponse](teamsresponse.md)
  Response object for a list of teams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi/getsessionuser)*