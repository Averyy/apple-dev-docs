# Modify an End User License Agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the text or territories for your custom end user license agreement.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to change the license agreement text or associate the agreement with different App Store territories.

In the following example the request contains a blank value for the `agreementText` attribute. Replace that attribute value with your actual agreement text.

If you change the territories relationship, the new territories replace the original territories.

##### Change the Text of a License Agreement

##### Replace the Territories of a License Agreement with Japan and Canada

## See Also

- [Create an End User License Agreement](post-v1-enduserlicenseagreements.md)
  Add a custom end user license agreement (EULA) to an app and configure the territories to which it applies.
- [Delete an End User License Agreement](delete-v1-enduserlicenseagreements-_id_.md)
  Delete the custom end user license agreement that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-enduserlicenseagreements-_id_)*