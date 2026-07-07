# WiFi.EAPClientConfiguration

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that configures an enterprise network.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
object WiFi.EAPClientConfiguration
```

## Properties

- `AcceptEAPTypes` ([integer]) *(required)*: The EAP types that the system accepts. Allowed values: - `13`: EAP-TLS
- `17`: LEAP
- `18`: EAP-SIM
- `21`: EAP-TTLS
- `23`: EAP-AKA
- `25`: PEAPv0/v1
- `43`: EAP-FAST For EAP-TLS authentication without a network payload, install the necessary identity certificates and have your users select EAP-TLS mode in the 802.1X credentials dialog that appears when they connect to the network. For other EAP types, a network payload is necessary and must specify the correct settings for the network.
- `EAPFASTProvisionPAC` (boolean): If ‘true’, allows PAC provisioning. This value is only applicable if ‘EAPFASTUsePAC’ is ‘true’. This value must be ‘true’ for EAP-FAST PAC usage to succeed because there’s no other way to provision a PAC.
- `EAPFASTProvisionPACAnonymously` (boolean): If ‘true’, provisions the device anonymously. Note that there are known machine-in-the-middle attacks for anonymous provisioning.
- `EAPFASTUsePAC` (boolean): If ‘true’, the device uses an existing PAC if it’s present. Otherwise, the server must present its identity using a certificate.
- `EAPSIMNumberOfRANDs` (integer): The minimum number of RAND values to accept from the server. For use with EAP-SIM only. Available: iOS 8+ | iPadOS 8+ | macOS 10.7+ | tvOS 9+ | visionOS 1+ | watchOS 3.2+
- `OneTimeUserPassword` (boolean): If ‘true’, the user receives a prompt for a password each time they connect to the network. Available: iOS 8+ | iPadOS 8+ | macOS 10.8+ | tvOS 9+ | visionOS 1+ | watchOS 3.2+
- `OuterIdentity` (string): A name that hides the user’s true name. The user’s actual name appears only inside the encrypted tunnel. For example, you might set this to anonymous or anon, or anon@mycompany.net. It can increase security because an attacker can’t see the authenticating user’s name in the clear. This key is only relevant to TTLS, PEAP, and EAP-FAST. This field is required if ‘TLSMinimumVersion’ is ‘1.3’.
- `PayloadCertificateAnchorUUID` ([string]): An array of the UUID of each certificate payload in the same profile to trust for authentication. Use this key to prevent the device from asking the user whether to trust the listed certificates. The device disables dynamic trust (the certificate dialogue) if you specify this property without also enabling ‘TLSAllowTrustExceptions’.
- `SystemModeCredentialsSource` (string): Set this string to ‘ActiveDirectory’ to use the AD computer name and password credentials. If using this property, you can’t use ‘SystemModeUseOpenDirectoryCredentials’.
- `SystemModeUseOpenDirectoryCredentials` (boolean): If ‘true’, the system mode connection tries to use the Open Directory credentials. If using this property, you can’t use ‘SystemModeCredentialsSource’.
- `TLSCertificateIsRequired` (boolean): If ‘true’, allows for two-factor authentication for EAP-TTLS, PEAP, or EAP-FAST. If ‘false’, allows for zero-factor authentication for EAP-TLS. If you don’t specify a value, the default is ‘true’ for EAP-TLS, and ‘false’ for other EAP types. Available: iOS 7+ | iPadOS 7+ | macOS 10.7+ | tvOS 9+ | visionOS 1+ | watchOS 3.2+
- `TLSMaximumVersion` (string): The maximum TLS version for EAP authentication. Available: iOS 11+ | iPadOS 11+ | macOS 10.13+ | tvOS 11+ | visionOS 1+ | watchOS 3.2+
- `TLSMinimumVersion` (string): The minimum TLS version for EAP authentication. Available: iOS 11+ | iPadOS 11+ | macOS 10.13+ | tvOS 11+ | visionOS 1+ | watchOS 3.2+
- `TLSTrustedCertificates` ([string]): An array of trusted certificates. Each entry in the array must contain certificate data that represents an anchor certificate used for verifying the server certificate.
- `TLSTrustedServerNames` ([string]): The list of accepted server certificate common names. If a server presents a certificate that isn’t in this list, the system doesn’t trust it. If you specify this property, the system disables dynamic trust (the certificate dialog) unless you also specify ‘TLSAllowTrustExceptions’ with the value ‘true’. If necessary, use a single “*” character to specify a wildcard for an individual component of the name, such as ‘wpa.*.example.com’.
- `TTLSInnerAuthentication` (string): The inner authentication that the TTLS module uses.
- `UserName` (string): The user name for the account. If you don’t specify a value, the system prompts the user during login.
- `UserPassword` (string): The user’s password. If you don’t specify a value, the system prompts the user during login.

## See Also

- [object WiFi.QoSMarkingPolicy](wifi/qosmarkingpolicy-data.dictionary.md)
  A dictionary that defines the quality-of-service settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifi/eapclientconfiguration-data.dictionary)*