# init(profileNumber:profileName:isDefaultProfile:carName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified profile name and index information.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 12.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
convenience init(profileNumber: Int? = nil, profileName: String? = nil, isDefaultProfile: Bool? = nil, carName: INSpeakableString? = nil)
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to restore settings from a profile. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `profileNumber`: An integer number that indicates which profile to use. This value represents the index of the profile in your system. The index can be a soft index inside your vehicle’s electronics systems or it can correspond to physical buttons that the user presses.
- `profileName`: The name of the profile. Specify `nil` when creating a profile based on a numerical index.
- `isDefaultProfile`: A Boolean value that indicates whether the profile should become the default profile.
- `carName`: The name of the car associated with the profile.

## See Also

### Initializing the Intent Object
- [convenience init(profileNumber: Int?, profileLabel: String?, defaultProfile: Int?)](./init%28profilenumber,profilelabel,defaultprofile%29.md)
  Creates the intent object with the specified profile name and index information.
- [convenience init(defaultProfile: Int?)](./init%28defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileLabel: String?)](./init%28profilelabel%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileLabel: String?, defaultProfile: Int?)](./init%28profilelabel,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileLabel: String?, isDefaultProfile: Bool?)](./init%28profilelabel,isdefaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileName: String?, defaultProfile: Int?)](./init%28profilename,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, defaultProfile: Int?)](./init%28profilenumber,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileLabel: String?)](./init%28profilenumber,profilelabel%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileLabel: String?, isDefaultProfile: Bool?)](./init%28profilenumber,profilelabel,isdefaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileName: String?, defaultProfile: Int?)](./init%28profilenumber,profilename,defaultprofile%29.md)
  Creates an intent to set the car’s profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/init(profilenumber:profilename:isdefaultprofile:carname:))*