# Integrating with Roster API and Sign in with Apple

**Framework**: Roster API

Associate someone’s Managed Apple ID with their identity in Apple School Manager.

#### Overview

When your app uses doc://com.apple.documentation/documentation/sign_in_with_apple to authenticate someone, Apple checks whether that person’s Managed Apple ID is associated with an Apple School Manager (ASM) organization that’s authorized Roster API for your app. The identity token contains identifiers that you use with Roster API to fetch information about the organization and person.

For more information about decoding an identity token that you receive from Sign in with Apple, see doc://com.apple.documentation/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple. The decoded identity token is a JSON object with the fields shown in the example below.

```javascript
{
  “iss”: “https://appleid.apple.com”,
  “aud”: “com.example.testapp”,
  “exp”: 1676417226,
  “iat”: 1676330826,
  “sub”: “000264.UDRoeTAxVUppaHdNQU5HYWN6MEU5VDRUWFVQU1BV.RUtP”,
  “c_hash”: “ZIglL3bJ-8LuXX9xiAWnXQ”,
  “email”: “teacher@example.com,
  “email_verified”: “false”,
  “org_id”: “8e257987-f221-4171-887d-efead972993b”,
  “auth_time”: 1676330826,
  “nonce_supported”: true
}
```

##### Compare the Organization Identifiers

If somebody authenticates with Sign in with Apple using a Managed Apple ID, the decoded identity token includes an `org_id` claim that identifies their organization. Compare the value in token’s `org_id` with the `id` you receive from a [`Read the organization`](returns-organization-infrmation.md) request. If the two identifiers are equal, then the person who authenticated is a user in an organization that’s authorized Roster API for your app.

##### Fetch the Users Record

When the Managed Apple ID is associated with an organization that authorized Roster API for your app, the Sign in with Apple user identifier is the same as their user identifier in Roster API. Get the user identifier from the `sub` value in the decoded identity token, and pass it as the `userId` to a [`Read a user`](returns-a-specific-user-in-an-apple-school-manager-organization.md) request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/integrating-with-roster-api-and-sign-in-with-apple)*