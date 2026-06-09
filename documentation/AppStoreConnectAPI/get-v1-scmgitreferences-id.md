# Read git reference information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Git reference.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmGitReferences/{id}`

## Parameters

- `fields[scmGitReferences]` ([string]): Additional fields to include for the Git References resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[scmRepositories]` ([string])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmgitreferences-_id_)*