# Item attribute keys and values

**Framework**: Security

Specify the attributes of keychain items.

#### Overview

In addition to the data that you want to store, keychain items also have attributes that allow you to find them later and that allow you to control how the data is used or shared.

You specify attributes as the keys and values of a dictionary. The available attribute keys are listed below. Typically, the corresponding value is a string, a number, or some other basic type, as given in each key description. In a few cases, the value comes instead from a list of a known constants. These predefined attribute values are also listed below, grouped according to the key that they serve.

> **Note**:  Not all attributes apply to every item class. You can find the list of attributes applicable to a given class in the relevant item class value definition, namely in [`kSecClassGenericPassword`](ksecclassgenericpassword.md), [`kSecClassInternetPassword`](ksecclassinternetpassword.md), [`kSecClassCertificate`](ksecclasscertificate.md), [`kSecClassIdentity`](ksecclassidentity.md), or [`kSecClassKey`](ksecclasskey.md).

## Topics

### General Item Attribute Keys
- [let kSecAttrAccess: CFString](ksecattraccess.md)
  A key with a value that indicates access control list settings for the item.
- [let kSecAttrAccessControl: CFString](ksecattraccesscontrol.md)
  A key with a value that’s an access control instance indicating access control settings for the item.
- [let kSecAttrAccessible: CFString](ksecattraccessible.md)
  A key with a value that indicates when the keychain item is accessible.
- [let kSecAttrAccessGroup: CFString](ksecattraccessgroup.md)
  A key with a value that’s a string indicating the access group the item is in.
- [let kSecAttrSynchronizable: CFString](ksecattrsynchronizable.md)
  A key with a value that’s a string indicating whether the item synchronizes through iCloud.
- [let kSecAttrCreationDate: CFString](ksecattrcreationdate.md)
  A key with a value that indicates the item’s creation date.
- [let kSecAttrModificationDate: CFString](ksecattrmodificationdate.md)
  A key with a value that indicates the item’s most recent modification date.
- [let kSecAttrDescription: CFString](ksecattrdescription.md)
  A key with a value that’s a string indicating the item’s description.
- [let kSecAttrComment: CFString](ksecattrcomment.md)
  A key with a value that’s a string indicating a comment associated with the item.
- [let kSecAttrCreator: CFString](ksecattrcreator.md)
  A key with a value that indicates the item’s creator.
- [let kSecAttrType: CFString](ksecattrtype.md)
  A key with a value that indicates the item’s type.
- [let kSecAttrLabel: CFString](ksecattrlabel.md)
  A key with a value that’s a string indicating the item’s label.
- [let kSecAttrIsInvisible: CFString](ksecattrisinvisible.md)
  A key with a value that’s a Boolean indicating the item’s visibility.
- [let kSecAttrIsNegative: CFString](ksecattrisnegative.md)
  A key with a value that’s a Boolean indicating whether the item has a valid password.
- [let kSecAttrSyncViewHint: CFString](ksecattrsyncviewhint.md)
  A key with a value that’s a string that provides a sync view hint.
- [let kSecAttrPersistantReference: CFString](ksecattrpersistantreference.md)
- [let kSecAttrPersistentReference: CFString](ksecattrpersistentreference.md)
- [let kSecUseUserIndependentKeychain: CFString](ksecuseuserindependentkeychain.md)
  A key with a value that indicates whether to store the data in a keychain available to anyone who uses the device.
### Password Attribute Keys
- [let kSecAttrAccount: CFString](ksecattraccount.md)
  A key whose value is a string indicating the item’s account name.
- [let kSecAttrService: CFString](ksecattrservice.md)
  A key whose value is a string indicating the item’s service.
- [let kSecAttrGeneric: CFString](ksecattrgeneric.md)
  A key whose value indicates the item’s user-defined attributes.
- [let kSecAttrSecurityDomain: CFString](ksecattrsecuritydomain.md)
  A key whose value is a string indicating the item’s security domain.
- [let kSecAttrServer: CFString](ksecattrserver.md)
  A key whose value is a string indicating the item’s server.
- [let kSecAttrProtocol: CFString](ksecattrprotocol.md)
  A key whose value indicates the item’s protocol.
- [let kSecAttrAuthenticationType: CFString](ksecattrauthenticationtype.md)
  A key whose value indicates the item’s authentication scheme.
- [let kSecAttrPort: CFString](ksecattrport.md)
  A key whose value indicates the item’s port.
