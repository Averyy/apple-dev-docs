# Read Xcode Cloud Artifact Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the artifact Xcode Cloud created for a specific action when it performed a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves detailed information about a specific artifact Xcode Cloud created when it performed a build. Use the information provided to download the artifact and store it on your own servers. Note that the returned download URL is only valid for a limited amount of time.

##### Example Request and Response


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciartifacts-_id_)*