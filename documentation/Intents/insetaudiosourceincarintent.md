# INSetAudioSourceInCarIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to change the source of audio playback in a CarPlay-enabled vehicle.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetAudioSourceInCarIntent
```

```objc
@interface INSetAudioSourceInCarIntent : INIntent
```

#### Overview

Automotive venders can add support for this intent to an Intents extension that they ship with their automotive apps. When the user asks Siri to change the audio source of the vehicle, SiriKit creates an [`INSetAudioSourceInCarIntent`](./insetaudiosourceincarintent.md) object and delivers it to your app’s Intents extension. You use the intent to identify which audio source the user wants to use and to communicate the new audio source information directly to your vehicle’s systems.

Users may select audio sources by name or by asking for the next or previous audio source that’s available. When the user asks for an audio source by name, Siri populates the [`audioSource`](./insetaudiosourceincarintent/audiosource.md) property of this intent object with the specific requested source. When the user asks for the next or previous audio source, Siri places the appropriate value in the [`relativeAudioSourceReference`](./insetaudiosourceincarintent/relativeaudiosourcereference.md) property so that you can determine which audio source to select. Only one of these properties contains usable information; Siri sets the other to a constant indicating an unknown status for the value.

The object that handles this intent must adopt the [`INSetAudioSourceInCarIntentHandling`](./insetaudiosourceincarintenthandling.md) protocol. Use this intent object to resolve the audio source details and to create an [`INSetAudioSourceInCarIntentResponse`](./insetaudiosourceincarintentresponse.md) object indicating the results of changing the audio source.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri (in conjunction with CarPlay) |
| Always requires unlocked device | Yes |

##### Example Phrases

Users can ask Siri to change the audio source in a vehicle in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Change the audio source to USB | Switch to the next audio source |
| zh_CN | 音源USB | 切换音源 |
| zh_HK | 音源較去USB | 切換音源 |
| zh_TW | 切換到USB | 切換音源 |
| yue_CN | 音源较去USB | 切换音源 |
| ar | تغيير مصدر الصوت | تبديل إلى مصدر الصوت التالي |
| da | aux lydkilde | Skift til næste lydindgang |
| de | Wechsele die Audioquelle auf USB | Die Audioquelle auf USB wechseln |
| es | Cambia la fuente de audio al USB | Pon la fuente de sonido al DVD |
| fi | Aseta äänilähteeksi USB | Vaihda seuraavaan äänilähteeseen |
| fr | Audio sur sortie auxiliaire | Passe à la source audio suivante |
| he | תחליפי את מקור אודיו | תחליפי את מקור האודיו |
| it | Cambia la sorgente audio a USB | Cambia alla prossima sorgente audio |
| ja | 音源をUSBに変更 | 次の音源に切り替えて |
| ko | 오디오 소스를 USB로 변경 | 다음 오디오 소스로 바꿔줘 |
| ms | Tukar sumber audio kepada USB | Tukar kepada sumber audio berikutnya |
| nb | Endre lydkilde til USB | Bytt til neste lydkilde |
| nl | Verander de audiobron naar USB | Schakel naar de volgende audiobron |
| pt | Mudar a entrada de áudio para USB | Troque para a próxima entrada de áudio |
| ru | Измени источник аудио на USB | Переключи на следующий источник музыки |
| sv | ändra ljudkälla till aux | byt ljudkälla till aux ljud |
| th | เปลี่ยนแหล่งเสียงเป็น USB | เปลี่ยนเป็นแหล่งเสียงถัดไป |
| tr | Ses kaynağı USB olsun | Bir sonraki ses kaynağına geç |

When managing CarPlay features, users don’t need to include the name of the app in the phrases that they speak. Siri knows automatically when CarPlay is active and routes CarPlay-related intents to the app of the corresponding automotive vendor.

## Topics

### Initializing the Intent Object
- [init(audioSource: INCarAudioSource, relativeAudioSourceReference: INRelativeReference)](./insetaudiosourceincarintent/init%28audiosource,relativeaudiosourcereference%29.md)
  Initializes the intent object with the specified audio source information.
### Getting Details About the Audio Source to Set
- [var audioSource: INCarAudioSource](./insetaudiosourceincarintent/audiosource.md)
  The audio source to select.
- [var relativeAudioSourceReference: INRelativeReference](./insetaudiosourceincarintent/relativeaudiosourcereference.md)
  The relative audio source to select.

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

### CarPlay Audio Source
- [protocol INSetAudioSourceInCarIntentHandling](./insetaudiosourceincarintenthandling.md)
  The handler interface for changing a vehicle’s audio source.
- [class INSetAudioSourceInCarIntentResponse](./insetaudiosourceincarintentresponse.md)
  Your app’s response to a set audio source in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintent)*