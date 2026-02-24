# MDM

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures mobile device management (MDM) settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object MDM
```

## Mentions

- [Displaying managed apps and packages](displaying-managed-apps-and-packages.md)
- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)
- [Implementing the simple authentication account-driven enrollment flow](implementing-the-simple-authentication-user-enrollment-flow.md)
- [Managing MDM Devices and Users in macOS](managing-mdm-devices-and-users-in-macos.md)
- [Migrating managed devices](migrating-managed-devices.md)
- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

Specify `com.apple.mdm` as the payload type.

Also define the following four standard payload values in your MDM payload:

- **`PayloadIdentifier`**: The reverse-DNS style identifier that identifies the profile; for example, `com.example.myprofile`. The system uses this value to determine whether to replace an existing profile or add a new one.
- **`PayloadUUID`**: A globally unique identifier for the profile. In macOS, you can use `uuidgen` to generate this value.
- **`PayloadType`**: The payload type. Set to `com.apple.mdm` to designate that this payload is an MDM payload.
- **`PayloadVersion`**: The version number of the profile format, which describes the version of the configuration profile as a whole, not of the individual profiles within it. Set this value to `1`.

> **Note**:  MDM reserves profile payload dictionary keys with the *Payload* prefix. Don’t treat them as managed preferences.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Allow manual install | iOS, macOS, tvOS, visionOS |
| Requires supervision | watchOS |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadContent</key>
            <data>
            LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZlRENDQTJB
            Q0NRQzFsWFV5WnJPbERqQU5CZ2txaGtpRzl3MEJBUXNGQURCK01R
            c3dDUVlEVlFRR0V3SlYKVXpFVE1CRUdBMVVFQ0F3S1EyRnNhV1p2
            Y201cFlURVNNQkFHQTFVRUJ3d0pRM1Z3WlhKMGFXNXZNUk13RVFZ
            RApWUVFLREFwQmNIQnNaU0JKYm1NdU1Sb3dHQVlEVlFRTERCRkVa
            WFpwWTJVZ1RXRnVZV2RsYldWdWRERVZNQk1HCkExVUVBd3dNVFVN
            Z1VtOXZkQ0JEWlhKME1CNFhEVEU1TURVd01UQTNNVFF6TVZvWERU
            STVNRFF5T0RBM01UUXoKTVZvd2ZqRUxNQWtHQTFVRUJoTUNWVk14
            RXpBUkJnTlZCQWdNQ2tOaGJHbG1iM0p1YVdFeEVqQVFCZ05WQkFj
            TQpDVU4xY0dWeWRHbHViekVUTUJFR0ExVUVDZ3dLUVhCd2JHVWdT
            VzVqTGpFYU1CZ0dBMVVFQ3d3UlJHVjJhV05sCklFMWhibUZuWlcx
            bGJuUXhGVEFUQmdOVkJBTU1ERTFESUZKdmIzUWdRMlZ5ZERDQ0Fp
            SXdEUVlKS29aSWh2Y04KQVFFQkJRQURnZ0lQQURDQ0Fnb0NnZ0lC
            QUpZVUFISWErRHI1Q0JzeEQ5NjJTRTc1WG50UzNmTEYyRGJIdHFT
            YwpwdXpsRVhEeC8yaXNVWHVKVkhYdlNkWkx3YmpFRFJKMTF5WlNv
            SzFTMTJVOFVUS1VsK2JHUS9HbjcxVkJnblY2CmFxYmRWVzRFOGxJ
            bU1rN2paRE1IMW14a3cxOWZHdEREaEVOMTA1R3g3K2RVbkpzMTdz
            NHAramJIUThwbzNIY2sKNG5VejgyVTZKUmJXdU5SZFNxNWIvaDNT
            VzlBM2laMXRPRHlNbExOK1ZyaHREYkxhRS9URlk1eFovdjRiUmZ2
            RQpGSjYvVVQ2bGc3RVorcjBYdnljV0tvMnZUL2ZPdUVHbU5CczFy
            YmNPZ3dpQlZEUjdXRG5Pb3RUVkHtMUxydFZFCmFtVlljUHdxSjlu
            Y01hSk14Y01JNHZDazR4eFBwNy9jeEJzcGQwK2diR1lYSVlkYnI5
            YlM2Q1RhMHkzTmIxeCsKdnJZN1RTWFBHSFRNQzAvYXBQQ21CRjBy
            RFdzNm1ZcytFKzRQaENLaDUyeFRROHp5WjVRNk5yOVhqUVJKajl2
            YgpKa2pMMTY1NnJwVFBFV21CUzJxQ1ZqTUxpbFA4MGE1MDVkd0kx
            YzZwa1NrUDczMGtIaExtQ1R4ZkJwb1Jid1p5CjFrQk1qM2xhWkE5
            Y21UUlFiT1pQMkYzNVVudmw1LzFuNG5Wd0N4R1Mzc2U1NWxudzh3
            SzUvRmtBYXptS1dDdzAKTnZjRUc5T0FtQUIrNWpaVVdNZXdoenFy
            TWdMUDFQbm1qR0twemN0dG8vTmxQZE91QVhnZ1A0ZjlPaVkyNlV4
            UwpHcW55R2hXamlIbTZIeXkvMWNuNXRYZVNMcVZISzZoaXJINk1o
            eks4K0R5Rkg2N0R3dmIyTnRKUkhadUhTb0FXClRwS2ZBZ01CQUFF
            d0RRWUpLb1pJaHZjTkFSSUxCUUFEZ2dJQkFHVWl4VDEwaW5KcVVq
            b0NtTWpHNlJwL1hGRUgKZzZoQml6OFUveVJWUEhvMG9RNFREdnIw
            WDBFOXk3Lyt3YXc5clpIRTdqd1VOendtWXZFeWwwMzZCcFQyVVZB
            aQpvWDAyMDZqcmVXSk9nTVYxbFlBVWhYZTY1eml2ak9WRE9rVFFX
            aUZKb3pjbXYwdXZabmsrRWl4eFByUEJYOThOClhRNEF5VWt5S25n
            WTVHSnlPbW5iK3ZnUlFCM25yTXpJbXIyekxNUlp2b21DT1pEV0FK
            ZGF3UlNZTXBFOGZreVAKZnY3QzVWOXdLVllxVFJNd1FEbk1YL1g5
            eUFUTXV0QWV0MTV3N2taN3JYenc4ZFxjZFBwMlBSQkJIem1kWWF3
            egpmbFdWT2dBKzdHSTcwVkVtNER6UkxCVmJjaUcyZU1mVEtYemZX
            eGcrbHhQaWxacy82T2Y1aG9jdVRWeVhEeHJnCkUwRDZLbFVSK2k0
            N3ovZDRTaWsrSVdJRkx3Y21XOEhFelEyVzlTakFwSDRTaGhEKzBz
            UXQ2bzZMNjA0cjBqTzEKbUhYbkhxSmNGRmVaYjlONzJrMElNZTJv
            MForaXd1YmJYamZQZzlMV1EzamVJOVJPZkJzWlA1ZkE1MkxiRlB5
            UgpiSkxOODl4cm5DeEt2TzVsUHp2WHpwYXlrRUNWRG1Oa0lZMlRO
            WG4yUnVmQVdDYXpFVWlLd2lPQ1JLZjJSTHBPCmZUb25IYVdIZi9B
            NzBqWTJXb1JGQ3laV1BnQ3U2QW1kMFNNK3p2cm1NQi9SLzZBYlQv
            WDFjckFQR1ArNkVzU0YKeHBkRHJqZUdLYWlYM3l0UmVBSnFFMEFQ
            YWt4OENXR2haMkVVOUlnY3loNTE2bGY4OXlUcTBEbGlCUjNDWVJl
            bgpsMGJhMSt6M1J6VlZhRWgvCi0tLS0tRU5EIENFUlRJRklDQVRF
            LS0tLS0K
            </data>
            <key>PayloadIdentifier</key>
            <string>com.example.mypempayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.pem</string>
            <key>PayloadUUID</key>
            <string>0dfe81fe-e8f6-45c0-9860-2c893fe30114</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
        <dict>
            <key>PayloadContent</key>
            <dict>
                <key>URL</key>
                <string>https://mdm.example.com:2002/scep</string>
                <key>Key Type</key>
                <string>RSA</string>
                <key>Key Usage</key>
                <integer>5</integer>
                <key>Keysize</key>
                <integer>2048</integer>
                <key>Subject</key>
                <array>
                    <array>
                        <array>
                            <string>O</string>
                            <string>Example, Inc.</string>
                        </array>
                    </array>
                    <array>
                        <array>
                            <string>CN</string>
                            <string>Device Certificate</string>
                        </array>
                    </array>
                </array>
                <key>Challenge</key>
                <string>MDMEnrollment</string>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.mysceppayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.scep</string>
            <key>PayloadUUID</key>
            <string>47492623-e4e7-4a64-ba63-2f31d2ca1a5f</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
        <dict>
            <key>IdentityCertificateUUID</key>
            <string>47492623-e4e7-4a64-ba63-2f31d2ca1a5f</string>
            <key>ServerURL</key>
            <string>https://mdm.example.com:2001/mdm</string>
            <key>Topic</key>
            <string>com.apple.mgmt.External.c809ab17-1cbd-48f2-8dc7-e952131df20c</string>
            <key>AccessRights</key>
            <integer>8191</integer>
            <key>ServerCapabilities</key>
            <array>
                <string>com.apple.mdm.per-user-connections</string>
                <string>com.apple.mdm.bootstraptoken</string>
            </array>
            <key>CheckInURL</key>
            <string>https://mdm.example.com:2001/checkin</string>
            <key>CheckOutWhenRemoved</key>
            <true/>
            <key>PromptUserToAllowBootstrapTokenForAuthentication</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mymdmpayload</string>
            <key>PayloadType</key>
            <string>com.apple.mdm</string>
            <key>PayloadUUID</key>
            <string>0ae4af50-590a-4478-b540-aa0a21da23f1</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>MDM</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>1f4ef23b-ab01-45b9-879c-7a036e47b083</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `AccessRights` (integer): Logical OR of the following bit flags: - `1`: Allow inspection of installed configuration profiles.
- `2`: Allow installation and removal of configuration profiles.
- `4`: Allow device lock and passcode removal.
- `8`: Allow device erase.
- `16`: Allow query of device information (device capacity, serial number).
- `32`: Allow query of network information (phone/SIM numbers, MAC addresses).
- `64`: Allow inspection of installed provisioning profiles.
- `128`: Allow installation and removal of provisioning profiles.
- `256`: Allow inspection of installed applications.
- `512`: Allow restriction-related queries.
- `1024`: Allow security-related queries.
- `2048`: Allow manipulation of settings.
- `4096`: Allow app management. Don’t set to `0`. Specify `1` if you specify `2`. Specify `64` if you specify `128`. Ignored if you set a value for `ManagedAppleID`. > **Note**:  When updating the payload, the addition of any access right is an error, and the update is rejected.
- `AssignedManagedAppleID` (string): The Managed Apple Account pre-assigned to the authenticated user. Required for account-driven enrollments. Available in iOS 15 and later, and macOS 14 and later. > **Note**:  When updating the payload, the value of this key must not change. Any change is an error, and the update is rejected.
- `CheckInURL` (string): The URL that the device should use to check in during installation. The URL must begin with the `https://` URL scheme and may contain a port number (`:1234`, for example). If not set, the system uses `ServerURL`. > **Note**:  When updating the payload, the value of this key must not change. Any change is an error, and the update is rejected.
- `CheckInURLPinningCertificateUUIDs` ([string]): An array of strings, each containing the payload UUID of a certificate to use when evaluating trust to the ‘…/checkin/’ URLs of MDM servers.
- `CheckOutWhenRemoved` (boolean): If ‘true’, the device attempts to send a [`Check Out`](check-out.md) message to the ‘CheckInURL’ when the profile is removed.
- `EnrollmentMode` (string): The enrollment mode the server indicates to use when enrolling. Required for account-driven enrollment. Available in iOS 15 and macOS 14, and later. > **Note**:  When updating the payload, the value of this key must not change. Any change is an error, and the update is rejected.
- `IdentityCertificateUUID` (string) *(required)*: The UUID of the certificate payload for the device’s identity. It may also point to a SCEP payload.
- `PinningRevocationCheckRequired` (boolean): If ‘true’, the system fails the connection attempt unless it obtains a verified positive response during certificate revocation checks. If ‘false’, the system performs revocation checks on a best-attempt basis, where failure to reach the server isn’t considered fatal.
- `PromptUserToAllowBootstrapTokenForAuthentication` (boolean): If ‘true’, the system warns the user that they need to reboot into RecoveryOS and allow the MDM to use the bootstrap token for authentication for certain sensitive operations such as enabling kernel extensions or installing some types of software updates. If the MDM doesn’t need to perform these operations, it can leave this key set to ‘false’, and the user isn’t notified. The SettingsCommand.Command.Settings.MDMOptions.MDMOptions command overrides this default value. This setting only applies to devices that have ‘BootstrapTokenRequiredForSoftwareUpdate’ or ‘BootstrapTokenRequiredForKernelExtensionApproval’ set to ‘true’ in their SecurityInfoResponse.SecurityInfo. DEP-enrolled devices are automatically allowed to use the bootstrap token for authentication. Available in macOS 11 and later.
- `RequiredAppIDForMDM` (integer): This property specifies an iTunes Store ID for an app the system can install with the InstallApplicationCommand, without any approval from the user. The MDM vendor or managing organization generally provides this app, which enhances the management experience for the user. The device shows the user details about this app in the account-driven enrollment process prior to installing the MDM profile. Use this property with account-driven MDM enrollments that normally require user approval for app installs through MDM. Only account-driven enrollments support this property and other enrollment types ignore it. Available in iOS 15.1 and later. > **Note**:  When updating the payload, the value of this key must not change. Any change is an error, and the update is rejected.
- `ServerCapabilities` ([string]): A unique array of strings indicating server capabilities: - `com.apple.mdm.per-user-connections`: Indicates that the server supports both device and user connections. This must be present when managing Shared iPad or macOS devices.
- `com.apple.mdm.bootstraptoken`: Indicates that the server supports escrowing the bootstrap token. This must be present for the device to create a bootstrap token and send it to the server. Available in iOS 26 and later, macOS 11 and later, and visionOS 26 and later.
- `com.apple.mdm.token`: Indicates that the server supports the [`Get Token`](get-token.md) CheckIn message type. This must be present for the device to use [`Get Token`](get-token.md) CheckIn message when appropriate. > **Note**:  When updating the payload, the `com.apple.mdm.per-user-connections` capability must not be added or removed. Any such change is an error, and the update is rejected.
- `ServerURL` (string) *(required)*: The URL that the device contacts to retrieve device management instructions. The URL must begin with the `https://` URL scheme, and may contain a port number (`:1234`, for example). > **Note**:  When updating the payload, the value of this key must not change. Any change is an error, and the update is rejected.
- `ServerURLPinningCertificateUUIDs` ([string]): An array of strings, each containing the UUID of a certificate to use when evaluating trust to the ‘…/connect/’ URLs of MDM servers.
- `SignMessage` (boolean): If ‘true’, each message coming from the device carries the additional ‘Mdm-Signature’ HTTP header.
- `Topic` (string) *(required)*: The topic that MDM listens to for push notifications. The certificate that the server uses to send push notifications must have the same topic in its subject. The topic must begin with the ‘com.apple.mgmt.’ prefix. > **Note**:  When updating the payload, the value of this key must not change. Any change is an error, and the update is rejected.
- `UseDevelopmentAPNS` (boolean): If ‘true’, the device uses the development APNS servers. Otherwise, the device uses the production servers. Set to ‘false’ if your Apple Push Notification Service certificate was issued by the Apple Push Certificate Portal (‘https://identity.apple.com/pushcert’). That portal only issues certificates for the production push environment.

## See Also

- [object EducationConfiguration](educationconfiguration.md)
  The payload that configures the users, groups, and departments within an educational organization.
- [object LightsOutManagementLOM](lightsoutmanagementlom.md)
  The payload that configures lights-out management (LOM) settings.
- [object ManagedPreferences](managedpreferences.md)
  The payload that configures managed preferences.
- [object ProfileRemovalPassword](profileremovalpassword.md)
  The payload that configures profile removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mdm)*