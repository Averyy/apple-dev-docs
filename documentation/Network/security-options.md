# Security Options

**Framework**: Network

Configure security options for TLS handshakes.

## Topics

### Configuring TLS Handshake Options
- [typealias sec_protocol_options_t](../Security/sec_protocol_options_t.md)
  A `sec_protocol_options` instance is a container of options for security protocol instances, such as TLS. Protocol options are used to configure security protocols in the network stack. For example, clients may set the maximum and minimum allowed TLS versions through protocol options.
- [protocol OS_sec_protocol_options](../Security/os_sec_protocol_options.md)
  A `sec_protocol_options` instance is a container of options for security protocol instances, such as TLS. Protocol options are used to configure security protocols in the network stack. For example, clients may set the maximum and minimum allowed TLS versions through protocol options.
- [func sec_protocol_options_set_tls_server_name(sec_protocol_options_t, UnsafePointer<CChar>)](../Security/sec_protocol_options_set_tls_server_name%28_,_%29.md)
- [func sec_protocol_options_add_pre_shared_key(sec_protocol_options_t, dispatch_data_t, dispatch_data_t)](../Security/sec_protocol_options_add_pre_shared_key%28_,_,_%29.md)
- [func sec_protocol_options_add_tls_application_protocol(sec_protocol_options_t, UnsafePointer<CChar>)](../Security/sec_protocol_options_add_tls_application_protocol%28_,_%29.md)
- [func sec_protocol_options_append_tls_ciphersuite(sec_protocol_options_t, tls_ciphersuite_t)](../Security/sec_protocol_options_append_tls_ciphersuite%28_,_%29.md)
- [func sec_protocol_options_append_tls_ciphersuite_group(sec_protocol_options_t, tls_ciphersuite_group_t)](../Security/sec_protocol_options_append_tls_ciphersuite_group%28_,_%29.md)
- [func sec_protocol_options_add_tls_ciphersuite(sec_protocol_options_t, SSLCipherSuite)](../Security/sec_protocol_options_add_tls_ciphersuite%28_,_%29.md)
- [func sec_protocol_options_add_tls_ciphersuite_group(sec_protocol_options_t, SSLCiphersuiteGroup)](../Security/sec_protocol_options_add_tls_ciphersuite_group%28_,_%29.md)
- [func sec_protocol_options_set_tls_diffie_hellman_parameters(sec_protocol_options_t, dispatch_data_t)](../Security/sec_protocol_options_set_tls_diffie_hellman_parameters%28_,_%29.md)
- [func sec_protocol_options_are_equal(sec_protocol_options_t, sec_protocol_options_t) -> Bool](../Security/sec_protocol_options_are_equal%28_,_%29.md)
### Configuring TLS Versions
- [func sec_protocol_options_set_min_tls_protocol_version(sec_protocol_options_t, tls_protocol_version_t)](../Security/sec_protocol_options_set_min_tls_protocol_version%28_,_%29.md)
- [func sec_protocol_options_set_max_tls_protocol_version(sec_protocol_options_t, tls_protocol_version_t)](../Security/sec_protocol_options_set_max_tls_protocol_version%28_,_%29.md)
- [func sec_protocol_options_get_default_min_tls_protocol_version() -> tls_protocol_version_t](../Security/sec_protocol_options_get_default_min_tls_protocol_version%28%29.md)
- [func sec_protocol_options_get_default_max_tls_protocol_version() -> tls_protocol_version_t](../Security/sec_protocol_options_get_default_max_tls_protocol_version%28%29.md)
- [func sec_protocol_options_get_default_min_dtls_protocol_version() -> tls_protocol_version_t](../Security/sec_protocol_options_get_default_min_dtls_protocol_version%28%29.md)
- [func sec_protocol_options_get_default_max_dtls_protocol_version() -> tls_protocol_version_t](../Security/sec_protocol_options_get_default_max_dtls_protocol_version%28%29.md)
- [func sec_protocol_options_set_tls_min_version(sec_protocol_options_t, SSLProtocol)](../Security/sec_protocol_options_set_tls_min_version%28_,_%29.md)
- [func sec_protocol_options_set_tls_max_version(sec_protocol_options_t, SSLProtocol)](../Security/sec_protocol_options_set_tls_max_version%28_,_%29.md)
### Configuring TLS Behavior
- [func sec_protocol_options_set_tls_resumption_enabled(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_resumption_enabled%28_,_%29.md)
- [func sec_protocol_options_set_tls_tickets_enabled(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_tickets_enabled%28_,_%29.md)
- [func sec_protocol_options_set_tls_false_start_enabled(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_false_start_enabled%28_,_%29.md)
- [func sec_protocol_options_set_tls_sct_enabled(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_sct_enabled%28_,_%29.md)
- [func sec_protocol_options_set_tls_ocsp_enabled(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_ocsp_enabled%28_,_%29.md)
- [func sec_protocol_options_set_tls_renegotiation_enabled(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_renegotiation_enabled%28_,_%29.md)
- [func sec_protocol_options_set_peer_authentication_required(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_peer_authentication_required%28_,_%29.md)
- [func sec_protocol_options_set_tls_is_fallback_attempt(sec_protocol_options_t, Bool)](../Security/sec_protocol_options_set_tls_is_fallback_attempt%28_,_%29.md)
- [func sec_protocol_options_set_tls_pre_shared_key_identity_hint(sec_protocol_options_t, dispatch_data_t)](../Security/sec_protocol_options_set_tls_pre_shared_key_identity_hint%28_,_%29.md)
### Handling TLS Events
- [func sec_protocol_options_set_verify_block(sec_protocol_options_t, sec_protocol_verify_t, dispatch_queue_t)](../Security/sec_protocol_options_set_verify_block%28_,_,_%29.md)
- [typealias sec_protocol_verify_t](../Security/sec_protocol_verify_t.md)
- [typealias sec_protocol_verify_complete_t](../Security/sec_protocol_verify_complete_t.md)
- [func sec_protocol_options_set_challenge_block(sec_protocol_options_t, sec_protocol_challenge_t, dispatch_queue_t)](../Security/sec_protocol_options_set_challenge_block%28_,_,_%29.md)
- [typealias sec_protocol_challenge_t](../Security/sec_protocol_challenge_t.md)
- [typealias sec_protocol_challenge_complete_t](../Security/sec_protocol_challenge_complete_t.md)
- [func sec_protocol_options_set_key_update_block(sec_protocol_options_t, sec_protocol_key_update_t, dispatch_queue_t)](../Security/sec_protocol_options_set_key_update_block%28_,_,_%29.md)
- [typealias sec_protocol_key_update_t](../Security/sec_protocol_key_update_t.md)
- [typealias sec_protocol_key_update_complete_t](../Security/sec_protocol_key_update_complete_t.md)
- [func sec_protocol_options_set_pre_shared_key_selection_block(sec_protocol_options_t, sec_protocol_pre_shared_key_selection_t, dispatch_queue_t)](../Security/sec_protocol_options_set_pre_shared_key_selection_block%28_,_,_%29.md)
- [typealias sec_protocol_pre_shared_key_selection_t](../Security/sec_protocol_pre_shared_key_selection_t.md)
- [typealias sec_protocol_pre_shared_key_selection_complete_t](../Security/sec_protocol_pre_shared_key_selection_complete_t.md)
### Inspecting TLS State
- [typealias sec_protocol_metadata_t](../Security/sec_protocol_metadata_t.md)
  A `sec_protocol_metadata` instance conatins read-only properties of a connected and configured security protocol. Clients use this object to read information about a protocol instance. Properties include, for example, the negotiated TLS version, ciphersuite, and peer certificates.
- [protocol OS_sec_protocol_metadata](../Security/os_sec_protocol_metadata.md)
  A `sec_protocol_metadata` instance conatins read-only properties of a connected and configured security protocol. Clients use this object to read information about a protocol instance. Properties include, for example, the negotiated TLS version, ciphersuite, and peer certificates.
- [func sec_protocol_metadata_get_negotiated_protocol(sec_protocol_metadata_t) -> UnsafePointer<CChar>?](../Security/sec_protocol_metadata_get_negotiated_protocol%28_%29.md)
- [func sec_protocol_metadata_get_server_name(sec_protocol_metadata_t) -> UnsafePointer<CChar>?](../Security/sec_protocol_metadata_get_server_name%28_%29.md)
- [func sec_protocol_metadata_get_negotiated_tls_protocol_version(sec_protocol_metadata_t) -> tls_protocol_version_t](../Security/sec_protocol_metadata_get_negotiated_tls_protocol_version%28_%29.md)
- [func sec_protocol_metadata_get_negotiated_tls_ciphersuite(sec_protocol_metadata_t) -> tls_ciphersuite_t](../Security/sec_protocol_metadata_get_negotiated_tls_ciphersuite%28_%29.md)
- [func sec_protocol_metadata_get_negotiated_protocol_version(sec_protocol_metadata_t) -> SSLProtocol](../Security/sec_protocol_metadata_get_negotiated_protocol_version%28_%29.md)
- [func sec_protocol_metadata_get_negotiated_ciphersuite(sec_protocol_metadata_t) -> SSLCipherSuite](../Security/sec_protocol_metadata_get_negotiated_ciphersuite%28_%29.md)
- [func sec_protocol_metadata_get_early_data_accepted(sec_protocol_metadata_t) -> Bool](../Security/sec_protocol_metadata_get_early_data_accepted%28_%29.md)
- [func sec_protocol_metadata_copy_peer_public_key(sec_protocol_metadata_t) -> dispatch_data_t?](../Security/sec_protocol_metadata_copy_peer_public_key%28_%29.md)
### Handling TLS Challenges
- [func sec_protocol_metadata_access_distinguished_names(sec_protocol_metadata_t, (dispatch_data_t) -> Void) -> Bool](../Security/sec_protocol_metadata_access_distinguished_names%28_,_%29.md)
- [func sec_protocol_metadata_access_ocsp_response(sec_protocol_metadata_t, (dispatch_data_t) -> Void) -> Bool](../Security/sec_protocol_metadata_access_ocsp_response%28_,_%29.md)
- [func sec_protocol_metadata_access_peer_certificate_chain(sec_protocol_metadata_t, (sec_certificate_t) -> Void) -> Bool](../Security/sec_protocol_metadata_access_peer_certificate_chain%28_,_%29.md)
- [func sec_protocol_metadata_access_supported_signature_algorithms(sec_protocol_metadata_t, (UInt16) -> Void) -> Bool](../Security/sec_protocol_metadata_access_supported_signature_algorithms%28_,_%29.md)
- [func sec_protocol_metadata_access_pre_shared_keys(sec_protocol_metadata_t, (dispatch_data_t, dispatch_data_t) -> Void) -> Bool](../Security/sec_protocol_metadata_access_pre_shared_keys%28_,_%29.md)
- [func sec_protocol_metadata_create_secret(sec_protocol_metadata_t, Int, UnsafePointer<CChar>, Int) -> dispatch_data_t?](../Security/sec_protocol_metadata_create_secret%28_,_,_,_%29.md)
- [func sec_protocol_metadata_create_secret_with_context(sec_protocol_metadata_t, Int, UnsafePointer<CChar>, Int, UnsafePointer<UInt8>, Int) -> dispatch_data_t?](../Security/sec_protocol_metadata_create_secret_with_context%28_,_,_,_,_,_%29.md)
- [func sec_protocol_metadata_peers_are_equal(sec_protocol_metadata_t, sec_protocol_metadata_t) -> Bool](../Security/sec_protocol_metadata_peers_are_equal%28_,_%29.md)
- [func sec_protocol_metadata_challenge_parameters_are_equal(sec_protocol_metadata_t, sec_protocol_metadata_t) -> Bool](../Security/sec_protocol_metadata_challenge_parameters_are_equal%28_,_%29.md)
### Handling Certificates
- [typealias sec_certificate_t](../Security/sec_certificate_t.md)
- [protocol OS_sec_certificate](../Security/os_sec_certificate.md)
- [func sec_certificate_create(SecCertificate) -> sec_certificate_t?](../Security/sec_certificate_create%28_%29.md)
- [func sec_certificate_copy_ref(sec_certificate_t) -> Unmanaged<SecCertificate>](../Security/sec_certificate_copy_ref%28_%29.md)
### Handling Identities
- [func sec_protocol_options_set_local_identity(sec_protocol_options_t, sec_identity_t)](../Security/sec_protocol_options_set_local_identity%28_,_%29.md)
- [typealias sec_identity_t](../Security/sec_identity_t.md)
- [protocol OS_sec_identity](../Security/os_sec_identity.md)
- [func sec_identity_create(SecIdentity) -> sec_identity_t?](../Security/sec_identity_create%28_%29.md)
- [func sec_identity_create_with_certificates(SecIdentity, CFArray) -> sec_identity_t?](../Security/sec_identity_create_with_certificates%28_,_%29.md)
- [func sec_identity_copy_ref(sec_identity_t) -> Unmanaged<SecIdentity>?](../Security/sec_identity_copy_ref%28_%29.md)
- [func sec_identity_access_certificates(sec_identity_t, (sec_certificate_t) -> Void) -> Bool](../Security/sec_identity_access_certificates%28_,_%29.md)
- [func sec_identity_copy_certificates_ref(sec_identity_t) -> Unmanaged<CFArray>?](../Security/sec_identity_copy_certificates_ref%28_%29.md)
### Handling Trust
- [typealias sec_trust_t](../Security/sec_trust_t.md)
  These are os_object compatible and ARC-able wrappers around existing CoreFoundation Security types, including: SecTrustRef, SecIdentityRef, and SecCertificateRef. They allow clients to use these types in os_object-type APIs and data structures. The underlying CoreFoundation types may be extracted and used by clients as needed.
- [protocol OS_sec_trust](../Security/os_sec_trust.md)
  These are os_object compatible and ARC-able wrappers around existing CoreFoundation Security types, including: SecTrustRef, SecIdentityRef, and SecCertificateRef. They allow clients to use these types in os_object-type APIs and data structures. The underlying CoreFoundation types may be extracted and used by clients as needed.
- [func sec_trust_create(SecTrust) -> sec_trust_t?](../Security/sec_trust_create%28_%29.md)
- [func sec_trust_copy_ref(sec_trust_t) -> Unmanaged<SecTrust>](../Security/sec_trust_copy_ref%28_%29.md)
### Managing Security Objects
- [func sec_release(UnsafeMutableRawPointer!)](../Security/sec_release%28_%29.md)
- [func sec_retain(UnsafeMutableRawPointer!) -> UnsafeMutableRawPointer!](../Security/sec_retain%28_%29.md)
- [typealias sec_object_t](../Security/sec_object_t.md)
  A `sec_object` is a generic, ARC-able type wrapper for common CoreFoundation Security types.
- [protocol OS_sec_object](../Security/os_sec_object.md)
  A `sec_object` is a generic, ARC-able type wrapper for common CoreFoundation Security types.

## See Also

### Network Security and Privacy
- [Privacy Management](./privacy-management.md)
  Configure parameters related to user privacy.
- [Creating an Identity for Local Network TLS](./creating-an-identity-for-local-network-tls.md)
  Learn how to create and use a digital identity in your application for local network TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/security-options)*