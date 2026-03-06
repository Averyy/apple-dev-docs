# BetaAppLocalization.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a Beta App Localizations resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppLocalization.Attributes
```

## Properties

- `description` (string): A description of your app that highlights features and functionality.
- `feedbackEmail` (string): An email address to which beta testers can send feedback. Also appears as the reply-to address for TestFlight invitation emails.
- `locale` (string): The specified locale. To learn more, see [`Managing metadata in your app by using locale shortcodes`](managing-metadata-in-your-app-by-using-locale-shortcodes.md).
- `marketingUrl` (string): A URL with information about your app. This URL is visible to testers in the TestFlight app.
- `privacyPolicyUrl` (string): A URL that links to your company’s privacy policy. Privacy policies are recommended for all apps that collect user or device-related data or as otherwise required by law.
- `tvOsPrivacyPolicy` (string): Your company’s privacy policy. Privacy policies are recommended for all apps that collect user or device-related data, or as otherwise required by law.

## See Also

- [Beta App Localizations](beta-app-localizations.md)
  Beta test information about apps, specific to a locale.
- [object BetaAppLocalization.Relationships](betaapplocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaapplocalization/attributes-data.dictionary)*