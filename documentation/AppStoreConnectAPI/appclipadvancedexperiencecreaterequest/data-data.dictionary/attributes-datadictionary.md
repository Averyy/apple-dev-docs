# AppClipAdvancedExperienceCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes you set that describe the new Advanced App Clip Experiences resource.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperienceCreateRequest.Data.Attributes
```

## Topics

### Objects
- [object AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place](appclipadvancedexperiencecreaterequest/data-data.dictionary/attributes-data.dictionary/place-data.dictionary.md)
  The place information of an advanced App Clip experience you create with this request.

## Properties

- `action` (AppClipAction): The call-to-action verb that appears on the App Clip card.
- `businessCategory` (string): The business category of an advanced App Clip experience; for example, `PARKING`
- `defaultLanguage` (AppClipAdvancedExperienceLanguage) *(required)*: The default language for the advanced App Clip experience.
- `isPoweredBy` (boolean) *(required)*: A Boolean value that indicates whether the advanced App Clip experience was submitted by a platform provider that serves multiple businesses.
- `link` (uri) *(required)*: The invocation URL of the advanced App Clip experience you’re creating.
- `place` (AppClipAdvancedExperienceCreateRequest.Data.Attributes.Place): The physical location you associate with the advanced App Clip experience. If you associate an advanced App Clip experience with a place, users can launch your App Clip from from location-based suggestions from Siri Suggestions and the Maps app.

## See Also

- [object AppClipAdvancedExperienceCreateRequest.Data.Relationships](appclipadvancedexperiencecreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperiencecreaterequest/data-data.dictionary/attributes-data.dictionary)*