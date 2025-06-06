# Authentication Types

**Framework**: Open Directory

Types of authentication available in Open Directory.

## Topics

### Constants
- [let kODAuthenticationType2WayRandom: String](kodauthenticationtype2wayrandom.md)
  The authentication type used to specify two way random authentication.
- [let kODAuthenticationType2WayRandomChangePasswd: String](kodauthenticationtype2wayrandomchangepasswd.md)
  The authentication type used to change a user’s password using two way random authentication.
- [let kODAuthenticationTypeAPOP: String](kodauthenticationtypeapop.md)
  The authentication type used to specify APOP authentication.
- [let kODAuthenticationTypeCRAM_MD5: String](kodauthenticationtypecram_md5.md)
  The authentication type used to specify CRAM MD5 authentication.
- [let kODAuthenticationTypeChangePasswd: String](kodauthenticationtypechangepasswd.md)
  The authentication type used to change a user’s password using CRAM MD5 authentication.
- [let kODAuthenticationTypeClearText: String](kodauthenticationtypecleartext.md)
  The authentication type used to specify cleartext authentication.
- [let kODAuthenticationTypeCrypt: String](kodauthenticationtypecrypt.md)
  The authentication type used to specify crypt authentication, which uses a crypt password stored in a user’s record if available.
- [let kODAuthenticationTypeDIGEST_MD5: String](kodauthenticationtypedigest_md5.md)
  The authentication type used to specify digest MD5 authentication.
- [let kODAuthenticationTypeDeleteUser: String](kodauthenticationtypedeleteuser.md)
  The authentication type used to specify that a user on an Apple password server be deleted.
- [let kODAuthenticationTypeGetEffectivePolicy: String](kodauthenticationtypegeteffectivepolicy.md)
  The authentication type used to access the policies applied to a user.
- [let kODAuthenticationTypeGetGlobalPolicy: String](kodauthenticationtypegetglobalpolicy.md)
  The authentication type used to access the global authentication policy.
- [let kODAuthenticationTypeGetKerberosPrincipal: String](kodauthenticationtypegetkerberosprincipal.md)
  The authentication type used to access the name of the Kerberos principal.
- [let kODAuthenticationTypeGetPolicy: String](kodauthenticationtypegetpolicy.md)
  The authentication type used to specify that the plug-in should determine the authentication method to use.
- [let kODAuthenticationTypeGetUserData: String](kodauthenticationtypegetuserdata.md)
  The authentication type used to access user data on an Apple password server.
- [let kODAuthenticationTypeGetUserName: String](kodauthenticationtypegetusername.md)
  The authentication type used to access a username on an Apple password server.
- [let kODAuthenticationTypeKerberosTickets: String](kodauthenticationtypekerberostickets.md)
  The authentication type used to provide write access to LDAP with an existing Kerberos ticket.
- [let kODAuthenticationTypeMPPEMasterKeys: String](kodauthenticationtypemppemasterkeys.md)
  The authentication type used to specify primary keys for MPPE encryption.
- [let kODAuthenticationTypeMSCHAP2: String](kodauthenticationtypemschap2.md)
  The authentication type used to specify MS-CHAPv2 encryption.
- [let kODAuthenticationTypeNTLMv2: String](kodauthenticationtypentlmv2.md)
  The authentication type used to verify an NTLMv2 challenge and response.
- [let kODAuthenticationTypeNTLMv2WithSessionKey: String](kodauthenticationtypentlmv2withsessionkey.md)
  The authentication type used to verify an NTLMv2 challenge and response and retrieve session keys in a single call.
- [let kODAuthenticationTypeNewUser: String](kodauthenticationtypenewuser.md)
  The authentication type used to create a new user on an Apple password server.
- [let kODAuthenticationTypeNewUserWithPolicy: String](kodauthenticationtypenewuserwithpolicy.md)
  The authentication type used to create a new user with specified policy settings on an Apple password server.
- [let kODAuthenticationTypeNodeNativeClearTextOK: String](kodauthenticationtypenodenativecleartextok.md)
  The authentication type used to specify that the plug-in should determine the authentication method to use. It also specifies that cleartext is an acceptable authentication method.
