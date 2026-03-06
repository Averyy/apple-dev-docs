# AppClipAdvancedExperience.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe an Advanced App Clip Experiences resource.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperience.Attributes
```

## Topics

### Objects
- [object AppClipAdvancedExperience.Attributes.Place](appclipadvancedexperience/attributes-data.dictionary/place-data.dictionary.md)
  The place information of an advanced App Clip experience.

## Properties

- `action` (AppClipAction): The call-to-action verb that appears on the App Clip card.
- `businessCategory` (string): The business category of an advanced App Clip experience; for example, `PARKING`
- `defaultLanguage` (AppClipAdvancedExperienceLanguage): The default language for the advanced App Clip experience.
- `isPoweredBy` (boolean): A Boolean value that indicates whether the advanced App Clip experience was submitted by a platform provider that serves multiple businesses.
- `link` (uri): The invocation URL of the advanced App Clip experience.
- `place` (AppClipAdvancedExperience.Attributes.Place): The physical location you associate with the advanced App Clip experience. If you associate an advanced App Clip experience with a place, users can launch your App Clip from location-based suggestions from Siri Suggestions and the Maps app.
- `placeStatus` (string): A string that describes a place’s match status with Points of Interest (POI) in Apple Maps. `PENDING` indicates that Apple Maps is currently matching the place to a POI. `MATCHED` indicates that the provided place information matched a POI, and `NO_MATCH` indicates that the place doesn’t match a POI in Apple Maps or is in a location not supported by Apple Maps.
- `status` (string): A string that describes the status of an advanced App Clip experience. `RECEIVED` indicates that users can invoke this experience, `DEACTIVATED` indicates that the experience is deactivated and users can’t launch the App Clip with this invocation, and `APP_TRANSFER_IN_PROGRESS` indicates that the experience is part of an app that’s currently transferred to another developer.
- `version` (integer): The build version of the App Clip as an integer value; for example, `1234`.

## See Also

- [object AppClipAdvancedExperience.Relationships](appclipadvancedexperience/relationships-data.dictionary.md)
  The relationships of the Advanced App Clip Experiences resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperience/attributes-data.dictionary)*