- [let kSecAttrPath: CFString](ksecattrpath.md)
  A key whose value is a string indicating the item’s path attribute.
### Certificate Attribute Keys
- [let kSecAttrSubject: CFString](ksecattrsubject.md)
  A key whose value indicates the item’s subject name.
- [let kSecAttrIssuer: CFString](ksecattrissuer.md)
  A key whose value indicates the item’s issuer.
- [let kSecAttrSerialNumber: CFString](ksecattrserialnumber.md)
  A key whose value indicates the item’s serial number.
- [let kSecAttrSubjectKeyID: CFString](ksecattrsubjectkeyid.md)
  A key whose value indicates the item’s subject key ID.
- [let kSecAttrPublicKeyHash: CFString](ksecattrpublickeyhash.md)
  A key whose value indicates the item’s public key hash.
- [let kSecAttrCertificateType: CFString](ksecattrcertificatetype.md)
  A key whose value indicates the item’s certificate type.
- [let kSecAttrCertificateEncoding: CFString](ksecattrcertificateencoding.md)
  A key whose value indicates the item’s certificate encoding.
### Cryptographic Key Attribute Keys
- [let kSecAttrKeyClass: CFString](ksecattrkeyclass.md)
  A key whose value indicates the item’s cryptographic key class.
- [let kSecAttrApplicationLabel: CFString](ksecattrapplicationlabel.md)
  A key whose value indicates the item’s application label.
- [let kSecAttrApplicationTag: CFString](ksecattrapplicationtag.md)
  A key whose value indicates the item’s private tag.
- [let kSecAttrKeyType: CFString](ksecattrkeytype.md)
  A key whose value indicates the item’s algorithm.
- [let kSecAttrPRF: CFString](ksecattrprf.md)
  A key whose value indicates the item’s pseudorandom function.
- [let kSecAttrSalt: CFString](ksecattrsalt.md)
  A key whose value indicates the salt to use for this item.
- [let kSecAttrRounds: CFString](ksecattrrounds.md)
  A key whose value indicates the number of rounds to run the pseudorandom function.
- [let kSecAttrKeySizeInBits: CFString](ksecattrkeysizeinbits.md)
  A key whose value indicates the number of bits in a cryptographic key.
- [let kSecAttrEffectiveKeySize: CFString](ksecattreffectivekeysize.md)
  A key whose value indicates the effective number of bits in a cryptographic key.
- [let kSecAttrTokenID: CFString](ksecattrtokenid.md)
  A key whose value indicates that a cryptographic key is in an external store.
### Cryptographic Key Usage Attribute Keys
- [let kSecAttrIsPermanent: CFString](ksecattrispermanent.md)
  A key whose value indicates the item’s permanence.
- [let kSecAttrIsSensitive: CFString](ksecattrissensitive.md)
  A key whose value indicates the item’s sensitivity.
- [let kSecAttrIsExtractable: CFString](ksecattrisextractable.md)
  A key whose value indicates the item’s extractability.
