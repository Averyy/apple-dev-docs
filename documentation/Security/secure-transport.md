# Secure Transport

**Framework**: Security

Secure network communication using standardized transport layer security mechanisms.

#### Overview

The `Security.SecureTransport` API gives you access to Apple’s implementation of Secure Sockets Layer version 3.0 (SSLv3), Transport Layer Security (TLS) versions 1.0 through 1.2, and Datagram Transport Layer Security (DTLS) version 1.0.

This API imposes no transport layer dependencies. You can use it with BSD Sockets and other protocols. To use this API, you provide callback functions to perform I/O on the underlying network connections. You are also responsible for setting up raw network connections. You pass in an opaque reference to the underlying (connected) entity at the start of an SSL session in the form of an [`SSLConnectionRef`](sslconnectionref.md) object.

> ❗ **Important**:  This API is considered legacy. Use the [`Network`](https://developer.apple.com/documentation/Network) framework instead.

 This API is considered legacy. Use the [`Network`](https://developer.apple.com/documentation/Network) framework instead.

## Topics

### First Steps
- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)
  Establish Secure Sockets Layer (SSL) sessions to facilitate secure communication between client and server.
### Session Context
- [func SSLCreateContext(CFAllocator?, SSLProtocolSide, SSLConnectionType) -> SSLContext?](sslcreatecontext(_:_:_:).md)
  Allocates and returns a new context.
- [enum SSLProtocolSide](sslprotocolside.md)
  The flags that indicate whether a context is for the server or client side of a connection.
- [enum SSLConnectionType](sslconnectiontype.md)
  The flags that indicate whether a context is to be used for streaming or datagram-based communication.
- [class SSLContext](sslcontext.md)
  An opaque type that represents an SSL session context object.
- [func SSLContextGetTypeID() -> CFTypeID](sslcontextgettypeid().md)
  Returns the Core Foundation type ID for context objects.
### Context Options
- [func SSLSetSessionOption(SSLContext, SSLSessionOption, Bool) -> OSStatus](sslsetsessionoption(_:_:_:).md)
  Specifies options for a specific session.
- [func SSLGetSessionOption(SSLContext, SSLSessionOption, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](sslgetsessionoption(_:_:_:).md)
  Indicates the current setting of Secure Sockets Layer (SSL) session options.
- [enum SSLSessionOption](sslsessionoption.md)
  The options that can be set for an SSL session.
### Context Callbacks
- [func SSLSetIOFuncs(SSLContext, SSLReadFunc, SSLWriteFunc) -> OSStatus](sslsetiofuncs(_:_:_:).md)
  Specifies callback functions that perform the network I/O operations.
- [typealias SSLReadFunc](sslreadfunc.md)
  A pointer to a customized read function that secure transport calls to read data from the connection.
- [typealias SSLWriteFunc](sslwritefunc.md)
  A pointer to a customized write function that secure transport calls to write data to the connection.
### Session Configuration
- [func SSLSetSessionConfig(SSLContext, CFString) -> OSStatus](sslsetsessionconfig(_:_:).md)
  Sets a predefined configuration for the Secure Sockets Layer (SSL) session.
- [func SSLSetClientSideAuthenticate(SSLContext, SSLAuthenticate) -> OSStatus](sslsetclientsideauthenticate(_:_:).md)
  Specifies the requirements for client-side authentication.
- [SSLConfig](sslconfig.md)
  Use these constants to configure Transport Layer Security (TLS) sessions.
- [enum SSLAuthenticate](sslauthenticate.md)
  The flags that represent the requirements for client-side authentication.
### I/O Connections
- [func SSLSetConnection(SSLContext, SSLConnectionRef?) -> OSStatus](sslsetconnection(_:_:).md)
  Specifies an I/O connection for a specific session.
- [func SSLGetConnection(SSLContext, UnsafeMutablePointer<SSLConnectionRef?>) -> OSStatus](sslgetconnection(_:_:).md)
  Retrieves an I/O connection—such as a socket or endpoint—for a specific session.
- [typealias SSLConnectionRef](sslconnectionref.md)
  A pointer to an opaque I/O connection object.
### Session State
- [func SSLHandshake(SSLContext) -> OSStatus](sslhandshake(_:).md)
  Performs the SSL handshake.
- [func SSLReHandshake(SSLContext) -> OSStatus](sslrehandshake(_:).md)
  Requests renegotiation of the SSL handshake. Server only.
- [func SSLClose(SSLContext) -> OSStatus](sslclose(_:).md)
  Terminates the current SSL session.
- [func SSLSetPeerID(SSLContext, UnsafeRawPointer?, Int) -> OSStatus](sslsetpeerid(_:_:_:).md)
  Specifies data that is sufficient to uniquely identify the peer of the current session.
- [func SSLGetPeerID(SSLContext, UnsafeMutablePointer<UnsafeRawPointer?>, UnsafeMutablePointer<Int>) -> OSStatus](sslgetpeerid(_:_:_:).md)
  Retrieves the current peer ID data.
- [func SSLGetSessionState(SSLContext, UnsafeMutablePointer<SSLSessionState>) -> OSStatus](sslgetsessionstate(_:_:).md)
  Retrieves the state of an SSL session.
- [enum SSLSessionState](sslsessionstate.md)
  The flags that represent the state of an SSL session.
- [func SSLSetError(SSLContext, OSStatus) -> OSStatus](sslseterror(_:_:).md)
  Sets the status of a session context.
### Read Operations
- [func SSLRead(SSLContext, UnsafeMutableRawPointer, Int, UnsafeMutablePointer<Int>) -> OSStatus](sslread(_:_:_:_:).md)
  Performs a normal application-level read operation.
- [func SSLGetBufferedReadSize(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslgetbufferedreadsize(_:_:).md)
  Determines how much data is available to be read.
### Write Operations
- [func SSLWrite(SSLContext, UnsafeRawPointer?, Int, UnsafeMutablePointer<Int>) -> OSStatus](sslwrite(_:_:_:_:).md)
  Performs a typical application-level write operation.
- [func SSLGetDatagramWriteSize(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslgetdatagramwritesize(_:_:).md)
  Provides the largest packet that the OS guarantees it can send without fragmentation.
- [func SSLGetMaxDatagramRecordSize(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslgetmaxdatagramrecordsize(_:_:).md)
  Obtains the maximum datagram record size allowed by the application for a given context.
- [func SSLSetMaxDatagramRecordSize(SSLContext, Int) -> OSStatus](sslsetmaxdatagramrecordsize(_:_:).md)
  Sets the maximum datagram record size allowed by the application for a given context.
- [func SSLSetDatagramHelloCookie(SSLContext, UnsafeRawPointer?, Int) -> OSStatus](sslsetdatagramhellocookie(_:_:_:).md)
  Sets the cookie value used in the Datagram Transport Layer Security (DTLS) hello message.
### The Peer Domain Name
- [func SSLSetPeerDomainName(SSLContext, UnsafePointer<CChar>?, Int) -> OSStatus](sslsetpeerdomainname(_:_:_:).md)
  Specifies the fully qualified domain name of the peer.
- [func SSLGetPeerDomainNameLength(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslgetpeerdomainnamelength(_:_:).md)
  Determines the length of a previously set peer domain name.
- [func SSLGetPeerDomainName(SSLContext, UnsafeMutablePointer<CChar>, UnsafeMutablePointer<Int>) -> OSStatus](sslgetpeerdomainname(_:_:_:).md)
  Retrieves the peer domain name specified previously.
- [func SSLCopyRequestedPeerName(SSLContext, UnsafeMutablePointer<CChar>, UnsafeMutablePointer<Int>) -> OSStatus](sslcopyrequestedpeername(_:_:_:).md)
  Determines the buffer size needed for the peer domain name.
- [func SSLCopyRequestedPeerNameLength(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslcopyrequestedpeernamelength(_:_:).md)
  Obtains the hostname specified by the client in the ServerName extension (SNI). Server only.
### Versions
- [func SSLSetProtocolVersionMax(SSLContext, SSLProtocol) -> OSStatus](sslsetprotocolversionmax(_:_:).md)
  Sets the maximum protocol version allowed by the application for a given SSL context.
- [func SSLSetProtocolVersionMin(SSLContext, SSLProtocol) -> OSStatus](sslsetprotocolversionmin(_:_:).md)
  Sets the minimum protocol version allowed by the application for a given SSL context.
- [func SSLGetProtocolVersionMax(SSLContext, UnsafeMutablePointer<SSLProtocol>) -> OSStatus](sslgetprotocolversionmax(_:_:).md)
  Gets the maximum protocol version allowed by the application for a given SSL context.
- [func SSLGetProtocolVersionMin(SSLContext, UnsafeMutablePointer<SSLProtocol>) -> OSStatus](sslgetprotocolversionmin(_:_:).md)
  Gets the minimum protocol version allowed by the application for a given SSL context.
- [func SSLGetNegotiatedProtocolVersion(SSLContext, UnsafeMutablePointer<SSLProtocol>) -> OSStatus](sslgetnegotiatedprotocolversion(_:_:).md)
  Obtains the negotiated protocol version of the active session.
- [enum tls_protocol_version_t](tls_protocol_version_t.md)
  The collection of supported TLS and DTLS versions.
- [enum SSLProtocol](sslprotocol.md)
  An enumeration of valid SSL protocol versions.
### Application Layer Protocols
- [func SSLCopyALPNProtocols(SSLContext, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](sslcopyalpnprotocols(_:_:).md)
  Gets the list of supported application layer protocols.
- [func SSLSetALPNProtocols(SSLContext, CFArray) -> OSStatus](sslsetalpnprotocols(_:_:).md)
  Sets the list of supported applicaiton layer protocols.
### Ciphers
- [func SSLGetNumberSupportedCiphers(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslgetnumbersupportedciphers(_:_:).md)
  Determines the number of cipher suites supported.
- [func SSLGetSupportedCiphers(SSLContext, UnsafeMutablePointer<SSLCipherSuite>, UnsafeMutablePointer<Int>) -> OSStatus](sslgetsupportedciphers(_:_:_:).md)
  Determines the values of the supported cipher suites.
- [func SSLSetEnabledCiphers(SSLContext, UnsafePointer<SSLCipherSuite>, Int) -> OSStatus](sslsetenabledciphers(_:_:_:).md)
  Specifies a restricted set of SSL cipher suites to be enabled by the current SSL session context.
- [func SSLGetNumberEnabledCiphers(SSLContext, UnsafeMutablePointer<Int>) -> OSStatus](sslgetnumberenabledciphers(_:_:).md)
  Determines the number of cipher suites currently enabled.
- [func SSLGetEnabledCiphers(SSLContext, UnsafeMutablePointer<SSLCipherSuite>, UnsafeMutablePointer<Int>) -> OSStatus](sslgetenabledciphers(_:_:_:).md)
  Determines which SSL cipher suites are currently enabled.
- [func SSLGetNegotiatedCipher(SSLContext, UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus](sslgetnegotiatedcipher(_:_:).md)
  Retrieves the cipher suite negotiated for this session.
- [func SSLSetDiffieHellmanParams(SSLContext, UnsafeRawPointer?, Int) -> OSStatus](sslsetdiffiehellmanparams(_:_:_:).md)
  Specifies Diffie-Hellman parameters for a given context.
- [func SSLGetDiffieHellmanParams(SSLContext, UnsafeMutablePointer<UnsafeRawPointer?>, UnsafeMutablePointer<Int>) -> OSStatus](sslgetdiffiehellmanparams(_:_:_:).md)
  Retrieves the Diffie-Hellman parameters for a given context.
- [enum tls_ciphersuite_group_t](tls_ciphersuite_group_t.md)
  Groups that collect ciphersuites of comparable security properties.
- [enum tls_ciphersuite_t](tls_ciphersuite_t.md)
  The collection of valid ciphersuites.
- [typealias SSLCipherSuite](sslciphersuite.md)
  A type for storing cipher suite values.
- [enum SSLCiphersuiteGroup](sslciphersuitegroup.md)
  A mechanism for grouping related cipher suites.
- [SSL Cipher Suite Values](ssl-cipher-suite-values.md)
  Recognize the set of valid SSL cipher suite values.
### Root Certificates
- [func SSLSetCertificateAuthorities(SSLContext, CFTypeRef, Bool) -> OSStatus](sslsetcertificateauthorities(_:_:_:).md)
  Adds one or more certificates to a server’s list of certification authorities (CAs) acceptable for client authentication.
- [func SSLCopyCertificateAuthorities(SSLContext, UnsafeMutablePointer<CFArray?>) -> OSStatus](sslcopycertificateauthorities(_:_:).md)
  Retrieves the current list of certification authorities.
### Authentication
- [func SSLAddDistinguishedName(SSLContext, UnsafeRawPointer?, Int) -> OSStatus](ssladddistinguishedname(_:_:_:).md)
  Adds a DER-encoded distinguished name to a list of acceptable names to be specified in requests for client certificates.
- [func SSLCopyDistinguishedNames(SSLContext, UnsafeMutablePointer<CFArray?>) -> OSStatus](sslcopydistinguishednames(_:_:).md)
  Retrieves the distinguished names of acceptable certification authorities.
- [func SSLSetCertificate(SSLContext, CFArray?) -> OSStatus](sslsetcertificate(_:_:).md)
  Specifies this connection’s certificate or certificates.
- [func SSLGetClientCertificateState(SSLContext, UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus](sslgetclientcertificatestate(_:_:).md)
  Retrieves the exchange status of the client certificate.
- [func SSLCopyPeerTrust(SSLContext, UnsafeMutablePointer<SecTrust?>) -> OSStatus](sslcopypeertrust(_:_:).md)
  Retrieves a trust management object for the certificate used by a session.
- [enum SSLClientCertificateState](sslclientcertificatestate.md)
  An enumeration of the states of client certificate exchange.
- [func SSLSetOCSPResponse(SSLContext, CFData) -> OSStatus](sslsetocspresponse(_:_:).md)
  Sets the OCSP response for the given SSL session.
- [func SSLSetSessionTicketsEnabled(SSLContext, Bool) -> OSStatus](sslsetsessionticketsenabled(_:_:).md)
  Enables or disables session ticket resumption.
### Result Codes
- [Secure Transport Result Codes](secure-transport-result-codes.md)
  Recognize result codes specific to the secure transport API.
### Legacy Operations
- [func SSLSetEncryptionCertificate(SSLContext, CFArray) -> OSStatus](sslsetencryptioncertificate(_:_:).md)
  Specifies the encryption certificates used for this connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secure-transport)*