# Credential Management

**Framework**: GSS

Securely establish connections between endpoints.

## Topics

### Allocation and Deallocation
- [func GSSCreateCredentialFromUUID(CFUUID) -> gss_cred_id_t?](gsscreatecredentialfromuuid(_:).md)
  Creates a credential from a universally unique identifier.
- [func gss_add_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_name_t?, gss_OID?, gss_cred_usage_t, OM_uint32, OM_uint32, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_add_cred(_:_:_:_:_:_:_:_:_:_:_:).md)
  Adds a new credential element to an existing credential.
- [func gss_set_cred_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_cred_option(_:_:_:_:).md)
  Changes a credential option.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_destroy_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_destroy_cred(_:_:).md)
  Purges a credential from memory.
### Initial Credential Keys
- [var kGSSICPassword: String](kgssicpassword.md)
  The value is a string that indicates a password.
- [var kGSSICCertificate: String](kgssiccertificate.md)
  The value that indicates a certificate to use with PKINIT/PKU2U.
- [var kGSSCredentialUsage: String](kgsscredentialusage.md)
  The value indicates how to use the credential.
- [var kGSSICVerifyCredential: String](kgssicverifycredential.md)
  The value indicates whether to validate the credential with a trusted source to ensure there was no machine-in-the-middle attack.
- [var kGSSICLKDCHostname: String](kgssiclkdchostname.md)
  The value is a string indicating the LKDC hostname.
- [var kGSSICKerberosCacheName: String](kgssickerberoscachename.md)
  The value is a string indicating the name of the cache created for use with the Kerberos mechanism.
- [var kGSSICSiteName: String](kgssicsitename.md)
  The value is a string that is the name of site you are authenticating with, used for load balancing in DNS in Kerberos.
- [var kGSSICAppIdentifierACL: String](kgssicappidentifieracl.md)
  The value is an array of strings containing the list of bundle ID prefixes allowed to access this credential.
- [var kGSSICCreateNewCredential: String](kgssiccreatenewcredential.md)
  The value is a Boolean that indicates whether the caller wants to create a new credential and not overwrite a credential with the same name.
- [var kGSSICAppleSourceApp: String](kgssicapplesourceapp.md)
  The value is a dictionary indicating attributes of the app that the credential is for (only applies to AppVPN).
- [var kGSSICVerifyCredentialAcceptorName: String](kgssicverifycredentialacceptorname.md)
  The value is a string indicating the name of the acceptor.
- [var kGSSICAuthenticationContext: String](kgssicauthenticationcontext.md)
  The value indicates whether to allow the authentication UI or a context to pass a pre-evaluated authentication context.
### Pseudo Random Constants
- [var GSS_C_PRF_KEY_FULL: Int32](gss_c_prf_key_full.md)
  This value indicates using the sub-session key by acceptor, initiator, or the ticket’s session key.
- [var GSS_C_PRF_KEY_PARTIAL: Int32](gss_c_prf_key_partial.md)
  This value indicates using the sub-session key the initiator or the ticket’s session key.
### Credential Usage Values
- [var kGSS_C_INITIATE: String](kgss_c_initiate.md)
  The value that indicates a credential may be used to initiate a context.
- [var kGSS_C_ACCEPT: String](kgss_c_accept.md)
  The value that indicates that a credential may be used to accept a context.
- [var kGSS_C_BOTH: String](kgss_c_both.md)
  The value that indicates that a credential may be used to either initiate or accept a context.
### Password Keys
- [var kGSSChangePasswordOldPassword: String](kgsschangepasswordoldpassword.md)
  The value is a string that indicates the old password.
- [var kGSSChangePasswordNewPassword: String](kgsschangepasswordnewpassword.md)
  The value is a string that indicates the new password.
### Credential Masks and Macros
- [var GSS_C_INDEFINITE: UInt](gss_c_indefinite.md)
  The value that indicates the maximum permitted lifetime when used in a time request.
