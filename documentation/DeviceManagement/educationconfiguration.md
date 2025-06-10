# EducationConfiguration

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the users, groups, and departments within an educational organization.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.14+

## Declaration

```swift
object EducationConfiguration
```

#### Discussion

Specify `com.apple.education` as the payload type.

In iOS, send this payload over the device channel. Additionally, the system requires supervision unless the payload only specifies as teacher configuration.

In macOS, send this payload over the user channel. The system supports student payloads in macOS 10.14.4 and later.

Additionally, configure:

- All identities as both SSL clients and servers
- All certificates with a key size of at least 2048 bits
- All certificates to use a hashing algorithm of SHA256 or stronger
- Leader certificates to have the common name prefix leader, which is case-insensitive
- Member certificates to have the common name prefix member, which is case-insensitive
- TLS server certificates issued on or after September 1, 2020 00:00 GMT/UTC to have a validity period greater than 398 days; see [`About Upcoming Limits on Trusted Certificates`](https://developer.apple.comhttps://support.apple.com/en-us/HT211025) for more information.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | macOS |
| Allow manual install | iOS, macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS |
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
            <key>Password</key>
            <string>Password123</string>
            <key>PayloadCertificateFileName</key>
            <string>TestServerCert.p12</string>
            <key>PayloadContent</key>
            <data>ExampleD</data>
            <key>PayloadDescription</key>
            <string>Adds a PKCS#12-formatted certificate</string>
            <key>PayloadDisplayName</key>
            <string>LeaderIdentity.p12</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myedconfigpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.pkcs12</string>
            <key>PayloadUUID</key>
            <string>c149dafb-033f-4894-8add-e1056dc1c420</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
        <dict>
            <key>PayloadCertificateFileName</key>
            <string>Cert.cer</string>
            <key>PayloadContent</key>
            <data>ExampleD</data>
            <key>PayloadDescription</key>
            <string>Adds a CA root certificate</string>
            <key>PayloadDisplayName</key>
            <string>leader: Catalyst Certificate</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mycertpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.root</string>
            <key>PayloadUUID</key>
            <string>0391e29c-f10d-4803-a749-d04ef7f6a8fa</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
        <dict>
            <key>OrganizationUUID</key>
            <string>24A9D6AC-9C34-45F3-B92F-88C4657204C9</string>
            <key>OrganizationName</key>
            <string>Example Inc.</string>
            <key>PayloadCertificateUUID</key>
            <string>8DBA6415-6F70-47FE-B0D2-C70B3D35B7A3</string>
            <key>LeaderPayloadCertificateAnchorUUID</key>
            <array>
                <string>c2113db2-8ea9-456d-a2e7-e19f4a706b75</string>
            </array>
            <key>MemberPayloadCertificateAnchorUUID</key>
            <array>
                <string>82c3100d-e22c-42db-b70b-3b628992c757</string>
            </array>
            <key>Departments</key>
            <array>
                <dict>
                    <key>Name</key>
                    <string>Phonetics</string>
                    <key>Identifier</key>
                    <string>NotNeeded</string>
                    <key>GroupBeaconIDs</key>
                    <array>
                        <integer>1</integer>
                        <integer>2</integer>
                        <integer>3</integer>
                    </array>
                </dict>
            </array>
            <key>Groups</key>
            <array>
                <dict>
                    <key>BeaconID</key>
                    <integer>1</integer>
                    <key>Name</key>
                    <string>Phonetic Info Provided</string>
                    <key>LeaderIdentifiers</key>
                    <array>
                        <string>can</string>
                    </array>
                    <key>MemberIdentifiers</key>
                    <array>
                        <string>juan</string>
                        <string>mei</string>
                        <string>tom</string>
                        <string>bill</string>
                    </array>
                </dict>
            </array>
            <key>Users</key>
            <array>
                <dict>
                    <key>Identifier</key>
                    <string>tom</string>
                    <key>Name</key>
                    <string>tom clark</string>
                    <key>GivenName</key>
                    <string>tom</string>
                    <key>FamilyName</key>
                    <string>clark</string>
                    <key>PhoneticGivenName</key>
                    <string>tom</string>
                    <key>PhoneticFamilyName</key>
                    <string>clark</string>
                    <key>AppleID</key>
                    <string>tom</string>
                    <key>ImageURL</key>
                    <string>https://url.example.com.jpg</string>
                    <key>PasscodeType</key>
                    <string>four</string>
                </dict>
                <dict>
                    <key>Identifier</key>
                    <string>Juan</string>
                    <key>Name</key>
                    <string>Juan Chavez</string>
                    <key>GivenName</key>
                    <string>Juan</string>
                    <key>FamilyName</key>
                    <string>Chavez</string>
                    <key>PhoneticGivenName</key>
                    <string>Juan</string>
                    <key>PhoneticFamilyName</key>
                    <string>Chavez</string>
                    <key>AppleID</key>
                    <string>Juan</string>
                    <key>ImageURL</key>
                    <string>https://url.example.com.jpg2</string>
                    <key>PasscodeType</key>
                    <string>four</string>
                </dict>
                <dict>
                    <key>Identifier</key>
                    <string>mei</string>
                    <key>Name</key>
                    <string>mei chen</string>
                    <key>GivenName</key>
                    <string>mei</string>
                    <key>FamilyName</key>
                    <string>chen</string>
                    <key>PhoneticGivenName</key>
                    <string>Mei</string>
                    <key>PhoneticFamilyName</key>
                    <string>Chen</string>
                    <key>AppleID</key>
                    <string>mei</string>
                    <key>ImageURL</key>
                    <string>https://url.example.com.jpg.3</string>
                    <key>PasscodeType</key>
                    <string>six</string>
                </dict>
                <dict>
                    <key>Identifier</key>
                    <string>bill</string>
                    <key>Name</key>
                    <string>bill james</string>
                    <key>GivenName</key>
                    <string>bill</string>
                    <key>FamilyName</key>
                    <string>james</string>
                    <key>PhoneticGivenName</key>
                    <string>Bill</string>
                    <key>PhoneticFamilyName</key>
                    <string>James</string>
                    <key>AppleID</key>
                    <string>bill</string>
                    <key>ImageURL</key>
                    <string>https://url.example.com.jpg.4</string>
                    <key>PasscodeType</key>
                    <string>complex</string>
                </dict>
            </array>
            <key>PayloadDescription</key>
            <string>Configures the EDU mode loginwindow.</string>
            <key>PayloadDisplayName</key>
            <string>EDU mode</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myedconfigpayload</string>
            <key>PayloadType</key>
            <string>com.apple.education</string>
            <key>PayloadUUID</key>
            <string>9AD88C7B-7478-44D0-BEDD-4B1709002916</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Education</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>2E4F6563-21DE-499B-B834-4BCF1F08B5AD3</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object EducationConfiguration.DepartmentsItem](educationconfiguration/departmentsitem.md)
  A department in the organization.
- [object EducationConfiguration.DeviceGroupsItem](educationconfiguration/devicegroupsitem.md)
  A device group in the organization.
- [object EducationConfiguration.GroupsItem](educationconfiguration/groupsitem.md)
  An array of dictionaries defining groups.
- [object EducationConfiguration.UsersItem](educationconfiguration/usersitem.md)
  A user in the organization.

## See Also

- [object LightsOutManagementLOM](lightsoutmanagementlom.md)
  The payload you use to configure lights-out management (LOM) settings.
- [object ManagedPreferences](managedpreferences.md)
  The payload you use to configure managed preferences.
- [object MDM](mdm.md)
  The payload you use to configure mobile device management (MDM) settings.
- [object ProfileRemovalPassword](profileremovalpassword.md)
  The payload you use to configure profile removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/educationconfiguration)*