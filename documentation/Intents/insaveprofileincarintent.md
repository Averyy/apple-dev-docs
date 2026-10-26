# INSaveProfileInCarIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to save the user’s vehicle environment settings in a CarPlay-enabled vehicle.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSaveProfileInCarIntent
```

```objc
@interface INSaveProfileInCarIntent : INIntent
```

#### Overview

Automotive vendors whose cars support the saving of seat and other environment settings can add support for this intent to an Intents extension that they ship with their automotive apps. When users engage Siri to save the current environment settings, SiriKit creates an [`INSaveProfileInCarIntent`](./insaveprofileincarintent.md) object and delivers it to the app’s Intents extension. You use the intent object to get the name or index of the profile to use when saving the settings.

You’re responsible for determining which settings to save and restore with user profiles. You can save seat-related settings, climate control settings, defroster settings, radio settings, other settings in your vehicle, or any combination of those settings. Siri handles only the name or index of the profile and doesn’t ask you to provide a list of the settings that you saved.

The object that handles this intent must adopt the [`INSaveProfileInCarIntentHandling`](./insaveprofileincarintenthandling.md) protocol. Use this intent object to resolve the audio source details and to create an [`INSaveProfileInCarIntentResponse`](./insaveprofileincarintentresponse.md) object indicating the results of changing the audio source.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (in conjunction with CarPlay) |
| Always requires unlocked device | Yes |

##### Example Phrases

Users can ask Siri to save profile settings in a vehicle in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list is not exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Remember these settings as profile ‘Jeremy on a road trip’ | Save the current settings to profile 1 |
| zh_CN | 记住设置小白的旅行 | 保存当前设置 |
| zh_HK | 記住資料為媽媽專用 | 保存當前嘅資料 |
| zh_TW | 記住車子設定檔為媽媽專用 | 儲存目前車子的設定 |
| yue_CN | 记住资料为妈妈专用 | 保存当前嘅资料 |
| ar | تسمية الملف الشخصي بالصباحي | تذكر الإعدادات الحالية كالملف الشخصي الأول |
| da | Husk disse indstillinger som “Peter på tur” | Gem indstillinger som profil 1 |
| de | Speicher diese Einstellungen als Profil Urlaub | Speicher Einstellungen als Profil Einkaufen |
| es | Guarda esta configuración como ‘viaje de verano’ | Guarda la configuración actual como ‘viaje corto’ |
| fi | tallenna profiili Jeren automatka | Tallenna asetukset profiiliin 1 |
| fr | Mémorise ces réglages avec le profil Thomas sur la route | Enregistre les réglages dans le profil 1 |
| he |  |  |
| it | Ricordati queste impostazioni come profilo “Alice in viaggio” | Salva le impostazioni correnti in profilo uno |
| ja | 今の設定をドライブ旅行というプロファイル名で記憶して | 現在の設定をプロファイルドライブ旅行に保存 |
| ko | 프로파일을 나들이 모드로 기억해 | 현재 설정을 프로파일 1으로 저장해 |
| ms | Namakan tetapan ini sebagai ‘berselancar’ | Simpan tetapan ini kepada profil 1 |
| nb | Husk disse innstillingene som profilen ‘Jens på biltur’ | Lagre innstillingene til profil 1 |
| nl | Onthoud deze instelling als het profiel ‘Willem onderweg’ | Bewaar de huidige instelling als profiel 1 |
| pt | Lembre dessas configurações como perfil ‘Viagem’ | Salve as configurações atuais no perfil 1 |
| ru | Запомни настройки как профиль “в путешествии” | Сохрани текущие настройки в профиль 1 |
| sv | namnge profilen semester | spara profilen som helgresan |
| th | ตั้งชื่อการตั้งค่าว่าขับรถหน้าร้อน | บันทึกการตั้งค่าปัจจุบันเป็นโปรไฟล์ 1 |
| tr | Ayarları ‘Parti zamanı’ olarak kaydet | Varolan ayarları ‘profil 1’ olarak kaydet |

When managing CarPlay features, users do not need to include the name of the app in the phrases that they speak. Siri knows automatically when CarPlay is active and routes CarPlay-related intents to the app of the corresponding automotive vendor.

## Topics

### Initializing the Intent Object
- [convenience init(profileNumber: Int?, profileLabel: String?)](./insaveprofileincarintent/init%28profilenumber,profilelabel%29.md)
  Creates the intent object with the specified profile name information.
### Getting the Profile Information
- [var profileNumber: Int?](./insaveprofileincarintent/profilenumber-2q84c.md)
  The profile index in which to save the settings.
- [var profileName: String?](./insaveprofileincarintent/profilename.md)
  The name to assign to the profile.
- [var profileLabel: String?](./insaveprofileincarintent/profilelabel.md)
  The name to assign to the profile.

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

### CarPlay Profile Saving
- [protocol INSaveProfileInCarIntentHandling](./insaveprofileincarintenthandling.md)
  The handler interface for saving vehicle environment settings to a user-specified profile.
- [class INSaveProfileInCarIntentResponse](./insaveprofileincarintentresponse.md)
  Your app’s response to a save profile in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintent)*