- [let kODAuthenticationTypeNodeNativeNoClearText: String](kodauthenticationtypenodenativenocleartext.md)
  The authentication type used to specify that the plug-in should determine the authentication method to use. It also specifies that cleartext is not an acceptable authentication method.
- [let kODAuthenticationTypeReadSecureHash: String](kodauthenticationtypereadsecurehash.md)
  The authentication type used to access the SHA1 or seeded SHA1 hash for a local user.
- [let kODAuthenticationTypeSMBNTv2UserSessionKey: String](kodauthenticationtypesmbntv2usersessionkey.md)
  The authentication type used to generate an NTLMv2 user session key.
- [let kODAuthenticationTypeSMBWorkstationCredentialSessionKey: String](kodauthenticationtypesmbworkstationcredentialsessionkey.md)
  The authentication type used to generate an SMB workstation credential session key.
- [let kODAuthenticationTypeSMB_LM_Key: String](kodauthenticationtypesmb_lm_key.md)
  The authentication type used to specify SMB LAN manager authentication.
- [let kODAuthenticationTypeSMB_NT_Key: String](kodauthenticationtypesmb_nt_key.md)
  The authentication type used to specify SMB NT authentication.
- [let kODAuthenticationTypeSMB_NT_UserSessionKey: String](kodauthenticationtypesmb_nt_usersessionkey.md)
  The authentication type used by Samba to access session keys on an Apple password server.
- [let kODAuthenticationTypeSMB_NT_WithUserSessionKey: String](kodauthenticationtypesmb_nt_withusersessionkey.md)
  The authentication type used by Samba to authenticate and access session keys on an Apple password server.
- [let kODAuthenticationTypeSetGlobalPolicy: String](kodauthenticationtypesetglobalpolicy.md)
  The authentication type used to set the global authentication policy.
- [let kODAuthenticationTypeSetLMHash: String](kodauthenticationtypesetlmhash.md)
  The authentication type used to set the LAN manager hash for an account.
- [let kODAuthenticationTypeSetNTHash: String](kodauthenticationtypesetnthash.md)
  The authentication type used to set the NT hash for a user.
- [let kODAuthenticationTypeSetPassword: String](kodauthenticationtypesetpassword.md)
  The authentication type used to set a password.
- [let kODAuthenticationTypeSetPasswordAsCurrent: String](kodauthenticationtypesetpasswordascurrent.md)
  The authentication type used to set a password using the current credentials.
- [let kODAuthenticationTypeSetPolicy: String](kodauthenticationtypesetpolicy.md)
  The authentication type used to specify that the plug-in should determine the authentication method to use.
- [let kODAuthenticationTypeSetPolicyAsCurrent: String](kodauthenticationtypesetpolicyascurrent.md)
  The authentication type used to set the authentication policy using the current credentials.
- [let kODAuthenticationTypeSetUserData: String](kodauthenticationtypesetuserdata.md)
  The authentication type used to set user data on an Apple password server.
- [let kODAuthenticationTypeSetUserName: String](kodauthenticationtypesetusername.md)
  The authentication type used to set a username on an Apple password server.
- [let kODAuthenticationTypeSetWorkstationPassword: String](kodauthenticationtypesetworkstationpassword.md)
  An authentication type used to support PDC SMB interaction with Directory Services.
- [let kODAuthenticationTypeWithAuthorizationRef: String](kodauthenticationtypewithauthorizationref.md)
  The authentication type used to allow root access to local directories with valid authorization.
- [let kODAuthenticationTypeWriteSecureHash: String](kodauthenticationtypewritesecurehash.md)
  The authentication type used to enable a root process to write the secure hash of a user record.
- [let kODAuthenticationTypeSetCertificateHashAsCurrent: String](kodauthenticationtypesetcertificatehashascurrent.md)
  An authentication type to set the certificate using the authenticated user’s credentials.

## See Also

- [Session Keys](session-keys.md)
  Keys used when specifying session information.
- [Node Types](1497602-node-types.md)
  Open Directory node types.
- [Match Types](match-types.md)
  Types of matches used for searches.
- [Record Types](record-types.md)
  Types of Open Directory records.
- [General Attribute Types](general-attribute-types.md)
  Types of Open Directory attributes.
- [Configuration Attribute Types](configuration-attribute-types.md)
  Types of Open Directory attributes specifically for use with configure nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/authentication-types)*