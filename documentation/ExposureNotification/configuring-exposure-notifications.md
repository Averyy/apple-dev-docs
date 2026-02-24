# Configuring Exposure Notifications

**Framework**: Exposure Notification

Define how Exposure Notifications work for a region by assigning server-based key-value pairs.

#### Overview

The configuration fields listed below define the behavior for Exposure Notifications features such as exposure matching, Exposure Risk Value (ERV) calculation, and messaging for regions managed by a Public Health Authority (PHA). These values can be changed by using the server-to-server API or by contacting Apple to request a change. PHAs that only support Exposure Notifications Express can also change these values by logging into Apple Business Register (ABR).

> **Note**:  To learn more about using these keys with the Exposure Notifications server-to-server API, see [`Changing Configuration Values Using the Server‑to‑Server API`](changing-configuration-values-using-the-server-to-server-api.md).

Some keys are relevant to all Exposure Notifications behavior, while some keys are only used by Exposure Notifications Express. Keys used to display information to users, to customize the user interface, to adjust exposure calculations, and to configure test verification servers are only used by Exposure Notifications Express. The other values are used by both Exposure Notifications Express and Exposure Notifications apps.

Certain keys are marked as Required, and some are also marked Localizable, as noted in bold in the lists below.

For keys marked Required, a PHA must configure these values for a region before it can go live with Exposure Notifications, but you don’t need to include required keys in every server-to-server API request. If a required field already has a valid value, requests only need to include that key when requesting a change to that field.

Using keys marked Localizable, you can provide different values for different languages by appending an underscore followed by the ISO two-letter language code, then another underscore, and then the ISO two-letter country code for the region. For example, to provide a localized value of `agencyDisplayName` for French-Canadians, use the key `agencyDisplayName_FR_CA`. When using the server-to-server API, you can provide multiple localized versions of the same key in the same request. In ABR, localizable fields provide a button that allows you to enter additional localized values.

##### Specify Api Version

Exposure Notifications’ APIs are available in two versions. Version 1 requires a client app to function, while Version 2 — available on iOS 13.7 and later —  works both with a client app or without an app by using Exposure Notifications Express.

- **`enVersion`**: An unsigned 8-bit integer that determines whether an app uses version 1 or 2 of the Exposure Notifications framework.

> **Note**:  Keys you use to display information to users, customize the UI, adjust exposure calculations, and configure test verification servers are only used by Exposure Notifications Express, including any field that takes a color, image, or URL, or that includes `header`, `message`, or `text` as part of its name.

##### Set Region Information

A PHA can manage more than one region and can configure each region with different values. These values allow you to change region-specific information:

- **`agencyDisplayName`**: **ABR Field**: PHA Name

Name of the PHA. Used in the single-color header during onboarding, in EN settings and in Exposure Notifications details. **Required**. **Localizable**.

- **`regionIdentifier`**: **ABR Field**: Region

A string containing the Mobile Country Code (MCC) in version 1, or the ISO Country Code in version 2.

- **`goLiveDate`**: **ABR Field**: Go Live Date

Date that Exposure Notifications is available for use in this region, specified as seconds since 00:00:00 UTC on January 1, 1970.

- **`agencyRegionName`**: **ABR Field**: Region (for example, state/province or country)

Name of the region. **Required**. **Localizable**.

- **`agencyWebsiteURL`**: **ABR Field**: Agency Website URL

A URL that contains the agency’s website. The system presents this URL to the user in the region’s detail view in the Settings app. **Required**.

- **`agencyRegionName`**: **ABR Field**: Region

Name of the region the PHA manages. Used as the subtitle in the onboarding header and in various places in the Settings app. **Required**.

- **`agencyHeaderStyle`**: **ABR Field**: Header Style

An integer used to customize the appearance of the header used in Exposure Notifications Express when presenting region-specific information to the user. Acceptable values are: `0` for standard appearance with name and icon, `1` for icon-only centered, `2` for icon-only on the left, and `3` for icon-only on the right.

- **`agencyHeaderTextColor`**: **ABR Field**: Text Color

An array of RGB values ranging from `0.0` to `1.0` representing the text color for the text in the header (for example, `[1.0, 0.75, 0.75]`).

- **`agencyColor`**: **ABR Field**: Header Color

An array of RGB values ranging from `0.0` to `1.0` representing the accent color to use as the background for the PHA-branded header above PHA-provided content (for example, `[1.0, 1.0, 0.0]`).

- **`agencyImage`**: **ABR Field**: Image URL

The URL of an image file for the agency logo, displayed in the PHA-branded header above PHA-provided content.

- **`agencyMessage`**: **ABR Field**: Message Body

Summary text that appears during onboarding and in settings below the branded header. **Required**. **Localizable**.

- **`legalConsentText`**: **ABR Field**: Legal Consent Text

A string that contains the plain text end-user consent document provided by the PHA. **Required**. **Localizable**.

- **`legalConsentVersion`**: **ABR Field**: Legal Consent Version

A string that contains the semantic version or monotonically increasing number of the consent text. **Required**.

- **`exposureMatching`**: **ABR Field**: Is exposure matching enabled?

