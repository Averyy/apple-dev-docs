# Create an End User License Agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a custom end user license agreement (EULA) to an app and configure the territories to which it applies.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to associate a custom license agreement with an app in the specified App Store territories. Any other territories will use the standard Apple-provided license agreement.

In the following example the request contains a blank value for the `agreementText` attribute. Replace that attribute value with your actual agreement text.

##### Create a Custom License Agreement for Usa and China

## See Also

- [Modify an End User License Agreement](patch-v1-enduserlicenseagreements-_id_.md)
  Update the text or territories for your custom end user license agreement.
- [Delete an End User License Agreement](delete-v1-enduserlicenseagreements-_id_.md)
  Delete the custom end user license agreement that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-enduserlicenseagreements)*