- [let kSecAttrCanEncrypt: CFString](ksecattrcanencrypt.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for encryption.
- [let kSecAttrCanDecrypt: CFString](ksecattrcandecrypt.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for decryption.
- [let kSecAttrCanDerive: CFString](ksecattrcanderive.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for derivation.
- [let kSecAttrCanSign: CFString](ksecattrcansign.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for digital signing.
- [let kSecAttrCanVerify: CFString](ksecattrcanverify.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for signature verification.
- [let kSecAttrCanWrap: CFString](ksecattrcanwrap.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for wrapping.
- [let kSecAttrCanUnwrap: CFString](ksecattrcanunwrap.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for unwrapping.
### Protocol Values
- [let kSecAttrProtocolFTP: CFString](ksecattrprotocolftp.md)
  FTP protocol.
- [let kSecAttrProtocolFTPAccount: CFString](ksecattrprotocolftpaccount.md)
  A client side FTP account.
- [let kSecAttrProtocolHTTP: CFString](ksecattrprotocolhttp.md)
  HTTP protocol.
- [let kSecAttrProtocolIRC: CFString](ksecattrprotocolirc.md)
  IRC protocol.
- [let kSecAttrProtocolNNTP: CFString](ksecattrprotocolnntp.md)
  NNTP protocol.
- [let kSecAttrProtocolPOP3: CFString](ksecattrprotocolpop3.md)
  POP3 protocol.
- [let kSecAttrProtocolSMTP: CFString](ksecattrprotocolsmtp.md)
  SMTP protocol.
- [let kSecAttrProtocolSOCKS: CFString](ksecattrprotocolsocks.md)
  SOCKS  protocol.
- [let kSecAttrProtocolIMAP: CFString](ksecattrprotocolimap.md)
  IMAP  protocol.
- [let kSecAttrProtocolLDAP: CFString](ksecattrprotocolldap.md)
  LDAP protocol.
- [let kSecAttrProtocolAppleTalk: CFString](ksecattrprotocolappletalk.md)
  AFP over AppleTalk.
- [let kSecAttrProtocolAFP: CFString](ksecattrprotocolafp.md)
  AFP over TCP.
- [let kSecAttrProtocolTelnet: CFString](ksecattrprotocoltelnet.md)
  Telnet protocol.
- [let kSecAttrProtocolSSH: CFString](ksecattrprotocolssh.md)
  SSH protocol.
- [let kSecAttrProtocolFTPS: CFString](ksecattrprotocolftps.md)
  FTP over TLS/SSL.
- [let kSecAttrProtocolHTTPS: CFString](ksecattrprotocolhttps.md)
  HTTP over TLS/SSL.
- [let kSecAttrProtocolHTTPProxy: CFString](ksecattrprotocolhttpproxy.md)
  HTTP proxy.
- [let kSecAttrProtocolHTTPSProxy: CFString](ksecattrprotocolhttpsproxy.md)
  HTTPS proxy.
- [let kSecAttrProtocolFTPProxy: CFString](ksecattrprotocolftpproxy.md)
  FTP proxy.
- [let kSecAttrProtocolSMB: CFString](ksecattrprotocolsmb.md)
  SMB protocol.
- [let kSecAttrProtocolRTSP: CFString](ksecattrprotocolrtsp.md)
  RTSP protocol.
- [let kSecAttrProtocolRTSPProxy: CFString](ksecattrprotocolrtspproxy.md)
  RTSP proxy.
- [let kSecAttrProtocolDAAP: CFString](ksecattrprotocoldaap.md)
  DAAP protocol.
- [let kSecAttrProtocolEPPC: CFString](ksecattrprotocoleppc.md)
  Remote Apple Events.
- [let kSecAttrProtocolIPP: CFString](ksecattrprotocolipp.md)
  IPP protocol.
- [let kSecAttrProtocolNNTPS: CFString](ksecattrprotocolnntps.md)
  NNTP over TLS/SSL.
- [let kSecAttrProtocolLDAPS: CFString](ksecattrprotocolldaps.md)
  LDAP over TLS/SSL.
- [let kSecAttrProtocolTelnetS: CFString](ksecattrprotocoltelnets.md)
  Telnet over TLS/SSL.
- [let kSecAttrProtocolIMAPS: CFString](ksecattrprotocolimaps.md)
  IMAP over TLS/SSL.
- [let kSecAttrProtocolIRCS: CFString](ksecattrprotocolircs.md)
  IRC over TLS/SSL.
- [let kSecAttrProtocolPOP3S: CFString](ksecattrprotocolpop3s.md)
  POP3 over TLS/SSL.
### Authentication Type Values
- [let kSecAttrAuthenticationTypeNTLM: CFString](ksecattrauthenticationtypentlm.md)
  Windows NT LAN Manager authentication.
- [let kSecAttrAuthenticationTypeMSN: CFString](ksecattrauthenticationtypemsn.md)
  Microsoft Network default authentication.
- [let kSecAttrAuthenticationTypeDPA: CFString](ksecattrauthenticationtypedpa.md)
  Distributed Password authentication.
- [let kSecAttrAuthenticationTypeRPA: CFString](ksecattrauthenticationtyperpa.md)
  Remote Password authentication.
- [let kSecAttrAuthenticationTypeHTTPBasic: CFString](ksecattrauthenticationtypehttpbasic.md)
  HTTP Basic authentication.
- [let kSecAttrAuthenticationTypeHTTPDigest: CFString](ksecattrauthenticationtypehttpdigest.md)
  HTTP Digest Access authentication.
- [let kSecAttrAuthenticationTypeHTMLForm: CFString](ksecattrauthenticationtypehtmlform.md)
  HTML form based authentication.
- [let kSecAttrAuthenticationTypeDefault: CFString](ksecattrauthenticationtypedefault.md)
  The default authentication type.
### Key Class Values
- [let kSecAttrKeyClassPublic: CFString](ksecattrkeyclasspublic.md)
  A public key of a public-private pair.
- [let kSecAttrKeyClassPrivate: CFString](ksecattrkeyclassprivate.md)
  A private key of a public-private pair.
- [let kSecAttrKeyClassSymmetric: CFString](ksecattrkeyclasssymmetric.md)
  A private key used for symmetric-key encryption and decryption.
### Key Type Values
- [let kSecAttrKeyTypeRSA: CFString](ksecattrkeytypersa.md)
  RSA algorithm.
- [let kSecAttrKeyTypeDSA: CFString](ksecattrkeytypedsa.md)
  DSA algorithm.
- [let kSecAttrKeyTypeAES: CFString](ksecattrkeytypeaes.md)
  AES algorithm.
- [let kSecAttrKeyTypeDES: CFString](ksecattrkeytypedes.md)
  DES algorithm.
- [let kSecAttrKeyType3DES: CFString](ksecattrkeytype3des.md)
  3DES algorithm.
- [let kSecAttrKeyTypeRC4: CFString](ksecattrkeytyperc4.md)
  RC4 algorithm.
- [let kSecAttrKeyTypeRC2: CFString](ksecattrkeytyperc2.md)
  RC2 algorithm.
- [let kSecAttrKeyTypeCAST: CFString](ksecattrkeytypecast.md)
  CAST algorithm.
- [let kSecAttrKeyTypeECDSA: CFString](ksecattrkeytypeecdsa.md)
  Elliptic curve DSA algorithm.
- [let kSecAttrKeyTypeEC: CFString](ksecattrkeytypeec.md)
  Elliptic curve algorithm.
- [let kSecAttrKeyTypeECSECPrimeRandom: CFString](ksecattrkeytypeecsecprimerandom.md)
  Elliptic curve algorithm.
### Synchronizability Values
- [let kSecAttrSynchronizableAny: CFString](ksecattrsynchronizableany.md)
  Specifies that both synchronizable and non-synchronizable results should be returned from a query.
### Token ID Values
- [let kSecAttrTokenIDSecureEnclave: CFString](ksecattrtokenidsecureenclave.md)
  Specifies an item should be stored in the device’s Secure Enclave.
### Accessibility Values
- [let kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFString](ksecattraccessiblewhenpasscodesetthisdeviceonly.md)
  The data in the keychain can only be accessed when the device is unlocked. Only available if a passcode is set on the device.
- [let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFString](ksecattraccessiblewhenunlockedthisdeviceonly.md)
  The data in the keychain item can be accessed only while the device is unlocked by the user.
- [let kSecAttrAccessibleWhenUnlocked: CFString](ksecattraccessiblewhenunlocked.md)
  The data in the keychain item can be accessed only while the device is unlocked by the user.
- [let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFString](ksecattraccessibleafterfirstunlockthisdeviceonly.md)
  The data in the keychain item cannot be accessed after a restart until the device has been unlocked once by the user.
- [let kSecAttrAccessibleAfterFirstUnlock: CFString](ksecattraccessibleafterfirstunlock.md)
  The data in the keychain item cannot be accessed after a restart until the device has been unlocked once by the user.
- [let kSecAttrAccessibleAlwaysThisDeviceOnly: CFString](ksecattraccessiblealwaysthisdeviceonly.md)
  The data in the keychain item can always be accessed regardless of whether the device is locked.
- [let kSecAttrAccessibleAlways: CFString](ksecattraccessiblealways.md)
  The data in the keychain item can always be accessed regardless of whether the device is locked.
### Pseudorandom Function Values
- [let kSecAttrPRFHmacAlgSHA1: CFString](ksecattrprfhmacalgsha1.md)
  Use the SHA1 algorithm.
- [let kSecAttrPRFHmacAlgSHA224: CFString](ksecattrprfhmacalgsha224.md)
  Use the SHA224 algorithm.
- [let kSecAttrPRFHmacAlgSHA256: CFString](ksecattrprfhmacalgsha256.md)
  Use the SHA256 algorithm.
- [let kSecAttrPRFHmacAlgSHA384: CFString](ksecattrprfhmacalgsha384.md)
  Use the SHA384 algorithm.
- [let kSecAttrPRFHmacAlgSHA512: CFString](ksecattrprfhmacalgsha512.md)
  Use the SHA512 algorithm.
### Access Group Values
- [let kSecAttrAccessGroupToken: CFString](ksecattraccessgrouptoken.md)
  The access group containing items provided by external tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/item-attribute-keys-and-values)*