A Boolean that indicates whether the server enables APIs that accept matching temporary exposure key files in that region.

- **`appBundleId`**: **ABR Field**: App Bundle ID (Optional)

A string that contains the App Store bundle identifier of the app for the given region.

- **`isTestRegion`**: **ABR Field**: Not editable

A Boolean that indicates whether this is a test region.

##### Set Signing Key

These keys define the security keys used to authenticate requests and sign key archives:

- **`publicKey`**: **ABR Field**: Public Key

A string that contains the public key used to verify the Temporary Exposure Key (TEK) file signature.

- **`publicKeyVersion`**: **ABR Field**: Public Key Version

A string that contains the version of the public key from the PHA.

##### Configure Duration Weights

These keys define the attenuation weights that Exposure Notifications Express uses to compute the ERV:

- **`attenuationImmediateWeight`**: **ABR Field**: Attenuation Immediate Weight (0-250%)** **

An unsigned 16-bit integer that contains the immediate attenuation weight.

- **`attenuationNearWeight`**: **ABR Field**: Attenuation Near Weight (0-250%)

An unsigned 16-bit integer that contains the near attenuation weight.

- **`attenuationMedWeight`**: **ABR Field**: Attenuation Medium Weight (0-250%)

An unsigned 16-bit integer that contains the medium attenuation weight.

- **`attenuationOtherWeight`**: **ABR Field**: Attenuation Other Weight (0-250%)

An unsigned 16-bit integer that contains the other attenuation weight.

- **`attenuationImmediateNearThreshold`**: **ABR Field**: Attenuation Immediate Near Threshold (0-255)

An unsigned 8-bit integer that contains the attenuation threshold for immediate to near.

- **`attenuationNearMedThreshold`**: **ABR Field**: Attenuation Immediate Med Threshold (0-255)

An unsigned 8-bit integer that contains the attenuation threshold for near to medium.

- **`attenuationMedFarThreshold`**: **ABR Field**: Attenuation Med Far Threshold (0-255)

An unsigned 8-bit integer that contains the attenuation threshold for medium to far.

##### Calculate Exposure Risk Values

These keys define weights and thresholds that Exposure Notifications Express uses to compute the ERV:

- **`symptomOnsetToInfectiousnessMap`**: **ABR Field**: Infectiousness to Symptom Onset Map

An unsigned 64-bit integer mapping *days since symptoms onset* in the Temporary Exposure Key to an infectiousness category. Set the value to one of the following: `00` (drop), `01` (standard infectiousness), `10` (high infectiousness).

- **`infectiousnessStandardWeight`**: **ABR Field**: Infectiousness Standard Weight (0-250%)

An unsigned 16-bit integer that contains the standard infectiousiness weight.

- **`infectiousnessHighWeight`**: **ABR Field**: Infectiousness High Weight (0-250%)

An unsigned 16-bit integer that contains the high infectiousiness weight.

- **`reportTypeConfirmedTestWeight`**: **ABR Field**: Report Type Confirmed Test Weight (0-250%)

An unsigned 16-bit integer that contains the confirmed test report type weight.

- **`reportTypeConfirmedClinicalDiagnosisWeight`**: **ABR Field**: Report Type Confirmed Clinical Diagnosis Weight (0-250%)

An unsigned 16-bit integer that contains the confirmed clinical report type weight.

- **`reportTypeSelfReportWeight`**: **ABR Field**: Report Type Self Report Weight (0-250%)

An unsigned 16-bit integer that contains the self report type weight.

- **`reportTypeNoneMap`**: **ABR Field**: Report Type None Map

An unsigned 8-bit integer that maps the None value to an existing report type.

- **`daysSinceExposureThreshold`**: **ABR Field**: Days Since Exposure Threshold (0-14)

An unsigned 8-bit integer that contains the threshold in days that EN considers history valid. For example, `10` means only the past 10 days of history is valid.

##### Set Exposure Classifications

These keys define values that set the calculation threshold for customizable exposure classifications in Exposure Notifications Express. A PHA can define up to four classifications. If a PHA creates more than one classification, they will be checked in order, only moving on to the next classification if the threshold is not met.

Replace the trailing `X` in the key names below with a number from 1 to 4 to specify which classification’s value to change. For example, to change the Exposure Details Body for the second exposure classification, you would use the key `exposureDetailsBodyText_2`. Setting any threshold field to a value of 0 disables its notification.

- **`exposureDetailsBodyText_X`**: **ABR Field**: Exposure Details Body

A string that contains the body text presented to the user when navigating to their latest exposure details in the Settings app. **Required**. **Localizable**.

- **`notificationSubject_X`**: **ABR Field**: Notification Subject

A string that contains the bolded subject of the notification presented to the user when transitioning to this exposure state. The system also presents this as the heading in the Settings app when a user browses to their latest exposure information. **Required**. **Localizable**.

- **`notificationBody_X`**: **ABR Field**: Notification Body

A string that contains the body text of the notification presented to the user when transitioning to this exposure state. **Required**. **Localizable**.

- **`classificationName_X`**: **ABR Field**: Classification Name

