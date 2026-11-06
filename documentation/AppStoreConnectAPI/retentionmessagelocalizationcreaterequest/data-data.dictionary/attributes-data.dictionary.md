# RetentionMessageLocalizationCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that you set that describe the new resource.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageLocalizationCreateRequest.Data.Attributes
```

## Properties

- `locale` (string) *(required)*: The locale of the header and body text. You can’t change the locale after you create the localization. For more information, see [Managing metadata in your app by using locale shortcodes](../../managing-metadata-in-your-app-by-using-locale-shortcodes.md).
- `header` (string): The heading of the retention message, up to 66 characters.
- `body` (string): The body text of the retention message, up to 144 characters.

## See Also

### Objects
- [object RetentionMessageLocalizationCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessagelocalizationcreaterequest/data-data.dictionary/attributes-data.dictionary)*