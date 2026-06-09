# TopLevel

**Framework**: Device Management  
**Kind**: dictionary

The top-level payload properties for all profiles.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
object TopLevel
```

## Mentions

- [Configuring multiple devices using profiles](configuring-multiple-devices-using-profiles.md)

#### Discussion

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | N/A |

## Topics

### Objects
- [object TopLevel.ConsentText](toplevel/consenttext-data.dictionary.md)
  The dictionary of consent agreements per language.
- [object TopLevel.PayloadContentItem](toplevel/payloadcontentitem.md)
  The payload-specific content for this profile.

## Properties

- `ConsentText` (TopLevel.ConsentText): A dictionary that includes: - A key that contains the IETF BCP 47 identifier for a language, such as *en* or *jp*
- A value that contains the agreement localized to language specified by the key The dictionary can also contain an optional key, `default`, with its value consisting of the unlocalized (usually in *en*) agreement. The system always displays the agreement in a dialog, and the user needs to agree before the system can install the profile. The system chooses a localized version in the order of preference that the user specifies in macOS, or based on the user’s current language setting in iOS. If there’s no exact match, the system uses the default localization. If there’s no default localization, the system uses the *en* localization. If there’s no *en* localization, the system uses the first available localization. > 💡 **Tip**:  Provide a default value, if possible. The system won’t display a warning if the user’s locale doesn’t match any localization in the `ConsentText` dictionary.
- `DurationUntilRemoval` (number): The number of seconds until the profile is automatically removed. If the `RemovalDate` key is present, the system uses whichever field yields the earliest date.
- `EncryptedPayloadContent` (data): The encrypted payload content. Only present for encrypted payloads.
- `PayloadContent` ([TopLevel.PayloadContentItem]) *(required)*: The array of payload dictionaries. Not present for encrypted payloads.
- `PayloadDescription` (string): The description of the profile, shown on the Detail screen for the profile. Make this description detailed enough to help the user decide whether to install the profile.
- `PayloadDisplayName` (string): The human-readable name for the profile, which doesn’t need to be unique. The system displays this value on the Detail screen.
- `PayloadExpirationDate` (date): The date when a profile is no longer valid and the system presents an update button to the user. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+ | visionOS 1+
- `PayloadIdentifier` (string) *(required)*: The reverse-DNS style identifier (`com.example.myprofile`, for example) that identifies the profile. The system uses this string to determine whether to replace an existing profile or add it as a new profile.
- `PayloadOrganization` (string): The human-readable string that contains the name of the organization that provided the profile.
- `PayloadRemovalDisallowed` (boolean): If present and set to `true`, the user can’t delete the profile unless the profile has a removal password and the user provides it. On macOS 10.15 and later, this key only affects removal of *manually* installed profiles. If set to `true` and no profile removal payload is present, removing the profile requires admin auth. On macOS versions prior to 10.15, this key prevents admins from removing MDM installed profiles. However, as of macOS 10.15, users can never remove MDM profiles, not even the admin. On iOS users can’t remove a MDM profile. Requires a supervised device. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+
- `PayloadScope` (string): A string that defines whether to install the profile for the system or the user. In many cases, it determines the location of certificate items, such as keychains. Though it’s not possible to declare different payload scopes, payloads like VPN can automatically install their items in both scopes, if needed. Available: iOS 4+ | iPadOS 4+ | macOS 10.8+ | tvOS 9+ | visionOS 1+ | watchOS 1+
- `PayloadType` (string) *(required)*: The type of payload. The only supported value is `Configuration`.
- `PayloadUUID` (string) *(required)*: The globally unique identifier for the profile. The actual content is unimportant. In macOS, you can use `uuidgen` to generate reasonable UUIDs.
- `PayloadVersion` (integer) *(required)*: The version number of the profile format, which needs to be `1`. This number represents the version of the configuration profile as a whole, not of the individual profiles within it.
- `RemovalDate` (date): The date when the system automatically removes the profile.
- `TargetDeviceType` (integer): The type of platform of the target device. Specifying the platform type helps prevent unintended installations. For interactive installations on iOS devices, specifying a target platform avoids interstitial alerts that prompt the user to choose a profile target when multiple targets are eligible. Allowed values: - `0`: Any/unspecified
- `1`: iPhone/iPad/iPod Touch
- `2`: Apple Watch
- `3`: HomePod
- `4`: Apple TV
- `5`: Mac
- `6`: Vision Pro Available: iOS 12.2+ | iPadOS 12.2+ | macOS 10.15+ | tvOS 12.2+ | visionOS 1.1+ | watchOS 5.2+

## See Also

- [object CommonPayloadKeys](commonpayloadkeys.md)
  The properties common to all payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/toplevel)*