A string that contains the unique name of this classification configuration. This name must change when the thresholds for this classification change. **Required**.

- **`classificationURL_X`**: **ABR Field**: Classification URL

A URL that contains the link to the PHA’s website for further guidance when the user navigates to their latest exposure details in Settings. **Required**.

- **`confirmedTestPerDaySumERVThreshold_X`**: **ABR Field**: Confirmed Test Per Day Sum ERV Threshold

A 32-bit integer that contains the confirmed test report type threshold in ERV from when the OS raises a notification.

- **`clinicalDiagnosisPerDaySumERVThreshold_X`**: **ABR Field**: Clinical Diagnosis Per Day Sum ERV Threshold

A 32-bit integer that contains the clinical diagnosis report type threshold in ERV from when the OS raises a notification.

- **`selfReportPerDaySumERVThreshold_X`**: **ABR Field**: Self Report Per Day Sum ERV Threshold

A 32-bit integer that contains the self report type threshold in ERV from when the OS raises a notification.

- **`recursivePerDaySumERVThreshold_X`**: **ABR Field**: Recursive Per Day Sum ERV Threshold

A 32-bit integer that contains the recursive report type threshold in ERV from when the OS raises a notification.

- **`perDaySumERVThreshold_X`**: **ABR Field**: Per Day Sum ERV Threshold

A 32-bit integer that contains the per day sum threshold in ERV from when the OS raises a notification.

- **`perDayMaxERVThreshold_X`**: **ABR Field**: Per Day Max ERV Threshold

A 32-bit integer that contains the per day maximum threshold in ERV from when the OS raises a notification.

- **`weightedDurationAtAttenuationThreshold_X`**: **ABR Field**: Weighted Duration at Attenuation Threshold

A 32-bit integer that contains the threshold in weighted duration-at-attenuation when the OS raises a notification.

##### Set Exposure Revoked Notifications

These keys define values that set text presented to the user by Exposure Notifications Express upon revocation of an exposure diagnosis:

- **`revokedNotificationBody`**: **ABR Field**: Notification Body

A string that contains body text of a notification presented to the user when transitioning to a no exposure state due to revocation of a prior exposure. **Required**.

- **`revokedNotificationSubject`**: **ABR Field**: Notification Subject

A string that contains a bolded notification presented to the user when transitioning to this exposure state. **Required**.

- **`revokedDetailsBodyText`**: **ABR Field**: Revoked Details Body

A string that contains body text presented to the user when navigating to their latest exposure details in the Settings app. **Required**. **Localizable**.

- **`revokedURL`**: **ABR Field**: Revoked URL

A URL to the PHA’s website for further guidance when the user navigates to their latest exposure details in the Settings app. **Required**.

##### Configure Key Server Information

These keys define values the system uses to interact with your key server.

- **`tekLocalDownloadIndexFile`**: **ABR Field**: TEK Local Download Index File

A URL that contains the TEK download endpoint index file. **Required**.

- **`tekLocalDownloadBasePath`**: **ABR Field**: TEK Local Download Base Path

A URL that contains the TEK base path. **Required**.

- **`tekPublishInterval`**: **ABR Field**: TEK Publish Interval in Hours

An unsigned 8-bit integer that contains how often the PHA expects to update TEK for downloading, specified in hours. Valid values are `2`, `4`, `8`, or `24`. **Required**.

- **`tekUploadURL`**: **ABR Field**: TEK Upload URL

A URL that contains the agency’s upload key server. **Required**.

##### Configure Test Verification Server Information

These keys define values used to verify a positive diagnosis before uploading key files to the key server when using Exposure Notifications Express:

- **`testVerificationIntroMessage`**: **ABR Field**: Test Verifiction Intro Message

A string that contains an introductory message from the PHA explaining the purpose of test verification and key upload. **Required**. **Localizable**.

- **`verificationCodeLearnMoreURL`**: **ABR Field**: Verification Learn More URL

A URL that contains the PHA’s website where user can learn more about use of cerification codes, and get help if something isn’t working. **Required**.

- **`testVerificationURL`**: **ABR Field**: Test Verification URL

A URL that contains the agency’s test verification server. Used to exchange valid verification codes for long-term authentication tokens. **Required**.

- **`testVerificationCertificateURL`**: **ABR Field**: Test Verification Certificate URL

A URL used to retrieve a certificate and per-key metadata for a batch of TEKs before uploading them to the key server. **Required**.

- **`testVerificationAPIKey`**: **ABR Field**: Test Verification API Key

An API key, required to talk to the Test Verification server. **Required**.

## See Also

- [class ENExposureConfiguration](enexposureconfiguration.md)
  The object that contains parameters for configuring exposure notification risk scoring behavior.
- [class ENExposureWindow](enexposurewindow.md)
  A set of scan events from observed beacons within a time span.
- [class ENScanInstance](enscaninstance.md)
  The aggregation of attenuations of beacons received during a scan.
- [Exposure Parameter Limits](exposure-parameter-limits.md)
  The limits for the parameters you use in exposure risk calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/configuring-exposure-notifications)*