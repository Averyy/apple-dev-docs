# Obtaining an API Token for an iCloud Container

**Framework**: CloudKit

Generate an API token to access CloudKit web services or use CloudKit JS.

#### Overview

With CloudKit, you can store data in iCloud and sync it across Apple devices. To access iCloud data from the web or other platforms, you can use [`CloudKit JS`](https://developer.apple.com/documentation/CloudKitJS) or [`CloudKit Web Services`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/) after obtaining a token.

##### Select Api Access for Your Container

Use your web browser to access the CloudKit Database app:

1. Sign in to the CloudKit Console at [`https://icloud.developer.apple.com/`](https://developer.apple.comhttps://icloud.developer.apple.com/).
2. Select the CloudKit Database app.
3. In the top section, choose your app’s container from the list.
4. In the Settings section on the left, select Tokens & Keys.

![A screenshot showing a selected container in the CloudKit Database app. The screenshot highlights the Tokens & Keys menu item in the Settings section on the left.](https://docs-assets.developer.apple.com/published/be18961ab64d83fa1141ebc118170536/media-3699104%402x.png)

##### Create the Api Token

To obtain your container’s API token:

1. From the Tokens & Keys section for your container, click the New API Token button. The detail area in the right panel shows an entry form for the new token.
2. Enter the name for the API token.
3. To specify a custom URL to load after the user signs in using their Apple ID, choose URL Redirect and http:// from the Sign in Callback field and enter a custom URL.
4. To restrict the domains that can access your app’s container using CloudKit web services, choose “Only the following domain(s) from the Allowed Origins field”, and enter a domain.
5. To add a description, type it in the Notes field.
6. Click the Save Changes button.

![A screenshot showing the CloudKit Database app API access management page the for selected container.](https://docs-assets.developer.apple.com/published/bcac804a98038eb7889671279fe61b2f/media-3699263%402x.png)

## See Also

- [Inspecting and Editing an iCloud Container’s Schema](inspecting-and-editing-an-icloud-container-s-schema.md)
  Review and edit the schema for your app’s container using the CloudKit Database app.
- [Handling an iCloud Container’s Data](handling-an-icloud-container-s-data.md)
  Inspect and manage your app’s iCloud container data using the CloudKit Database app.
- [Deploying an iCloud Container’s Schema](deploying-an-icloud-container-s-schema.md)
  Reset your container’s state during development and deploy your container’s schema to production.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/obtaining-an-api-token-for-an-icloud-container)*