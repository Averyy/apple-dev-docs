# Secure Transport Result Codes

**Framework**: Security

Recognize result codes specific to the secure transport API.

#### Discussion

Use the [`SecCopyErrorMessageString(_:_:)`](seccopyerrormessagestring(_:_:).md) function to obtain a human readable string corresponding to these status codes.

The functions of the [`Secure Transport`](secure-transport.md) API may also return the general codes listed in [`Security Framework Result Codes`](security-framework-result-codes.md).

Errors in the range of –9819 through –9840 are fatal errors that are detected by the peer.

## Topics

### App Transport Security result codes
- [var errSSLATSViolation: OSStatus](errsslatsviolation.md)
  An App Transport Security violation occurred.
- [var errSSLATSMinimumVersionViolation: OSStatus](errsslatsminimumversionviolation.md)
  The minimum protocol version isn’t App Transport Security compliant.
- [var errSSLATSCiphersuiteViolation: OSStatus](errsslatsciphersuiteviolation.md)
  The selected ciphersuite isn’t App Transport Security compliant.
- [var errSSLATSMinimumKeySizeViolation: OSStatus](errsslatsminimumkeysizeviolation.md)
  The peer key size isn’t App Transport Security compliant.
- [var errSSLATSLeafCertificateHashAlgorithmViolation: OSStatus](errsslatsleafcertificatehashalgorithmviolation.md)
  The peer leaf certificate hash algorithm isn’t App Transport Security compliant.
- [var errSSLATSCertificateHashAlgorithmViolation: OSStatus](errsslatscertificatehashalgorithmviolation.md)
  The peer certificate hash algorithm isn’t App Transport Security compliant.
- [var errSSLATSCertificateTrustViolation: OSStatus](errsslatscertificatetrustviolation.md)
  The peer certificate wasn’t issued by a trusted peer.
### Certificate issue result codes
- [var errSSLBadCert: OSStatus](errsslbadcert.md)
  Bad certificate format.
- [var errSSLBadCertificateStatusResponse: OSStatus](errsslbadcertificatestatusresponse.md)
  Bad OCSP response.
- [var errSSLCertExpired: OSStatus](errsslcertexpired.md)
  The certificate chain had an expired certificate.
- [var errSSLCertNotYetValid: OSStatus](errsslcertnotyetvalid.md)
  The certificate chain had a certificatethat is not yet valid.
- [var errSSLCertificateRequired: OSStatus](errsslcertificaterequired.md)
  Certificate required.
- [var errSSLClientCertRequested: OSStatus](errsslclientcertrequested.md)
  The server has requested a client certificate.
- [var errSSLHostNameMismatch: OSStatus](errsslhostnamemismatch.md)
  The host name you connected with does not match any of the host names allowed by the certificate.
- [var errSSLNoRootCert: OSStatus](errsslnorootcert.md)
  No root certificate for the certificate chain.
- [var errSSLPeerBadCert: OSStatus](errsslpeerbadcert.md)
  A bad certificate was encountered.
- [var errSSLPeerCertExpired: OSStatus](errsslpeercertexpired.md)
  The certificate expired.
- [var errSSLPeerCertRevoked: OSStatus](errsslpeercertrevoked.md)
  The certificate was revoked.
- [var errSSLPeerCertUnknown: OSStatus](errsslpeercertunknown.md)
  The certificate is unknown.
- [var errSSLPeerUnsupportedCert: OSStatus](errsslpeerunsupportedcert.md)
  An unsupported certificate format was encountered.
- [var errSSLUnknownRootCert: OSStatus](errsslunknownrootcert.md)
  Certificate chain is valid, but root is nottrusted.
- [var errSSLXCertChainInvalid: OSStatus](errsslxcertchaininvalid.md)
  Invalid certificate chain.
- [var errSSLPeerUnknownCA: OSStatus](errsslpeerunknownca.md)
  An unknown certificate authority was encountered.
### Connection status result codes
- [var errSSLClientHelloReceived: OSStatus](errsslclienthelloreceived.md)
  A non-fatal result for providing a server name indication.
- [var errSSLClosedAbort: OSStatus](errsslclosedabort.md)
  The connection closed due to an error.
- [var errSSLClosedGraceful: OSStatus](errsslclosedgraceful.md)
  The connection closed gracefully.
- [var errSSLClosedNoNotify: OSStatus](errsslclosednonotify.md)
  The server closed the session with no notification.
- [var errSSLConnectionRefused: OSStatus](errsslconnectionrefused.md)
  The peer dropped the connection before responding.
- [var errSSLPeerAuthCompleted: OSStatus](errsslpeerauthcompleted.md)
  A non-fatal result indicating the peer certificate is valid, or was ignored if verification is disabled.
- [var errSSLWouldBlock: OSStatus](errsslwouldblock.md)
  Function is blocked; waiting for I/O. This is not fatal.
### Cryptography result codes
- [var errSSLCrypto: OSStatus](errsslcrypto.md)
  An underlying cryptographic error was encountered.
- [var errSSLDecryptionFail: OSStatus](errssldecryptionfail.md)
  Decryption failed.
