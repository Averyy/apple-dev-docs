# Validating with the Roster API test scope

**Framework**: Roster API

Use test data to ensure your integration with the Roster API works correctly.

#### Overview

Testing your Roster API integration before deployment is critical to the success of your implementation. The Roster API provides a  that you use to obtain sample user and class data for testing to ensure your integration is correct.

Use the test scope to generate an access token, then query the various endpoints of the Roster API. When the Roster API receives the request, it responds with test data that represents the dataset and provides all possible states of user and class records.

##### Configure the Test Scope

From your developer account, select Certificates, Identifiers & Profiles. When performing the steps to select the primary app identifier, choose “Roster API: Test data access” in the Organizational Data Sharing Scopes section.

Ensure the service URL has the test scope configured in the Apple Developer website. The following screenshot shows where to configure the test scope:

![A screenshot showing the Certificates, Identifiers and Profiles page of the Apple developer website.](https://docs-assets.developer.apple.com/published/df63cb83754f8edbf49d02d0d96ee0ec/media-4133355%402x.png)

##### Test the Authorization Endpoint

As explained in the WWDC 2022 session [`Discover Sign in with Apple at Work & School`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10053/), you need to generate the grant code to get the access token.

Use the following URL when creating the integration:

```other
URL: https://appleid.apple.com/auth/oauth2/v2/authorize
```

Use the following query parameters:

The URL opens the Apple OAuth consent screen. Enter your developer account credentials.

After successfully logging in, you receive the grant code in the registered redirect URI.

##### Generate the Access and Refresh Tokens

With your grant code, generate the access and refresh tokens. Create the `POST` request from your server with the following URL:

```other
https://appleid.apple.com/auth/oauth2/v2/token

```

In the request body, set the following parameters:

Set the header as follows:

```other
Content-Type: application/x-www-form-urlencoded
```

This generates both the access and refresh tokens. You receive a response like the following:

```other
{
    "access_token":"a1b054845b71446108514503d37086c7a.0.nwsw.xuSePX9jsQ6IjTq8CqMsdw",
    "token_type":"Bearer",
    "expires_in":3600,
    "refresh_token":"r23b98899c8e6466493f55ab7505d24ae.0.nwsw.WkPIjDsKblacDkVc_khN2g"
}
```

Access tokens expire after one hour. If yours expires, you can use the refresh token you receive to create a new access token. For more information, see Handle an expired token, below.

##### Perform a Request

After receiving the access token, perform a Roster API request using the test scope. Replace `[ACCESS_TOKEN]` with the token you receive from the previous step.

```other
curl --request GET \
  --url 'https://api-school.apple.com/rosterapi/v1/users?limit=2' \
  --header 'Authorization: Bearer [ACCESS_TOKEN]'
```

You receive a response like the following:

```other
{
  "users": [
    {
      "givenName": "given100",
      "middleName": "middle100",
      "familyName": "family100",
      "id": "001385.dmdTSkZEVVdLaXRjS3U2bTNJUUFMNlIzQlNHUTUz.RVB0",
      "grade": "4",
      "email": "given100family100@mytestschool.org",
      "roleLocationMapping": [
        {
          "roleName": "Student",
          "locationId": "LO:1234"
        }
      ],
      "dateCreated": "2020-07-06T20:32:00Z",
      "dateLastModified": "2022-12-13T19:46:46.404451216Z"
    },
    {
      "givenName": "given101",
      "middleName": "middle101",
      "familyName": "family101",
      "id": "001385.dmdTSkZEVVdLaXRjS3U2bTNJUUVMNlIzQlNHUTUz.RVB0",
      "roleLocationMapping": [
        {
          "roleName": "Student",
          "locationId": "LO:1234"
        }
      ],
      "dateCreated": "2020-07-06T20:32:00Z",
      "dateLastModified": "2022-12-13T19:46:46.406289073Z"
    }
  ],
  "nextPageToken": "mOG8EzKsKDOMbs2ruJa5tQ",
  "moreToFollow": true
}
```

##### Handle an Expired Access Token

If your access token expires, use the refresh token to generate a new access token.

```other
URL: https://appleid.apple.com/auth/oauth2/v2/token
Request Type: POST
Request Body:
client_id="Your client ID"
client_secret="Your Client secret"
grant_type=refresh_token
refresh_token="The refresh token received"

Headers:
Content-Type: application/x-www-form-urlencoded
```

You receive the following response:

```other
{
    "access_token":"a1b054845b71446108514503d37086c7a.0.nwsw.xuSePX9jsQ6IjTq8CqMsdw",
    "token_type":"Bearer",
    "expires_in":3600
}
```

These steps describe how to fetch sample user and class data for testing the Roster API. Follow the same steps to generate the access and refresh tokens for production. Ensure that the scopes you request for production are for `edu.users.read` and `edu.classes.read`.

## See Also

- [Obtaining information about people and classes](obtaining-information-about-people-and-classes.md)
  Prepare your app to request organizational information from a server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/validating-with-the-roster-api-test-scope)*