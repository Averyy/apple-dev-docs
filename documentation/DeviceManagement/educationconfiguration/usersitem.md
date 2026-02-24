# EducationConfiguration.UsersItem

**Framework**: Device Management  
**Kind**: dictionary

A user in the organization.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.14+

## Declaration

```swift
object EducationConfiguration.UsersItem
```

## Properties

- `AppleID` (string): The Managed Apple Account for this user. Not required to configure Classroom, but if set the system uses it. Required to configure the Shared iPad login screen.
- `FamilyName` (string): The family name of the user.
- `FullScreenImageURL` (string): Deprecated in iOS 9.3.1 and later. The URL pointing to an image of the user. The system uses the  `ResourcePayloadCertificateUUID` identity certificate or the MDM client identity to perform authentication when fetching the specified resource.
- `GivenName` (string): The given name of the user.
- `Identifier` (string) *(required)*: The unique identifier for a user in the organization.
- `ImageURL` (string): A string that contains a URL pointing to an image of the user. The system displays this image in the iOS login screen and in the Classroom app. The recommended resolution is 256 x 256 pixels (512 x 512 pixels on a 2x device). The recommended formats are JPEG, PNG, and TIFF. The system uses the `ResourcePayloadCertificateUUID` identity certificate or the MDM client identity to perform authentication when fetching the image.
- `Name` (string) *(required)*: The name of the user.
- `PasscodeType` (string): The type of passcode UI to show when the user is at the Login Window.
- `PhoneticFamilyName` (string): The user’s phonetic family name. The system uses this name to sort users in the Classroom app and the Shared iPad login screen.
- `PhoneticGivenName` (string): The user’s phonetic given name. The system uses this name to sort users in the Classroom app and the Shared iPad Login Screen.

## See Also

- [object EducationConfiguration.DepartmentsItem](educationconfiguration/departmentsitem.md)
  A department in the organization.
- [object EducationConfiguration.DeviceGroupsItem](educationconfiguration/devicegroupsitem.md)
  A device group in the organization.
- [object EducationConfiguration.GroupsItem](educationconfiguration/groupsitem.md)
  An array of dictionaries defining groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/educationconfiguration/usersitem)*