- [var errSSLPeerDecryptError: OSStatus](errsslpeerdecrypterror.md)
  A decryption error occurred.
- [var errSSLPeerDecryptionFail: OSStatus](errsslpeerdecryptionfail.md)
  Decryption failed.
- [var errSSLWeakPeerEphemeralDHKey: OSStatus](errsslweakpeerephemeraldhkey.md)
  Indicates a weak ephemeral dh key.
### Other result codes
- [var errSSLBadCipherSuite: OSStatus](errsslbadciphersuite.md)
  A bad SSL cipher suite was encountered.
- [var errSSLBadConfiguration: OSStatus](errsslbadconfiguration.md)
  A configuration error occurred.
- [var errSSLBadRecordMac: OSStatus](errsslbadrecordmac.md)
  A record with a bad message authentication code (MAC) was encountered.
- [var errSSLBufferOverflow: OSStatus](errsslbufferoverflow.md)
  An insufficient buffer was provided.
- [var errSSLConfigurationFailed: OSStatus](errsslconfigurationfailed.md)
  TLS configuration failed.
- [var errSSLDecodeError: OSStatus](errssldecodeerror.md)
  Decode failed.
- [var errSSLDecompressFail: OSStatus](errssldecompressfail.md)
  Decompression failed.
- [var errSSLFatalAlert: OSStatus](errsslfatalalert.md)
  A fatal alert was encountered.
- [var errSSLHandshakeFail: OSStatus](errsslhandshakefail.md)
  Handshake failed.
- [var errSSLIllegalParam: OSStatus](errsslillegalparam.md)
  An illegal parameter was encountered.
- [var errSSLInappropriateFallback: OSStatus](errsslinappropriatefallback.md)
  Inappropriate fallback.
- [var errSSLInternal: OSStatus](errsslinternal.md)
  Internal error.
- [var errSSLMissingExtension: OSStatus](errsslmissingextension.md)
  Missing extension.
- [var errSSLModuleAttach: OSStatus](errsslmoduleattach.md)
  Module attach failure.
- [var errSSLNegotiation: OSStatus](errsslnegotiation.md)
  The cipher suite negotiation failed.
- [var errSSLNetworkTimeout: OSStatus](errsslnetworktimeout.md)
  Network timeout triggered.
- [var errSSLPeerAccessDenied: OSStatus](errsslpeeraccessdenied.md)
  Access was denied.
- [var errSSLPeerBadRecordMac: OSStatus](errsslpeerbadrecordmac.md)
  A record with a bad message authentication code (MAC) was encountered.
- [var errSSLPeerDecodeError: OSStatus](errsslpeerdecodeerror.md)
  A decoding error occurred.
- [var errSSLPeerDecompressFail: OSStatus](errsslpeerdecompressfail.md)
  Decompression failed.
- [var errSSLPeerExportRestriction: OSStatus](errsslpeerexportrestriction.md)
  An export restriction occurred.
- [var errSSLPeerHandshakeFail: OSStatus](errsslpeerhandshakefail.md)
  The handshake failed.
- [var errSSLPeerInsufficientSecurity: OSStatus](errsslpeerinsufficientsecurity.md)
  There is insufficient security for this operation.
- [var errSSLPeerInternalError: OSStatus](errsslpeerinternalerror.md)
  An internal error occurred.
- [var errSSLPeerNoRenegotiation: OSStatus](errsslpeernorenegotiation.md)
  No renegotiation is allowed.
- [var errSSLPeerProtocolVersion: OSStatus](errsslpeerprotocolversion.md)
  A bad protocol version was encountered.
- [var errSSLPeerRecordOverflow: OSStatus](errsslpeerrecordoverflow.md)
  A record overflow occurred.
- [var errSSLPeerUnexpectedMsg: OSStatus](errsslpeerunexpectedmsg.md)
  An unexpected message was received.
- [var errSSLPeerUserCancelled: OSStatus](errsslpeerusercancelled.md)
  The user canceled the operation.
- [var errSSLProtocol: OSStatus](errsslprotocol.md)
  SSL protocol error.
- [var errSSLRecordOverflow: OSStatus](errsslrecordoverflow.md)
  A record overflow occurred.
- [var errSSLSessionNotFound: OSStatus](errsslsessionnotfound.md)
  An attempt to restore an unknown session failed.
- [var errSSLTransportReset: OSStatus](errssltransportreset.md)
  Transport (socket) shutdown, for example, TCP RST or FIN.
- [var errSSLUnexpectedMessage: OSStatus](errsslunexpectedmessage.md)
  Peer rejected unexpected message.
- [var errSSLUnexpectedRecord: OSStatus](errsslunexpectedrecord.md)
- [var errSSLUnknownPSKIdentity: OSStatus](errsslunknownpskidentity.md)
  Unknown PSK identity.
- [var errSSLUnrecognizedName: OSStatus](errsslunrecognizedname.md)
  Unknown or unrecognized name.
- [var errSSLUnsupportedExtension: OSStatus](errsslunsupportedextension.md)
  Unsupported TLS extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secure-transport-result-codes)*