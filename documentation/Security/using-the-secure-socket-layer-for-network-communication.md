# Using the Secure Socket Layer for Network Communication

**Framework**: Security  
**Role**: Article

Establish Secure Sockets Layer (SSL) sessions to facilitate secure communication between client and server.

## Overview

The following terms are used in this discussion:

- **Client**: The initiator of an SSL session. The canonical example of a client is a web browser communicating with an HTTPS URL.
- **Server**: An entity that accepts requests for SSL sessions made by clients. An example is a secure web server.
- **SSLSession**: An entity whose existence is bounded by calls to the functions [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) and [`SSLClose(_:)`](./sslclose%28_%29.md). An active session is in some state between these two calls, inclusive.
- **SSLSessionContext**: The state associated with one session. A session context cannot be reused for multiple sessions.

Most applications need only a few of the functions in this API, which are normally called in the following sequence:

- Prepare for a session
- Call [`SSLCreateContext(_:_:_:)`](./sslcreatecontext%28_,_,_%29.md) to create a new SSL session context.
- Write the [`SSLWriteFunc`](./sslwritefunc.md) and [`SSLReadFunc`](./sslreadfunc.md) I/O functions and register them with Secure Transport by calling the [`SSLSetIOFuncs(_:_:_:)`](./sslsetiofuncs%28_,_,_%29.md) function.
- Establish a connection using [CFNetwork](../CFNetwork/CFNetwork.md), BSD Sockets, or Open Transport. Then call [`SSLSetConnection(_:_:)`](./sslsetconnection%28_,_%29.md) to specify the connection to which the SSL session context applies.
- Call [`SSLSetPeerDomainName(_:_:_:)`](./sslsetpeerdomainname%28_,_,_%29.md) to specify the fully-qualified domain name of the peer to which you want to connect (optional but highly recommended).
- Call [`SSLSetCertificate(_:_:)`](./sslsetcertificate%28_,_%29.md) to specify the certificate to be used in authentication (required for server side, optional for client).
- Start a session
- Call [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) to perform the SSL handshake and establish a secure session.
- Maintain a session
- To transfer data over the secure session, Secure Transport calls your [`SSLWrite(_:_:_:_:)`](./sslwrite%28_,_,_,_%29.md) and [`SSLRead(_:_:_:_:)`](./sslread%28_,_,_,_%29.md) functions as needed.
- End a session
- Call [`SSLClose(_:)`](./sslclose%28_%29.md) to close the secure session.
- Close the connection and dispose of the connection reference.
- Release the SSL session context by calling [`CFRelease`](../CoreFoundation/cfrelease.md).
- If you called `SSLGetPeerCertificates` to obtain any certificates, call [`CFRelease`](../CoreFoundation/cfrelease.md) to release the certificate reference objects.

In many cases, it is easier to use the CFNetwork API than Secure Transport to implement a simple connection to a secure (HTTPS) URL. See [CFNetwork Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132) for documentation of the CFNetwork API and the CFNetworkHTTPDownload sample code for an example of code that downloads data from a URL. If you specify an HTTPS URL, this routine automatically uses Secure Transport to encrypt the data stream.

For functions to manage and evaluate certificates, see [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/using-the-secure-socket-layer-for-network-communication)*