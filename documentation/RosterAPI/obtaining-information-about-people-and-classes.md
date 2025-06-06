# Obtaining information about people and classes

**Framework**: Roster API

Prepare your app to request organizational information from a server.

#### Overview

Roster API gives you access to information about the people and classes within an Apple School Manager (ASM) organization. To accomplish this, register for access, then perform queries to obtain the users and classes in that organization.

##### Plan Your Integration Design

When planning the design for the integration, create roles that allow specific accounts to perform the steps for integrating your app with Roster API. Provide only those roles with the privileges to perform create, read, update, and delete operations for the integration. For example, in ASM, only accounts that have administrator or site-manager roles can authorize an app to use Roster API.

Consider that there’s only one configuration at the organizational level. Accounts belonging to the roles with privileges work with this single configuration. This means that any changes that one privileged account makes are visible to other privileged accounts.

##### Select the Primary App Id

Use your credentials to log in to the [`Apple Developer website`](https://developer.apple.comhttp://developer.apple.com/), then choose Certificates, IDs & Profiles > Services, and click the Configure button in the Account & Organizational Data Sharing section.

![A screenshot of the Certificates, Identifiers and Profiles page with an outline around the Account and Organizational Data Sharing section.](https://docs-assets.developer.apple.com/published/d5dbdf6a52e482d0a43ef91ca688c9b6/media-4113871%402x.png)

Click the Add button (+) to the right of Configurations, or click the Configure button in the Get Started with Account & Organizational Data Sharing section.

![A screenshot of the Certificates, Identifiers and Profiles  page with an outline around Configurations in the Get Started with Account and Organizational Data Sharing section.](https://docs-assets.developer.apple.com/published/399f868720643f9967d43a42d2818f41/media-4113870%402x.png)

Choose the primary App ID from the drop-down menu, then click Continue.

![A screenshot showing the Primary App ID drop-down menu in the Account and Organizational Data Sharing: Configuration section of the Certificates, Identifiers and Profiles page.](https://docs-assets.developer.apple.com/published/afeeacda4d208f3e3afc3a728441b5f4/media-4113867%402x.png)

##### Set the Return Urls

Return URLs receive the grant code after successfully authorizing with Apple. From the Organizational Data Sharing Scopes options, select Roster API: User access, Roster API: Class access, and Roster API: Test Data access.  For more information about the test data access scope, see [`Validating with the Roster API test scope`](validating-with-the-roster-api-test-scope.md).

Add your return URLs in the Return URLs section, then enter a URL for the Server to Server Notification Endpoint so you can receive updates about people and accounts.

![A screenshot showing the Organizational Data Sharing Scopes and Return URLs areas of the Provide additional configuration details section for the Account and Organizational Data Sharing: Configuration section on the Certificates, Identifiers and Profiles page. In the Organizational Data Sharing Scopes area, the Roster API: User access, Roster API: Class access, and Roster API: Test Data access options are selected. In the Return URLs area, there is an example URL selected for placement in the text field.](https://docs-assets.developer.apple.com/published/df63cb83754f8edbf49d02d0d96ee0ec/media-4113869%402x.png)

Review your configuration and click Confirm.

![A screenshot of a confirmation screen with a summary of the primary bundle ID, Server to Server Notification Endpoint URL, and Return URLs. There is an outline around the Confirm button.](https://docs-assets.developer.apple.com/published/5185a3919d59fc55971b334968fb5c2d/media-4113872%402x.png)

##### Generate the Client Secret

Before you can generate the access token, you’ll first need to generate the client secret, which you’ll need to create the token. See [`Creating a client secret`](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/creating-a-client-secret).

Next, choose an existing key, or create a new key by clicking the Add button (+).

![A screenshot showing the Certificates, Identifiers and Profiles page with the Keys item highlighted and two keys named TestKey1 and TestKey2.](https://docs-assets.developer.apple.com/published/68bf28ffae2c9bb64d5fdb72ab2912a6/media-4113874%402x.png)

Enter a key name if you’re creating a new key, select Account & Organizational Data Sharing, and click Continue.

![A screenshot showing the Register a New Key section of the Certificates, Identifiers and Profiles page. There are outlines around the Key Name field, which has an entry of Organizational Data Sharing Key, and the Account and Organizational Data Sharing option, which is selected.](https://docs-assets.developer.apple.com/published/f6daee9ef9ea7409f129f9b4920f1ba2/media-4113866%402x.png)

Review the information and then click Register to register the key.

![A screenshot showing the Register a New Key section of the Certificates, Identifiers and Profiles  page. The selected key is enabled and there’s an outline around the Register button.](https://docs-assets.developer.apple.com/published/aacd1d9026520fef8ebe409034a3709a/media-4113868%402x.png)

Click Download, then set up a client secret. See [`Creating a client secret`](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/creating-a-client-secret).

![A screenshot showing the Download Your Key section of the Certificates, Identifiers and Profiles page. The key is available to download and there’s an outline around the Download button. A warning says “After downloading your key, it cannot be re-downloaded as the server copy is removed. If you are not prepared to download your key at this time, click Done and download it at a later time. Be sure to save a backup of your key in a secure place”.](https://docs-assets.developer.apple.com/published/6b4aba8ecbe7707bc654cc69fe1b00e0/media-4113873%402x.png)

##### Validate Using the Test Scope

To ensure your integration works correctly, test it before providing it to users. See [`Validating with the Roster API test scope`](validating-with-the-roster-api-test-scope.md).

##### Receive Revocation Notifications

ASM organizations can set up integration with the supported apps to import information about people and classes.

If an organization decides to revoke an app, Apple sends out a revocation notification to the URL you configures as the Server to Server Notification Endpoint. After receiving the  notification, remove all data associated with that organization.

The following is an example revocation notification request:

```other
{
    "iss": "https://appleid.apple.com/auth/oauth2/v2"
    "aud": "[CLIENT_ID]",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": [
        {
            "type": "consent-revoked",
            "sub": "001273.YVlIczRoMFRGbll4ODIzRUV0M2NLNkFRM0VHUTdQ.RVBY",
            "org_id": "8e257987-f221-4171-887d-efead972993b",
            "scopes": "edu.classes.read edu.users.read"
            "event_time": 1508184845
        }
    ]
}
```

Information for `org_id` and `scopes` are part of the payload. Use `org_id` to remove all data associated with the organization.

Use the `/rosterapi/v1/organization` endpoint to determine the `org_id` when obtaining user and class information for an organization. The following is a sample response:

```other
{
    "id": "8e257987-f221-4171-887d-efead972993b",
    "type": "EDUCATION",
    "name": "Apple School Manager Test Organization",
    "dateCreated": "2016-07-26T18:11:51Z",
    "dateLastModified": "2016-07-26T18:11:51Z", 
    "domains": [{"name": "mytestschool.org", "isVerified": false}]
}
```

Use `id` as the identifier to associate records to a certain organization. When the revocation notification arrives, delete those records associated with the organization that matches `org_id`.

##### Synchronize Data with Apple School Manager

Apple synchronizes data in ASM with authorized student information systems every 24 hours. Fetch data using Roster API once every 24 hours to have the most up to date data in your app. If you need to reduce your resource usage, consider fetching data less frequently, for example once every 48 hours or once every week.

Design your synchronization to handle class and roster updates. When someone removes a student from a class in ASM, or deletes a class, subsequent requests to [`List users in a class`](returns-a-users-for-an-apple-school-manager-class.md) and [`List classes`](returns-a-list-of-classes-for-an-apple-school-manager-organization.md) don’t include the removed items. Consider whether to show teachers existing data and give them the option to remove it manually, or automatically remove the deleted records.

## See Also

- [Validating with the Roster API test scope](validating-with-the-roster-api-test-scope.md)
  Use test data to ensure your integration with the Roster API works correctly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/obtaining-information-about-people-and-classes)*