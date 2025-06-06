# Using the Secure Socket Layer for Network Communication

**Framework**: Security

Establish Secure Sockets Layer (SSL) sessions to facilitate secure communication between client and server.

#### Overview

The following terms are used in this discussion:

Most applications need only a few of the functions in this API, which are normally called in the following sequence:

- Prepare for a session
- Call [`SSLCreateContext(_:_:_:)`](sslcreatecontext(_:_:_:).md) to create a new SSL session context.
- Write the [`SSLWriteFunc`](sslwritefunc.md) and [`SSLReadFunc`](sslreadfunc.md) I/O functions and register them with Secure Transport by calling the [`SSLSetIOFuncs(_:_:_:)`](sslsetiofuncs(_:_:_:).md) function.
- Establish a connection using [`CFNetwork`](https://developer.apple.com/documentation/CFNetwork), BSD Sockets, or Open Transport. Then call [`SSLSetConnection(_:_:)`](sslsetconnection(_:_:).md) to specify the connection to which the SSL session context applies.
- Call [`SSLSetPeerDomainName(_:_:_:)`](sslsetpeerdomainname(_:_:_:).md) to specify the fully-qualified domain name of the peer to which you want to connect (optional but highly recommended).
- Call [`SSLSetCertificate(_:_:)`](sslsetcertificate(_:_:).md) to specify the certificate to be used in authentication (required for server side, optional for client).
- Start a session
- Call [`SSLHandshake(_:)`](sslhandshake(_:).md) to perform the SSL handshake and establish a secure session.
- Maintain a session
- To transfer data over the secure session, Secure Transport calls your [`SSLWrite(_:_:_:_:)`](sslwrite(_:_:_:_:).md) and [`SSLRead(_:_:_:_:)`](sslread(_:_:_:_:).md) functions as needed.
- End a session
- Call [`SSLClose(_:)`](sslclose(_:).md) to close the secure session.
- Close the connection and dispose of the connection reference.
- Release the SSL session context by calling [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).
- If you called `SSLGetPeerCertificates` to obtain any certificates, call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release the certificate reference objects.

In many cases, it is easier to use the CFNetwork API than Secure Transport to implement a simple connection to a secure (HTTPS) URL. See [`CFNetwork Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132) for documentation of the CFNetwork API and the CFNetworkHTTPDownload sample code for an example of code that downloads data from a URL. If you specify an HTTPS URL, this routine automatically uses Secure Transport to encrypt the data stream.

For functions to manage and evaluate certificates, see [`Certificate, Key, and Trust Services`](certificate-key-and-trust-services.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/using-the-secure-socket-layer-for-network-communication)*