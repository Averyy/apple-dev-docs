# StatusManagementClientCapabilities

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the devices’s protocol capabilities.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusManagementClientCapabilities
```

## Mentions

- [Leveraging the declarative management data model to scale devices](leveraging-the-declarative-management-data-model-to-scale-devices.md)

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |

##### Status Item Example

```json
{
    "management": {
        "client-capabilities": {
            "supported-features": {},
            "supported-payloads": {
                "declarations": {
                    "activations": [
                        "com.apple.activation.simple"
                    ],
                    "assets": [
                        "com.apple.asset.credential.acme",
                        "com.apple.asset.credential.certificate",
                        "com.apple.asset.credential.identity",
                        "com.apple.asset.credential.scep",
                        "com.apple.asset.credential.userpassword",
                        "com.apple.asset.data",
                        "com.apple.asset.useridentity"
                    ],
                    "configurations": [
                        "com.apple.configuration.account.caldav",
                        "com.apple.configuration.account.carddav",
                        "com.apple.configuration.account.exchange",
                        "com.apple.configuration.account.google",
                        "com.apple.configuration.account.ldap",
                        "com.apple.configuration.account.mail",
                        "com.apple.configuration.account.subscribed-calendar",
                        "com.apple.configuration.app.managed",
                        "com.apple.configuration.app.settings",
                        "com.apple.configuration.audio-accessory.settings",
                        "com.apple.configuration.extensible-sso",
                        "com.apple.configuration.external-intelligence.settings",
                        "com.apple.configuration.intelligence.settings",
                        "com.apple.configuration.keyboard.settings",
                        "com.apple.configuration.legacy",
                        "com.apple.configuration.legacy.interactive",
                        "com.apple.configuration.management.status-subscriptions",
                        "com.apple.configuration.management.test",
                        "com.apple.configuration.math.settings",
                        "com.apple.configuration.network.dns-proxy",
                        "com.apple.configuration.network.dns-settings",
                        "com.apple.configuration.network.relay",
                        "com.apple.configuration.network.vpn.always-on",
                        "com.apple.configuration.network.vpn.ikev2",
                        "com.apple.configuration.network.vpn.ipsec",
                        "com.apple.configuration.network.vpn.vpn-plugin",
                        "com.apple.configuration.passcode.settings",
                        "com.apple.configuration.safari.bookmarks",
                        "com.apple.configuration.safari.extensions.settings",
                        "com.apple.configuration.safari.settings",
                        "com.apple.configuration.security.certificate",
                        "com.apple.configuration.security.identity",
                        "com.apple.configuration.security.passkey.attestation",
                        "com.apple.configuration.siri.settings",
                        "com.apple.configuration.softwareupdate.enforcement.specific",
                        "com.apple.configuration.softwareupdate.settings",
                        "com.apple.configuration.watch.enrollment",
                        "com.apple.configuration.webcontent-filter.plugin"
                    ],
                    "management": [
                        "com.apple.management.organization-info",
                        "com.apple.management.properties",
                        "com.apple.management.server-capabilities"
                    ]
                },
                "status-items": [
                    "account.list.caldav",
                    "account.list.carddav",
                    "account.list.exchange",
                    "account.list.google",
                    "account.list.ldap",
                    "account.list.mail.incoming",
                    "account.list.mail.outgoing",
                    "account.list.subscribed-calendar",
                    "app.managed.list",
                    "device.identifier.serial-number",
                    "device.identifier.udid",
                    "device.model.family",
                    "device.model.identifier",
                    "device.model.marketing-name",
                    "device.model.number",
                    "device.operating-system.build-version",
                    "device.operating-system.family",
                    "device.operating-system.marketing-name",
                    "device.operating-system.supplemental.build-version",
                    "device.operating-system.supplemental.extra-version",
                    "device.operating-system.version",
                    "device.power.battery-health",
                    "device.system.health",
                    "enhanced-logging.applecare-token",
                    "enhanced-logging.status",
                    "enhanced-logging.timestamp",
                    "management.client-capabilities",
                    "management.declarations",
                    "mdm.app",
                    "mdm.enrollment-type",
                    "mdm.is-awaiting-configuration",
                    "mdm.is-return-to-service",
                    "mdm.is-shared-ipad",
                    "mdm.push-magic",
                    "mdm.push-token",
                    "passcode.is-compliant",
                    "passcode.is-present",
                    "security.certificate.list",
                    "security.lockdown-mode",
                    "softwareupdate.beta-enrollment",
                    "softwareupdate.device-id",
                    "softwareupdate.failure-reason",
                    "softwareupdate.install-reason",
                    "softwareupdate.install-state",
                    "softwareupdate.pending-version",
                    "test.array-value",
                    "test.boolean-value",
                    "test.dictionary-value",
                    "test.error-value",
                    "test.integer-value",
                    "test.real-value",
                    "test.string-value"
                ]
            },
            "supported-versions": [
                "1.0.0"
            ]
        }
    }
}
```

## Topics

### Objects
- [object StatusManagementClientCapabilitiesCapabilitiesObject](statusmanagementclientcapabilitiescapabilitiesobject.md)
  An object that contains the client’s protocol capabilities. These typically only change when the device upgrades its software. An implicit status subscription for this status item is always present, so the client always reports changes to the server.

## Properties

- `management.client-capabilities` (StatusManagementClientCapabilitiesCapabilitiesObject) *(required)*: An object that contains the client’s protocol capabilities. These typically only change when the device upgrades its software. An implicit status subscription for this status item is always present, so the client always reports changes to the server.

## See Also

- [object StatusManagementDeclarations](statusmanagementdeclarations.md)
  The status item that reports the device’s processed declarations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmanagementclientcapabilities)*