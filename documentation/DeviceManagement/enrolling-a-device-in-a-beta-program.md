# Enrolling a device in a beta program

**Framework**: Device Management

Use program tokens to manage beta program enrollment.

#### Overview

To enroll a device in the Apple Beta Software Program or AppleSeed for IT, a device management service retrieves a token from Apple, then provides the token to devices during Automated Device Enrollment or by using the [`SoftwareUpdateSettings`](softwareupdatesettings.md) declaration. For more information, see [`Request a specific minimum software version during enrollment`](deploying-software-updates-using-declarative-management#Request-a-specific-minimum-software-version-during-enrollment.md).

#### Retrieve Beta Tokens

Follow these steps to retrieve beta tokens from the AppleSeed for IT program using your device management service:

1. An administrator in Apple School Manager or Apple Business enrolls in the [`AppleSeed for IT`](https://developer.apple.comhttps://beta.apple.com/for-it) program.
2. The AppleSeed for IT service creates organization-specific beta program enrollment tokens.
3. A device management service requests available beta program tokens using the `https://mdmenrollment.apple.com/os-beta-enrollment/tokens` endpoint. ![The device management service retrieves the beta tokens from the AppleSeed for IT program](https://docs-assets.developer.apple.com/published/0774d2d632b35a7a7d667d3a95ff42cf/enrolling-a-device-in-a-beta-program01%402x.png)

Similar to other service endpoints available at `mdmenrollment.apple.com`, device management services authenticate using OAuth.

The HTTP `GET` request must include the following header fields:

- `X-ADM-Auth-Session`: The OAuth token to authenticate the request. For more information about the authentication process, see [`Authenticating for Automated Device Enrollment`](authenticating-for-automated-device-enrollment.md).
- `X-Server-Protocol-Version`: Set this to `1`.

The service endpoint returns a JSON object with the following structure:

```json
{
  "betaEnrollmentTokens": [
    {
      "token": "<your-beta-token-here>",
      "title": "macOS 27 Golden Gate AppleSeed Beta",
      "os": "macOS"
    },
    {
      "token": "<your-beta-token-here>",
      "title": "iOS 27 AppleSeed Beta",
      "os": "iOS"
    }
  ]
}
```

The `token` is unique for each organization and you can’t reuse it across different Apple School Manager and Apple Business organizations. The `token` is also specific to a certain operating system upgrade seeding period. The `title` is a human-readable description of the beta release. The `os` field can contain the following values: `iOS` (includes iPadOS), `macOS`, `tvOS`, `watchOS`, or `visionOS`.

#### Enroll Devices in a Beta Program

After a device enrolls in device management, a device management service can offer, enroll, or unenroll supervised iPad, iPhone, and Mac devices from beta programs using the `Beta` dictionary in the [`SoftwareUpdateSettings`](softwareupdatesettings.md) declaration. On unsupervised devices, you can only use the `OfferPrograms` array to let users manually enroll in beta programs that the organization subscribes to.

![The device management service applies a software update settings declaration to enroll a device in a beta program](https://docs-assets.developer.apple.com/published/435437ad7b670520f859b4a7424ccf0d/enrolling-a-device-in-a-beta-program02%402x.png)

The dictionaries used in the `OfferPrograms` and `RequireProgram` keys must contain the following keys:

| Key | Type | Required | Description |
| --- | --- | --- | --- |
| `Description` | String | Yes | A human-readable description of the beta program. |
| `Token` | String | Yes | The seeding service token for the organization that operates the device management service. The device uses this token with the Apple Seeding Server to verify eligibility and receive an updated software update configuration. |

The `OfferPrograms` key is an array that can have multiple `Program` entries of the structure above. The `RequireProgram` dictionary contains only a single program definition.

#### Allow Users to Enroll Devices in a Beta Program

When you set the `ProgramEnrollment` key to `Allowed`, users can enroll in any program available to their Apple Account or Managed Apple Account and in any beta program that the `OfferPrograms` array lists.

The following example uses the described keys:

```json
{
  "Beta": {
    "ProgramEnrollment": "Allowed",
    "OfferPrograms": [
      {
          "Description": "iOS 27 AppleSeed Beta",
          "Token": "<your-beta-token-here>"
      }
    ]
  }
}
```

To allow users to participate without signing in, set the `ProgramEnrollment` key to `AlwaysOn`. In this case, the device offers users all programs listed in the `OfferPrograms` array.

#### Automatically Enroll Devices in a Beta Program

You can also automatically enroll devices in a beta program by setting `ProgramEnrollment` to `AlwaysOn` and defining the program in the `RequireProgram` dictionary.

The `RequireProgram` dictionary requires the following keys:

| Key | Type | Required | Description |
| --- | --- | --- | --- |
| `Description` | String | Yes | A human-readable description of the beta program. |
| `Token` | String | Yes | The seeding service token for the organization that operates the device management service. The device management service uses this token to enroll devices in the corresponding beta program. |

The following example uses the described keys:

```json
{
  "Beta": {
    "ProgramEnrollment": "AlwaysOn",
    "RequireProgram": {
      "Description": "iOS 27 AppleSeed Beta",
      "Token": "<your-beta-token-here>"
    }
  }
}
```

#### Restrict Users From Enrolling Devices in a Beta Program

To prevent users from enrolling, set the `ProgramEnrollment` key to `AlwaysOff`. This setting also unenrolls the device from any beta program that a user or the device management service previously enrolled it in.

## See Also

- [Deploying software updates using declarative management](deploying-software-updates-using-declarative-management.md)
  Use declarative configurations to deploy and manage software updates on managed devices.
- [Phases of software update enforcement](phases-of-software-update-enforcement.md)
  Enforcing software updates on Apple devices goes through specific phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enrolling-a-device-in-a-beta-program)*