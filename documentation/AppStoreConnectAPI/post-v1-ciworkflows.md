# Create a Workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a new Xcode Cloud workflow for an Xcode Cloud product.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below creates a new workflow that performs the archive action. App Store Connect returns the `201` HTTP status code to indicate the successful creation of the workflow and returns information about the workflow. Use the data to access additional information or to start a new build.

##### Example Request and Response

## Request Body

The request body you use to create a new Xcode Cloud workflow.

## See Also

- [Update an Xcode Cloud Workflow](patch-v1-ciworkflows-_id_.md)
  Make changes to an Xcode Cloud workflow.
- [Delete a Workflow](delete-v1-ciworkflows-_id_.md)
  Delete an Xcode Cloud workflow and all of its associated data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-ciworkflows)*