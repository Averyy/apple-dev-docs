# INSetProfileInCarIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to change the user’s vehicle environment settings to the ones from the specified profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetProfileInCarIntent
```

```objc
@interface INSetProfileInCarIntent : INIntent
```

#### Overview

Automotive vendors whose cars support the saving of seat and other environment settings can add support for this intent to an Intents extension that they ship with their automotive apps. When users want to restore settings from a profile, SiriKit creates an [`INSetProfileInCarIntent`](./insetprofileincarintent.md) object and delivers it to the app’s Intents extension. You use the intent object to get the name or index of the profile whose settings you use to configure the vehicle.

You’re responsible for determining which settings to save and restore with user profiles. You can restore seat-related settings, climate control settings, defroster settings, radio settings, other settings in your vehicle, or any combination of those settings. Siri handles only the name or index of the profile and doesn’t ask you to provide a list of the settings that you restored. Users can restore settings regardless for whether the profile was originally created through Siri or through your vehicle’s built-in interface.

The object that handles this intent must adopt the [`INSetProfileInCarIntentHandling`](./insetprofileincarintenthandling.md) protocol. Use this intent object to resolve the profile information and to create an [`INSetProfileInCarIntentResponse`](./insetprofileincarintentresponse.md) object indicating the results of restoring the profile.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (in conjunction with CarPlay) |
| Always requires unlocked device | Yes |

##### Example Phrases

Users can ask Siri to restore profile settings in a vehicle in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Activate profile 1 | Restore profile 3 |
| zh_CN | 打开设置 | 重设设置 |
| zh_HK | 打開資料 | 恢復資料 |
| zh_TW | 打開一號設定檔 |  |
| yue_CN | 打开资料 | 恢复资料 |
| ar | تفعيل الملف الشخصي | تمكين الملف الشخصي |
| da | Aktiver profil 1 | Indlæs profil 2 |
| de | Aktiviere Profil Urlaub | Profil Urlaub aktivieren |
| es | Activa el perfil ‘día soleado’ | Pon la configuración ‘paseo familiar’ |
| fi | Lataa asetukset nimellä 1 | Lataa asetukset 3 |
| fr | Active le profil 1 | Charge le profil virée en voiture |
| he |  |  |
| it | Attiva profilo uno | Rimetti il profilo tre |
| ja | プロファイル1を使用する | プロファイル3をリストアする |
| ko | 프로파일 1 켜줘 | 프로파일 3 작동 시켜 |
| ms | Aktifkan profil 1 | Buka profil 2 |
| nb | Aktiver profil 1 | Still inn profil 3 |
| nl | Activeer profiel 1 | Herstel profiel 3 |
| pt | Ativar perfil 1 | Restaurar perfil 3 |
| ru | Активируй профиль 1 | Загрузи профиль 1 |
| sv | namnge profilen semester | spara profilen som helgresan |
| th | ใช้งานโปรไฟล์ 1 | โหลดโปรไฟล์ 3 |
| tr | Profil 1’i etkinleştir | Profil 1’i aktif hale getir |

When managing CarPlay features, users don’t need to include the name of the app in the phrases that they speak. Siri knows automatically when CarPlay is active and routes CarPlay-related intents to the app of the corresponding automotive vendor.

## Topics

### Initializing the Intent Object
- [convenience init(profileNumber: Int?, profileName: String?, isDefaultProfile: Bool?, carName: INSpeakableString?)](./insetprofileincarintent/init%28profilenumber,profilename,isdefaultprofile,carname%29.md)
  Initializes the intent object with the specified profile name and index information.
- [convenience init(profileNumber: Int?, profileLabel: String?, defaultProfile: Int?)](./insetprofileincarintent/init%28profilenumber,profilelabel,defaultprofile%29.md)
  Creates the intent object with the specified profile name and index information.
- [convenience init(defaultProfile: Int?)](./insetprofileincarintent/init%28defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileLabel: String?)](./insetprofileincarintent/init%28profilelabel%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileLabel: String?, defaultProfile: Int?)](./insetprofileincarintent/init%28profilelabel,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileLabel: String?, isDefaultProfile: Bool?)](./insetprofileincarintent/init%28profilelabel,isdefaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileName: String?, defaultProfile: Int?)](./insetprofileincarintent/init%28profilename,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, defaultProfile: Int?)](./insetprofileincarintent/init%28profilenumber,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileLabel: String?)](./insetprofileincarintent/init%28profilenumber,profilelabel%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileLabel: String?, isDefaultProfile: Bool?)](./insetprofileincarintent/init%28profilenumber,profilelabel,isdefaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [convenience init(profileNumber: Int?, profileName: String?, defaultProfile: Int?)](./insetprofileincarintent/init%28profilenumber,profilename,defaultprofile%29.md)
  Creates an intent to set the car’s profile.
- [- initWithProfileNumber:profileName:defaultProfile:carName:](./insetprofileincarintent/initwithprofilenumber_profilename_defaultprofile_carname_.md)
  Initializes the intent object with the specified profile name and index information.
- [- initWithProfileNumber:profileName:defaultProfile:](./insetprofileincarintent/initwithprofilenumber_profilename_defaultprofile_.md)
  Initializes the intent object with the specified profile name and index information.
- [- initWithProfileNumber:profileLabel:defaultProfile:](./insetprofileincarintent/initwithprofilenumber_profilelabel_defaultprofile_.md)
  Initializes the intent object with the specified profile name and index information.
### Getting the Profile Information
- [var isDefaultProfile: Bool?](./insetprofileincarintent/isdefaultprofile.md)
  A Boolean value indicating whether to make the profile the default profile.
- [var profileName: String?](./insetprofileincarintent/profilename.md)
  The name assigned to the profile.
- [var profileNumber: Int?](./insetprofileincarintent/profilenumber-37vj8.md)
  The profile index from which to restore the settings.
- [var profileLabel: String?](./insetprofileincarintent/profilelabel.md)
  The name assigned to the profile.
- [defaultProfile](./insetprofileincarintent/defaultprofile-4ztep.md)
  A Boolean value indicating whether to make the profile the default profile.
- [profileNumber](./insetprofileincarintent/profilenumber-50f30.md)
  The profile index from which to restore the settings.
### Getting the Car Name
- [var carName: INSpeakableString?](./insetprofileincarintent/carname.md)
  The name of the car associated with the profile.
### Instance Properties
- [var defaultProfile: Int?](./insetprofileincarintent/defaultprofile-19jwc.md)

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### CarPlay Profile Settings
- [protocol INSetProfileInCarIntentHandling](./insetprofileincarintenthandling.md)
  The handler interface for restoring vehicle environment settings from a user-specified profile.
- [class INSetProfileInCarIntentResponse](./insetprofileincarintentresponse.md)
  Your app’s response to a set profile in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent)*