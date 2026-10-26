# kSCPropNetIPSecXAuthPasswordEncryption

**Framework**: System Configuration  
**Kind**: var  
**Role**: Global Variable

The IPSec key XAuthPasswordEncryption.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let kSCPropNetIPSecXAuthPasswordEncryption: CFString
```

```c
extern CFStringRef const kSCPropNetIPSecXAuthPasswordEncryption;
```

#### Discussion

The value of this key is of type [`CFString`](../CoreFoundation/cfstring.md). This key can accept the following constants:

- [`kSCValNetIPSecXAuthPasswordEncryptionKeychain`](./kscvalnetipsecxauthpasswordencryptionkeychain-swift.var.md), which has the value `Keychain`
- [`kSCValNetIPSecXAuthPasswordEncryptionPrompt`](./kscvalnetipsecxauthpasswordencryptionprompt-swift.var.md), which has the value `Prompt`

## See Also

### Constants
- [let kSCCompAnyRegex: CFString](./ksccompanyregex-swift.var.md)
  A regular expression pattern that matches any component.
- [let kSCPropNetIPSecConnectTime: CFString](./kscpropnetipsecconnecttime-swift.var.md)
  The IPSec key ConnectTime.
- [let kSCPropNetIPSecRemoteAddress: CFString](./kscpropnetipsecremoteaddress-swift.var.md)
  The IPSec key RemoteAddress.
- [let kSCPropNetIPSecStatus: CFString](./kscpropnetipsecstatus-swift.var.md)
  The IPSec key Status.
- [let kSCPropNetIPSecXAuthEnabled: CFString](./kscpropnetipsecxauthenabled-swift.var.md)
  The IPSec key XAuthEnabled.
- [let kSCPropNetIPSecXAuthName: CFString](./kscpropnetipsecxauthname-swift.var.md)
  The IPSec key XAuthName.
- [let kSCPropNetIPSecXAuthPassword: CFString](./kscpropnetipsecxauthpassword-swift.var.md)
  The IPSec key XAuthPassword.
- [let kSCPropNetProxiesProxyAutoConfigJavaScript: CFString](./kscpropnetproxiesproxyautoconfigjavascript-swift.var.md)
  The Proxies key ProxyAutoConfigJavaScript.
- [let kSCResvInactive: CFString](./kscresvinactive-swift.var.md)
  The reserved key __INACTIVE__.
- [let kSCResvLink: CFString](./kscresvlink-swift.var.md)
  The reserved key __LINK__.
- [let kSCValNetIPSecAuthenticationMethodCertificate: CFString](./kscvalnetipsecauthenticationmethodcertificate-swift.var.md)
  The constant value Certificate.
- [let kSCValNetIPSecAuthenticationMethodHybrid: CFString](./kscvalnetipsecauthenticationmethodhybrid-swift.var.md)
  The constant value Hybrid.
- [let kSCValNetIPSecAuthenticationMethodSharedSecret: CFString](./kscvalnetipsecauthenticationmethodsharedsecret-swift.var.md)
  The constant value SharedSecret.
- [let kSCValNetIPSecLocalIdentifierTypeKeyID: CFString](./kscvalnetipseclocalidentifiertypekeyid-swift.var.md)
  The constant value KeyID.
- [let kSCValNetIPSecSharedSecretEncryptionKeychain: CFString](./kscvalnetipsecsharedsecretencryptionkeychain-swift.var.md)
  The constant value Keychain.
- [kCNNetworkInfoKeyBSSID](./kcnnetworkinfokeybssid.md)
  The key for the network’s BSSID, which is represented as a [`CFStringRef`](../CoreFoundation/cfstring.md) object.
- [kCNNetworkInfoKeySSID](./kcnnetworkinfokeyssid.md)
  The key for the network’s SSID, which is represented as a [`CFStringRef`](../CoreFoundation/cfstring.md) object.
- [kCNNetworkInfoKeySSIDData](./kcnnetworkinfokeyssiddata.md)
  The key for the network’s SSID, which is represented as a [`CFDataRef`](../CoreFoundation/cfdata.md) object.
- [kSCPropUsersConsoleUserGID](./kscpropusersconsoleusergid-c.var.md)
  The deprecated key GID.
- [kSCPropUsersConsoleUserName](./kscpropusersconsoleusername-c.var.md)
  The deprecated key Name.
- [kSCPropUsersConsoleUserUID](./kscpropusersconsoleuseruid-c.var.md)
  The deprecated key UID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthpasswordencryption-swift.var)*