- [var GSS_C_INITIATE: Int32](gss_c_initiate.md)
  The value that indicates a credential that can initiate a security context.
- [var GSS_C_ACCEPT: Int32](gss_c_accept.md)
  The value that indicates a credential that can accept a security context.
- [var GSS_C_BOTH: Int32](gss_c_both.md)
  The value that indicates a credential that can both initiate and accept security contexts.
- [var GSS_C_OPTION_MASK: Int32](gss_c_option_mask.md)
  The masking constant for options.
- [var GSS_C_CRED_NO_UI: Int32](gss_c_cred_no_ui.md)
  The value that indicates no UI.
- [typealias gss_auth_identity_t](gss_auth_identity_t.md)
  A pointer to an opaque object used to manage authentication identities.
- [typealias gss_const_cred_id_t](gss_const_cred_id_t.md)
  A pointer to an immutable opaque type that you use to exchange a credential object with GSS-API functions.
- [typealias gss_cred_id_t](gss_cred_id_t.md)
  A pointer to an opaque type that you use to exchange a credential object with GSS-API functions.
- [typealias gss_cred_usage_t](gss_cred_usage_t.md)
  A credential usage value.
### Acquisition
- [func gss_aapl_initial_cred(gss_name_t, gss_const_OID, CFDictionary?, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](gss_aapl_initial_cred(_:_:_:_:_:).md)
  Acquires a new credential using a password or certificate.
- [func gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t?, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred(_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context.
- [func gss_acquire_cred_with_password(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, OM_uint32, gss_OID_set?, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t?>, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_acquire_cred_with_password(_:_:_:_:_:_:_:_:_:).md)
  Acquires a credential for use in establishing a security context using a password.
- [func GSSCredentialCopyUUID(gss_cred_id_t) -> Unmanaged<CFUUID>?](gsscredentialcopyuuid(_:).md)
  Returns a copy of the universally unique identifier corresponding to a GSS credential.
- [func GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t?](gsscredentialcopyname(_:).md)
  Returns the name describing the credential.
- [func gss_pseudo_random(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, Int, gss_buffer_t) -> OM_uint32](gss_pseudo_random(_:_:_:_:_:_:).md)
  Returns a pseudo-random byte stream for keying.
### Inquiries
- [func gss_inquire_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_cred(_:_:_:_:_:_:).md)
  Obtains information about a credential.
- [func gss_inquire_cred_by_mech(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, gss_OID, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_usage_t>?) -> OM_uint32](gss_inquire_cred_by_mech(_:_:_:_:_:_:_:).md)
  Obtains per-mechanism information about a credential.
- [func gss_inquire_cred_by_oid(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t?>) -> OM_uint32](gss_inquire_cred_by_oid(_:_:_:_:).md)
  Inquires about a particular characteristic of a credential.
- [func GSSCredentialGetLifetime(gss_cred_id_t) -> OM_uint32](gsscredentialgetlifetime(_:).md)
  Returns the remaining time in seconds before the credential expires.
### Iteration
- [func gss_iter_creds(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID?, (gss_OID?, gss_cred_id_t?) -> Void) -> OM_uint32](gss_iter_creds(_:_:_:_:).md)
  Iterates over all credentials.
- [func gss_iter_creds_f(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID?, UnsafeMutableRawPointer?, (UnsafeMutableRawPointer?, gss_OID?, gss_cred_id_t?) -> Void) -> OM_uint32](gss_iter_creds_f(_:_:_:_:_:).md)
  Iterates over all credentials with a user context.
### Import and Export
- [func gss_import_cred(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_import_cred(_:_:_:).md)
  Imports a credential from a token.
- [func gss_export_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_buffer_t) -> OM_uint32](gss_export_cred(_:_:_:).md)
  Exports a credential to a token.

## See Also

- [Security Mechanisms](security-mechanisms.md)
  Provide a security mechanism for your implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/credential-management)*