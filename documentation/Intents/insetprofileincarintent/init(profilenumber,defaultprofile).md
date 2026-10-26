# init(profileNumber:defaultProfile:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an intent to set the car’s profile.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0 (renamed: init(profileNumber:profileName:isDefaultProfile:))
- iPadOS 10.0+ - Deprecated in 11.0 (renamed: init(profileNumber:profileName:isDefaultProfile:))
- Mac Catalyst 10.0+ - Deprecated in 11.0 (renamed: init(profileNumber:profileName:isDefaultProfile:))

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
convenience init(profileNumber: Int?, defaultProfile: Int?)
```

## See Also

### Initializing the Intent Object
- [convenience init(profileNumber: Int?, profileName: String?, isDefaultProfile: Bool?, carName: INSpeakableString?)](./init%28profilenumber,profilename,isdefaultprofile,carname%29.md)
  Initializes the intent object with the specified profile name and index information.
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
- [convenience init(profileNumber: Int?, profileLabel: String?)](./init%28profilenumber,profilelabel%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileLabel: String?, isDefaultProfile: Bool?)](./init%28profilenumber,profilelabel,isdefaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileName: String?, defaultProfile: Int?)](./init%28profilenumber,profilename,defaultprofile%29.md)
  Creates an intent to set the car’s profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/init(profilenumber:defaultprofile:))*