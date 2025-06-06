# Configuring Exposure Notifications

**Framework**: Exposurenotification

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

> **Note**:  Keys you use to display information to users, customize the UI, adjust exposure calculations, and configure test verification servers are only used by Exposure Notifications Express, including any field that takes a color, image, or URL, or that includes `header`, `message`, or `text` as part of its name.

##### Set Region Information

A PHA can manage more than one region and can configure each region with different values. These values allow you to change region-specific information:

Name of the PHA. Used in the single-color header during onboarding, in EN settings and in Exposure Notifications details. . .

A string containing the Mobile Country Code (MCC) in version 1, or the ISO Country Code in version 2.

Date that Exposure Notifications is available for use in this region, specified as seconds since 00:00:00 UTC on January 1, 1970.

Name of the region. . .

A URL that contains the agency’s website. The system presents this URL to the user in the region’s detail view in the Settings app. .

Name of the region the PHA manages. Used as the subtitle in the onboarding header and in various places in the Settings app. .

An integer used to customize the appearance of the header used in Exposure Notifications Express when presenting region-specific information to the user. Acceptable values are: `0` for standard appearance with name and icon, `1` for icon-only centered, `2` for icon-only on the left, and `3` for icon-only on the right.

An array of RGB values ranging from `0.0` to `1.0` representing the text color for the text in the header (for example, `[1.0, 0.75, 0.75]`).

An array of RGB values ranging from `0.0` to `1.0` representing the accent color to use as the background for the PHA-branded header above PHA-provided content (for example, `[1.0, 1.0, 0.0]`).

The URL of an image file for the agency logo, displayed in the PHA-branded header above PHA-provided content.

Summary text that appears during onboarding and in settings below the branded header. . .

A string that contains the plain text end-user consent document provided by the PHA. . .

A string that contains the semantic version or monotonically increasing number of the consent text. .

A Boolean that indicates whether the server enables APIs that accept matching temporary exposure key files in that region.

A string that contains the App Store bundle identifier of the app for the given region.

A Boolean that indicates whether this is a test region.

##### Set Signing Key

These keys define the security keys used to authenticate requests and sign key archives:

A string that contains the public key used to verify the Temporary Exposure Key (TEK) file signature.

A string that contains the version of the public key from the PHA.

##### Configure Duration Weights

These keys define the attenuation weights that Exposure Notifications Express uses to compute the ERV:

An unsigned 16-bit integer that contains the immediate attenuation weight.

An unsigned 16-bit integer that contains the near attenuation weight.

An unsigned 16-bit integer that contains the medium attenuation weight.

An unsigned 16-bit integer that contains the other attenuation weight.

An unsigned 8-bit integer that contains the attenuation threshold for immediate to near.

An unsigned 8-bit integer that contains the attenuation threshold for near to medium.

An unsigned 8-bit integer that contains the attenuation threshold for medium to far.

##### Calculate Exposure Risk Values

These keys define weights and thresholds that Exposure Notifications Express uses to compute the ERV:

An unsigned 64-bit integer mapping  in the Temporary Exposure Key to an infectiousness category. Set the value to one of the following: `00` (drop), `01` (standard infectiousness), `10` (high infectiousness).

An unsigned 16-bit integer that contains the standard infectiousiness weight.

An unsigned 16-bit integer that contains the high infectiousiness weight.

An unsigned 16-bit integer that contains the confirmed test report type weight.

An unsigned 16-bit integer that contains the confirmed clinical report type weight.

An unsigned 16-bit integer that contains the self report type weight.

An unsigned 8-bit integer that maps the None value to an existing report type.

An unsigned 8-bit integer that contains the threshold in days that EN considers history valid. For example, `10` means only the past 10 days of history is valid.

##### Set Exposure Classifications

These keys define values that set the calculation threshold for customizable exposure classifications in Exposure Notifications Express. A PHA can define up to four classifications. If a PHA creates more than one classification, they will be checked in order, only moving on to the next classification if the threshold is not met.

Replace the trailing `X` in the key names below with a number from 1 to 4 to specify which classification’s value to change. For example, to change the Exposure Details Body for the second exposure classification, you would use the key `exposureDetailsBodyText_2`. Setting any threshold field to a value of 0 disables its notification.

A string that contains the body text presented to the user when navigating to their latest exposure details in the Settings app. . .

A string that contains the bolded subject of the notification presented to the user when transitioning to this exposure state. The system also presents this as the heading in the Settings app when a user browses to their latest exposure information. . .

A string that contains the body text of the notification presented to the user when transitioning to this exposure state. . .

A string that contains the unique name of this classification configuration. This name must change when the thresholds for this classification change. .

A URL that contains the link to the PHA’s website for further guidance when the user navigates to their latest exposure details in Settings. .

A 32-bit integer that contains the confirmed test report type threshold in ERV from when the OS raises a notification.

A 32-bit integer that contains the clinical diagnosis report type threshold in ERV from when the OS raises a notification.

A 32-bit integer that contains the self report type threshold in ERV from when the OS raises a notification.

A 32-bit integer that contains the recursive report type threshold in ERV from when the OS raises a notification.

A 32-bit integer that contains the per day sum threshold in ERV from when the OS raises a notification.

A 32-bit integer that contains the per day maximum threshold in ERV from when the OS raises a notification.

A 32-bit integer that contains the threshold in weighted duration-at-attenuation when the OS raises a notification.

##### Set Exposure Revoked Notifications

These keys define values that set text presented to the user by Exposure Notifications Express upon revocation of an exposure diagnosis:

A string that contains body text of a notification presented to the user when transitioning to a no exposure state due to revocation of a prior exposure. .

A string that contains a bolded notification presented to the user when transitioning to this exposure state. .

A string that contains body text presented to the user when navigating to their latest exposure details in the Settings app. . .

A URL to the PHA’s website for further guidance when the user navigates to their latest exposure details in the Settings app. .

##### Configure Key Server Information

These keys define values the system uses to interact with your key server.

A URL that contains the TEK download endpoint index file. .

A URL that contains the TEK base path. .

An unsigned 8-bit integer that contains how often the PHA expects to update TEK for downloading, specified in hours. Valid values are `2`, `4`, `8`, or `24`. .

A URL that contains the agency’s upload key server. .

##### Configure Test Verification Server Information

These keys define values used to verify a positive diagnosis before uploading key files to the key server when using Exposure Notifications Express:

A string that contains an introductory message from the PHA explaining the purpose of test verification and key upload. . .

A URL that contains the PHA’s website where user can learn more about use of cerification codes, and get help if something isn’t working. .

A URL that contains the agency’s test verification server. Used to exchange valid verification codes for long-term authentication tokens. .

A URL used to retrieve a certificate and per-key metadata for a batch of TEKs before uploading them to the key server. .

An API key, required to talk to the Test Verification server. .

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

*[View on Apple Developer](https://developer.apple.com/documentation/ExposureNotification/configuring-exposure-notifications)*