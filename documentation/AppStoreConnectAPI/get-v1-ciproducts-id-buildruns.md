# List all xcode cloud builds for an xcode cloud product

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all builds Xcode Cloud performed for a specific product.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciProducts/{id}/buildRuns`

## Parameters

- `fields[builds]` ([string]): Additional fields to include for each Build Runs resource returned by the response.
- `fields[ciBuildRuns]` ([string]): Additional fields to include for each Build Runs resource returned by the response.
- `filter[builds]` ([string]): Filter the returned build runs using the ID of the related Builds resource.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Build Runs resources to return.
- `limit[builds]` (integer): The number of included Build Runs resources to return if the builds relationship is included.
- `fields[scmGitReferences]` ([string])
- `fields[ciWorkflows]` ([string])
- `fields[scmPullRequests]` ([string])
- `fields[ciProducts]` ([string])
- `sort` ([string])

## See Also

- [List all xcode cloud products](get-v1-ciproducts.md)
  Get a list of all products you created in Xcode Cloud.
- [Read xcode cloud product information](get-v1-ciproducts-_id_.md)
  Get information about a specific Xcode Cloud product.
- [List all additional repositories for an xcode cloud product](get-v1-ciproducts-_id_-additionalrepositories.md)
  List all additional Git repositories you associated with an Xcode Cloud product.
- [List additional repository IDs for a CI product](get-v1-ciproducts-_id_-relationships-additionalrepositories.md)
- [Read app information for an xcode cloud product](get-v1-ciproducts-_id_-app.md)
  Get the app in App Store Connect that’s related to an Xcode Cloud product.
- [Get the app ID for a CI product](get-v1-ciproducts-_id_-relationships-app.md)
- [List build run IDs for a CI product](get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List all primary git repositories for an xcode cloud product](get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [List primary repository IDs for a CI product](get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List all workflows for an xcode cloud product](get-v1-ciproducts-_id_-workflows.md)
  List all workflows for a specific Xcode Cloud product.
- [List workflow IDs for a CI product](get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the xcode cloud product for an app](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts-_id_-buildruns)*