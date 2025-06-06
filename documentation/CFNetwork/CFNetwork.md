# CFNetwork

**Framework**: CFNetwork  
**Kind**: module

Access network services and handle changes in network configurations. Build on abstractions of network protocols to simplify tasks such as working with BSD sockets, administering HTTP and FTP servers, and managing Bonjour services.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Topics

### Errors
- [enum CFNetworkErrors](cfnetworkerrors.md)
  This enumeration contains error codes returned under the error domain [`kCFErrorDomainCFNetwork`](kcferrordomaincfnetwork.md).
- [Error Dictionary Keys](error-dictionary-keys.md)
  Networking-related keys that may be available in a `CFErrorRef` object’s `userInfo` dictionary.
- [Error Domains](error-domains.md)
  High-level error domains.
### Hosts
- [class CFHost](cfhost.md)
  An opaque reference representing an CFHost object.
- [enum CFHostInfoType](cfhostinfotype.md)
  Values indicating the type of data that is to be resolved or the type of data that was resolved.
- [struct CFHostClientContext](cfhostclientcontext.md)
  A structure containing user-defined data and callbacks for CFHost objects.
- [func CFHostCancelInfoResolution(CFHost, CFHostInfoType)](cfhostcancelinforesolution(_:_:).md)
  Cancels the resolution of a host.
- [func CFHostCreateCopy(CFAllocator?, CFHost) -> Unmanaged<CFHost>](cfhostcreatecopy(_:_:).md)
  Creates a new host object by copying.
- [func CFHostCreateWithAddress(CFAllocator?, CFData) -> Unmanaged<CFHost>](cfhostcreatewithaddress(_:_:).md)
  Uses an address to create an instance of a host object.
- [func CFHostCreateWithName(CFAllocator?, CFString) -> Unmanaged<CFHost>](cfhostcreatewithname(_:_:).md)
  Uses a name to create an instance of a host object.
- [func CFHostGetAddressing(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](cfhostgetaddressing(_:_:).md)
  Gets the addresses from a host.
- [func CFHostGetNames(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFArray>?](cfhostgetnames(_:_:).md)
  Gets the names from a CFHost.
- [func CFHostGetReachability(CFHost, UnsafeMutablePointer<DarwinBoolean>?) -> Unmanaged<CFData>?](cfhostgetreachability(_:_:).md)
  Gets reachability information from a host.
- [func CFHostGetTypeID() -> CFTypeID](cfhostgettypeid().md)
  Gets the Core Foundation type identifier for the CFHost opaque type.
- [func CFHostScheduleWithRunLoop(CFHost, CFRunLoop, CFString)](cfhostschedulewithrunloop(_:_:_:).md)
  Schedules a CFHost on a run loop.
- [func CFHostSetClient(CFHost, CFHostClientCallBack?, UnsafeMutablePointer<CFHostClientContext>?) -> Bool](cfhostsetclient(_:_:_:).md)
  Associates a client context and a callback function with a CFHost object or disassociates a client context and callback function that were previously set.
- [func CFHostStartInfoResolution(CFHost, CFHostInfoType, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhoststartinforesolution(_:_:_:).md)
  Starts resolution for a host object.
- [func CFHostUnscheduleFromRunLoop(CFHost, CFRunLoop, CFString)](cfhostunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFHost from a run loop.
### Global Proxy Configuration
- [func CFNetworkCopyProxiesForURL(CFURL, CFDictionary) -> Unmanaged<CFArray>](cfnetworkcopyproxiesforurl(_:_:).md)
  Returns the list of proxies that should be used to download a given URL.
- [func CFNetworkCopyProxiesForAutoConfigurationScript(CFString, CFURL, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](cfnetworkcopyproxiesforautoconfigurationscript(_:_:_:).md)
  Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- [func CFNetworkExecuteProxyAutoConfigurationScript(CFString, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationscript(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkExecuteProxyAutoConfigurationURL(CFURL, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationurl(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](cfnetworkcopysystemproxysettings().md)
  Returns a CFDictionary containing the current systemwide internet proxy settings.
- [typealias CFProxyAutoConfigurationResultCallback](cfproxyautoconfigurationresultcallback.md)
  Callback function called when a proxy autoconfiguration computation has completed.
- [Property Keys](property-keys.md)
  Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamSetProperty(_:_:_:)) and [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)).
- [Proxy Types](proxy-types.md)
  Constants that specify the type of proxy.
- [Global Proxy Settings Constants](global-proxy-settings-constants.md)
  Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](cfnetworkcopysystemproxysettings().md).
### HTTP Authentication
- [class CFHTTPAuthentication](cfhttpauthentication.md)
  An opaque reference representing HTTP authentication information.
- [func CFHTTPAuthenticationAppliesToRequest(CFHTTPAuthentication, CFHTTPMessage) -> Bool](cfhttpauthenticationappliestorequest(_:_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is associated with a CFHTTPMessage object.
- [func CFHTTPAuthenticationCopyDomains(CFHTTPAuthentication) -> Unmanaged<CFArray>](cfhttpauthenticationcopydomains(_:).md)
  Returns an array of domain URLs to which a given CFHTTPAuthentication object can be applied.
- [func CFHTTPAuthenticationCopyMethod(CFHTTPAuthentication) -> Unmanaged<CFString>](cfhttpauthenticationcopymethod(_:).md)
  Gets the strongest authentication method that will be used when a CFHTTPAuthentication object is applied to a request.
- [func CFHTTPAuthenticationCopyRealm(CFHTTPAuthentication) -> Unmanaged<CFString>](cfhttpauthenticationcopyrealm(_:).md)
  Gets an authentication information’s namespace.
- [func CFHTTPAuthenticationCreateFromResponse(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPAuthentication>](cfhttpauthenticationcreatefromresponse(_:_:).md)
  Uses an authentication failure response to create a CFHTTPAuthentication object.
- [func CFHTTPAuthenticationGetTypeID() -> CFTypeID](cfhttpauthenticationgettypeid().md)
  Gets the Core Foundation type identifier for the CFHTTPAuthentication opaque type.
- [func CFHTTPAuthenticationIsValid(CFHTTPAuthentication, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhttpauthenticationisvalid(_:_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object is valid.
- [func CFHTTPAuthenticationRequiresAccountDomain(CFHTTPAuthentication) -> Bool](cfhttpauthenticationrequiresaccountdomain(_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires an account domain.
- [func CFHTTPAuthenticationRequiresOrderedRequests(CFHTTPAuthentication) -> Bool](cfhttpauthenticationrequiresorderedrequests(_:).md)
  Returns a Boolean value that indicates whether authentication requests should be made one at a time.
- [func CFHTTPAuthenticationRequiresUserNameAndPassword(CFHTTPAuthentication) -> Bool](cfhttpauthenticationrequiresusernameandpassword(_:).md)
  Returns a Boolean value that indicates whether a CFHTTPAuthentication object uses an authentication method that requires a username and a password.
- [let kCFHTTPAuthenticationAccountDomain: CFString](kcfhttpauthenticationaccountdomain.md)
  Account domain to use for authentication.
- [let kCFHTTPAuthenticationPassword: CFString](kcfhttpauthenticationpassword.md)
  Password to use for authentication.
- [let kCFHTTPAuthenticationSchemeBasic: CFString](kcfhttpauthenticationschemebasic.md)
  Request the HTTP basic authentication scheme.
- [let kCFHTTPAuthenticationSchemeDigest: CFString](kcfhttpauthenticationschemedigest.md)
  Request the HTTP digest authentication scheme.
- [let kCFHTTPAuthenticationSchemeKerberos: CFString](kcfhttpauthenticationschemekerberos.md)
  Request the HTTP Kerberos authentication scheme.
- [let kCFHTTPAuthenticationSchemeNTLM: CFString](kcfhttpauthenticationschementlm.md)
  Request the HTTP NTLM authentication scheme.
- [let kCFHTTPAuthenticationSchemeNegotiate: CFString](kcfhttpauthenticationschemenegotiate.md)
  Request the HTTP Negotiate authentication scheme.
- [let kCFHTTPAuthenticationSchemeNegotiate2: CFString](kcfhttpauthenticationschemenegotiate2.md)
  Request the HTTP Negotiate v2 authentication scheme.
- [let kCFHTTPAuthenticationSchemeXMobileMeAuthToken: CFString](kcfhttpauthenticationschemexmobilemeauthtoken.md)
  Request the HTTP XMobileMeAuthToken authentication scheme.
- [let kCFHTTPAuthenticationUsername: CFString](kcfhttpauthenticationusername.md)
  Username to use for authentication.
### HTTP Messages
- [class CFHTTPMessage](cfhttpmessage.md)
  An opaque reference representing an HTTP message.
- [func CFHTTPMessageAddAuthentication(CFHTTPMessage, CFHTTPMessage?, CFString, CFString, CFString?, Bool) -> Bool](cfhttpmessageaddauthentication(_:_:_:_:_:_:).md)
  Adds authentication information to a request.
- [func CFHTTPMessageAppendBytes(CFHTTPMessage, UnsafePointer<UInt8>, CFIndex) -> Bool](cfhttpmessageappendbytes(_:_:_:).md)
  Appends data to a `CFHTTPMessage` object.
- [func CFHTTPMessageApplyCredentialDictionary(CFHTTPMessage, CFHTTPAuthentication, CFDictionary, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhttpmessageapplycredentialdictionary(_:_:_:_:).md)
  Use a dictionary containing authentication credentials to perform the authentication method specified by a `CFHTTPAuthentication` object.
- [func CFHTTPMessageApplyCredentials(CFHTTPMessage, CFHTTPAuthentication, CFString?, CFString?, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhttpmessageapplycredentials(_:_:_:_:_:).md)
  Performs the authentication method specified by a `CFHTTPAuthentication` object.
- [func CFHTTPMessageCopyAllHeaderFields(CFHTTPMessage) -> Unmanaged<CFDictionary>?](cfhttpmessagecopyallheaderfields(_:).md)
  Gets all header fields from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyBody(CFHTTPMessage) -> Unmanaged<CFData>?](cfhttpmessagecopybody(_:).md)
  Gets the body from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyHeaderFieldValue(CFHTTPMessage, CFString) -> Unmanaged<CFString>?](cfhttpmessagecopyheaderfieldvalue(_:_:).md)
  Gets the value of a header field from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyRequestMethod(CFHTTPMessage) -> Unmanaged<CFString>?](cfhttpmessagecopyrequestmethod(_:).md)
  Gets the request method from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyRequestURL(CFHTTPMessage) -> Unmanaged<CFURL>?](cfhttpmessagecopyrequesturl(_:).md)
  Gets the URL from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyResponseStatusLine(CFHTTPMessage) -> Unmanaged<CFString>?](cfhttpmessagecopyresponsestatusline(_:).md)
  Gets the status line from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopySerializedMessage(CFHTTPMessage) -> Unmanaged<CFData>?](cfhttpmessagecopyserializedmessage(_:).md)
  Serializes a CFHTTPMessage object.
- [func CFHTTPMessageCopyVersion(CFHTTPMessage) -> Unmanaged<CFString>](cfhttpmessagecopyversion(_:).md)
  Gets the HTTP version from a `CFHTTPMessage` object.
- [func CFHTTPMessageCreateCopy(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreatecopy(_:_:).md)
  Gets a copy of a CFHTTPMessage object.
- [func CFHTTPMessageCreateEmpty(CFAllocator?, Bool) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreateempty(_:_:).md)
  Creates and returns a new, empty `CFHTTPMessage` object.
- [func CFHTTPMessageCreateRequest(CFAllocator?, CFString, CFURL, CFString) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreaterequest(_:_:_:_:).md)
  Creates and returns a `CFHTTPMessage` object for an HTTP request.
- [func CFHTTPMessageCreateResponse(CFAllocator?, CFIndex, CFString?, CFString) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreateresponse(_:_:_:_:).md)
  Creates and returns a `CFHTTPMessage` object for an HTTP response.
- [func CFHTTPMessageGetResponseStatusCode(CFHTTPMessage) -> CFIndex](cfhttpmessagegetresponsestatuscode(_:).md)
  Gets the status code from a `CFHTTPMessage` object representing an HTTP response.
- [func CFHTTPMessageGetTypeID() -> CFTypeID](cfhttpmessagegettypeid().md)
  Returns the Core Foundation type identifier for the `CFHTTPMessage` opaque type.
- [func CFHTTPMessageIsHeaderComplete(CFHTTPMessage) -> Bool](cfhttpmessageisheadercomplete(_:).md)
  Determines whether a message header is complete.
- [func CFHTTPMessageIsRequest(CFHTTPMessage) -> Bool](cfhttpmessageisrequest(_:).md)
  Returns a Boolean indicating whether the HTTP message is a request or a response.
- [func CFHTTPMessageSetBody(CFHTTPMessage, CFData)](cfhttpmessagesetbody(_:_:).md)
  Sets the body of a `CFHTTPMessage` object.
- [func CFHTTPMessageSetHeaderFieldValue(CFHTTPMessage, CFString, CFString?)](cfhttpmessagesetheaderfieldvalue(_:_:_:).md)
  Sets the value of a header field in an HTTP message.
- [let kCFHTTPVersion1_0: CFString](kcfhttpversion1_0.md)
  Specifies HTTP version 1.0.
- [let kCFHTTPVersion1_1: CFString](kcfhttpversion1_1.md)
  Specifies HTTP version 1.1.
- [let kCFHTTPVersion2_0: CFString](kcfhttpversion2_0.md)
  HTTP version 2.0.
### FTP
- [func CFFTPCreateParsedResourceListing(CFAllocator?, UnsafePointer<UInt8>, CFIndex, UnsafeMutablePointer<Unmanaged<CFDictionary>?>?) -> CFIndex](cfftpcreateparsedresourcelisting(_:_:_:_:).md)
  Parses an FTP listing to a dictionary.
- [let kCFFTPResourceGroup: CFString](kcfftpresourcegroup.md)
  CFDictionary key for getting the CFString containing the name of a group that shares the FTP resource.
- [let kCFFTPResourceLink: CFString](kcfftpresourcelink.md)
  CFDictionary key for getting the CFString containing the symbolic link information. If the item is a symbolic link, the CFString contains the path to the item that the link references.
- [let kCFFTPResourceModDate: CFString](kcfftpresourcemoddate.md)
  CFDictionary key for getting the CFDate containing the last date and time the FTP resource was modified.
- [let kCFFTPResourceMode: CFString](kcfftpresourcemode.md)
  CFDictionary key for getting the CFNumber containing the access permissions, defined in `sys/types.h`, of the FTP resource.
- [let kCFFTPResourceName: CFString](kcfftpresourcename.md)
  CFDictionary key for getting the CFString containing the name of the FTP resource.
- [let kCFFTPResourceOwner: CFString](kcfftpresourceowner.md)
  CFDictionary key for getting the CFString containing the name of the owner of the FTP resource.
- [let kCFFTPResourceSize: CFString](kcfftpresourcesize.md)
  CFDictionary key for getting the CFNumber containing the size in bytes of the FTP resource.
- [let kCFFTPResourceType: CFString](kcfftpresourcetype.md)
  CFDictionary key for getting the CFNumber containing the type of the FTP resource as defined in `sys/dirent.h`.
### Network Diagnostics
- [class CFNetDiagnostic](cfnetdiagnostic.md)
  An opaque reference representing a CFNetDiagnostic.
- [enum CFNetDiagnosticStatusValues](cfnetdiagnosticstatusvalues.md)
  Constants for diagnostic status values.
- [func CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFNetDiagnosticStatus](cfnetdiagnosticcopynetworkstatuspassively(_:_:).md)
  Gets a network status value.
- [func CFNetDiagnosticCreateWithStreams(CFAllocator?, CFReadStream?, CFWriteStream?) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithstreams(_:_:_:).md)
  Creates a network diagnostic object from a pair of CFStreams.
- [func CFNetDiagnosticCreateWithURL(CFAllocator, CFURL) -> Unmanaged<CFNetDiagnostic>](cfnetdiagnosticcreatewithurl(_:_:).md)
  Creates a CFNetDiagnosticRef from a CFURLRef.
- [func CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic) -> CFNetDiagnosticStatus](cfnetdiagnosticdiagnoseprobleminteractively(_:).md)
  Opens a Network Diagnostics window.
- [func CFNetDiagnosticSetName(CFNetDiagnostic, CFString)](cfnetdiagnosticsetname(_:_:).md)
  Overrides the displayed application name.
### Network Services
- [class CFNetService](cfnetservice.md)
  An opaque reference representing a CFNetService.
- [class CFNetServiceBrowser](cfnetservicebrowser.md)
  An opaque reference representing a CFNetServiceBrowser.
- [struct CFNetServiceBrowserFlags](cfnetservicebrowserflags.md)
  Flags that the system passes to net service browser callbacks.
- [class CFNetServiceMonitor](cfnetservicemonitor.md)
  An opaque reference for a service monitor.
- [enum CFNetServiceMonitorType](cfnetservicemonitortype.md)
  Record type specifier used to tell a service monitor the type of record changes to watch for.
- [struct CFNetServiceClientContext](cfnetserviceclientcontext.md)
  A structure provided when a CFNetService is associated with a callback function or when a CFNetServiceBrowser is created.
- [struct CFNetServiceRegisterFlags](cfnetserviceregisterflags.md)
  Options to use when registering a service on the network.
- [enum CFNetServicesError](cfnetserviceserror.md)
  Error codes that may be returned by CFNetServices functions or passed to CFNetServices callback functions.
- [func CFNetServiceBrowserInvalidate(CFNetServiceBrowser)](cfnetservicebrowserinvalidate(_:).md)
  Invalidates an instance of a Network Service browser object.
- [func CFNetServiceBrowserScheduleWithRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](cfnetservicebrowserschedulewithrunloop(_:_:_:).md)
  Schedules a CFNetServiceBrowser on a run loop.
- [func CFNetServiceBrowserCreate(CFAllocator?, CFNetServiceBrowserClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>](cfnetservicebrowsercreate(_:_:_:).md)
  Creates an instance of a Network Service browser object.
- [func CFNetServiceBrowserGetTypeID() -> CFTypeID](cfnetservicebrowsergettypeid().md)
  Gets the Core Foundation type identifier for the Network Service browser object.
- [func CFNetServiceBrowserSearchForDomains(CFNetServiceBrowser, Bool, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicebrowsersearchfordomains(_:_:_:).md)
  Searches for domains.
- [func CFNetServiceBrowserSearchForServices(CFNetServiceBrowser, CFString, CFString, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicebrowsersearchforservices(_:_:_:_:).md)
  Searches a domain for services of a specified type.
- [func CFNetServiceBrowserStopSearch(CFNetServiceBrowser, UnsafeMutablePointer<CFStreamError>?)](cfnetservicebrowserstopsearch(_:_:).md)
  Stops a search for domains or services.
- [func CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser, CFRunLoop, CFString)](cfnetservicebrowserunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFNetServiceBrowser from a run loop and mode.
- [func CFNetServiceCancel(CFNetService)](cfnetservicecancel(_:).md)
  Cancels a service registration or a service resolution.
- [func CFNetServiceCreate(CFAllocator?, CFString, CFString, CFString, Int32) -> Unmanaged<CFNetService>](cfnetservicecreate(_:_:_:_:_:).md)
  Creates an instance of a Network Service object.
- [func CFNetServiceCreateCopy(CFAllocator?, CFNetService) -> Unmanaged<CFNetService>](cfnetservicecreatecopy(_:_:).md)
  Creates a copy of a CFNetService object.
- [func CFNetServiceCreateDictionaryWithTXTData(CFAllocator?, CFData) -> Unmanaged<CFDictionary>?](cfnetservicecreatedictionarywithtxtdata(_:_:).md)
  Uses TXT record data to create a dictionary.
- [func CFNetServiceCreateTXTDataWithDictionary(CFAllocator?, CFDictionary) -> Unmanaged<CFData>?](cfnetservicecreatetxtdatawithdictionary(_:_:).md)
  Flattens a set of key/value pairs into a CFDataRef suitable for passing to [`CFNetServiceSetTXTData(_:_:)`](cfnetservicesettxtdata(_:_:).md).
- [func CFNetServiceGetAddressing(CFNetService) -> Unmanaged<CFArray>?](cfnetservicegetaddressing(_:).md)
  Gets the IP addressing from a CFNetService.
- [func CFNetServiceGetDomain(CFNetService) -> Unmanaged<CFString>](cfnetservicegetdomain(_:).md)
  Gets the domain from a CFNetService.
- [func CFNetServiceGetName(CFNetService) -> Unmanaged<CFString>](cfnetservicegetname(_:).md)
  Gets the name from a CFNetService.
- [func CFNetServiceGetPortNumber(CFNetService) -> Int32](cfnetservicegetportnumber(_:).md)
  This function gets the port number from a CFNetService.
- [func CFNetServiceGetTXTData(CFNetService) -> Unmanaged<CFData>?](cfnetservicegettxtdata(_:).md)
  Queries a network service for the contents of its TXT records.
- [func CFNetServiceGetTargetHost(CFNetService) -> Unmanaged<CFString>?](cfnetservicegettargethost(_:).md)
  Queries a CFNetService for its target hosts.
- [func CFNetServiceGetType(CFNetService) -> Unmanaged<CFString>](cfnetservicegettype(_:).md)
  Gets the type from a CFNetService.
- [func CFNetServiceGetTypeID() -> CFTypeID](cfnetservicegettypeid().md)
  Gets the Core Foundation type identifier for the Network Service object.
- [func CFNetServiceMonitorCreate(CFAllocator?, CFNetService, CFNetServiceMonitorClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>](cfnetservicemonitorcreate(_:_:_:_:).md)
  Creates an instance of a NetServiceMonitor object that watches for record changes.
- [func CFNetServiceMonitorGetTypeID() -> CFTypeID](cfnetservicemonitorgettypeid().md)
  Gets the Core Foundation type identifier for all CFNetServiceMonitor instances.
- [func CFNetServiceMonitorInvalidate(CFNetServiceMonitor)](cfnetservicemonitorinvalidate(_:).md)
  Invalidates an instance of a Network Service monitor object.
- [func CFNetServiceMonitorScheduleWithRunLoop(CFNetServiceMonitor, CFRunLoop, CFString)](cfnetservicemonitorschedulewithrunloop(_:_:_:).md)
  Schedules a CFNetServiceMonitor on a run loop.
- [func CFNetServiceMonitorStart(CFNetServiceMonitor, CFNetServiceMonitorType, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetservicemonitorstart(_:_:_:).md)
  Starts monitoring.
- [func CFNetServiceMonitorStop(CFNetServiceMonitor, UnsafeMutablePointer<CFStreamError>?)](cfnetservicemonitorstop(_:_:).md)
  Stops a CFNetServiceMonitor.
- [func CFNetServiceMonitorUnscheduleFromRunLoop(CFNetServiceMonitor, CFRunLoop, CFString)](cfnetservicemonitorunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFNetServiceMonitor from a run loop.
- [func CFNetServiceRegisterWithOptions(CFNetService, CFOptionFlags, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetserviceregisterwithoptions(_:_:_:).md)
  Makes a CFNetService available on the network.
- [func CFNetServiceResolveWithTimeout(CFNetService, CFTimeInterval, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfnetserviceresolvewithtimeout(_:_:_:).md)
  Gets the IP address or addresses for a CFNetService.
- [func CFNetServiceSetClient(CFNetService, CFNetServiceClientCallBack?, UnsafeMutablePointer<CFNetServiceClientContext>?) -> Bool](cfnetservicesetclient(_:_:_:).md)
  Associates a callback function with a CFNetService or disassociates a callback function from a CFNetService.
- [func CFNetServiceSetTXTData(CFNetService, CFData) -> Bool](cfnetservicesettxtdata(_:_:).md)
  Sets the TXT record for a CFNetService.
- [func CFNetServiceUnscheduleFromRunLoop(CFNetService, CFRunLoop, CFString)](cfnetserviceunschedulefromrunloop(_:_:_:).md)
  Unschedules a CFNetService from a run loop.
- [func CFNetServiceScheduleWithRunLoop(CFNetService, CFRunLoop, CFString)](cfnetserviceschedulewithrunloop(_:_:_:).md)
  Schedules a CFNetService on a run loop.
### Streams
- [func CFReadStreamCreateForHTTPRequest(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFReadStream>](cfreadstreamcreateforhttprequest(_:_:).md)
  Creates a read stream for a CFHTTP request message.
- [func CFReadStreamCreateForStreamedHTTPRequest(CFAllocator?, CFHTTPMessage, CFReadStream) -> Unmanaged<CFReadStream>](cfreadstreamcreateforstreamedhttprequest(_:_:_:).md)
  Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory.
- [let kCFStreamPropertyHTTPAttemptPersistentConnection: CFString](kcfstreampropertyhttpattemptpersistentconnection.md)
- [let kCFStreamPropertyHTTPFinalRequest: CFString](kcfstreampropertyhttpfinalrequest.md)
  HTTP Final Request property. A value of type CFHTTPMessage containing the final message transmitted by the stream after all modifications (including authentication, connection policy, redirects, and so on) have been made. This property cannot be set.
- [let kCFStreamPropertyHTTPFinalURL: CFString](kcfstreampropertyhttpfinalurl.md)
  HTTP Final URL property. A value of type CFURL containing the final HTTP URL. This value differs from the URL in the original HTTP request if an autoredirection occurred. This property cannot be set.
- [let kCFStreamPropertyHTTPProxy: CFString](kcfstreampropertyhttpproxy.md)
- [let kCFStreamPropertyHTTPProxyHost: CFString](kcfstreampropertyhttpproxyhost.md)
- [let kCFStreamPropertyHTTPProxyPort: CFString](kcfstreampropertyhttpproxyport.md)
- [let kCFStreamPropertyHTTPRequestBytesWrittenCount: CFString](kcfstreampropertyhttprequestbyteswrittencount.md)
- [let kCFStreamPropertyHTTPResponseHeader: CFString](kcfstreampropertyhttpresponseheader.md)
  HTTP Response Header property. When copied by [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)), the header of an HTTP response message is returned.
- [let kCFStreamPropertyHTTPSProxyHost: CFString](kcfstreampropertyhttpsproxyhost.md)
- [let kCFStreamPropertyHTTPSProxyPort: CFString](kcfstreampropertyhttpsproxyport.md)
- [let kCFStreamPropertyHTTPShouldAutoredirect: CFString](kcfstreampropertyhttpshouldautoredirect.md)
  HTTP Should Auto Redirect property. Set this property to `kCFBooleanTrue` to enable autoredirection; set this property to `kCFBooleanFalse` to disable autoredirection.
- [func CFWriteStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFWriteStream>](cfwritestreamcreatewithftpurl(_:_:).md)
  Creates an FTP write stream.
- [func CFReadStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFReadStream>](cfreadstreamcreatewithftpurl(_:_:).md)
  Creates an FTP read stream.
- [let kCFStreamPropertyFTPAttemptPersistentConnection: CFString](kcfstreampropertyftpattemptpersistentconnection.md)
- [let kCFStreamPropertyFTPFetchResourceInfo: CFString](kcfstreampropertyftpfetchresourceinfo.md)
- [let kCFStreamPropertyFTPFileTransferOffset: CFString](kcfstreampropertyftpfiletransferoffset.md)
  FTP File Transfer Offset stream property key for set and copy operations. The value of this property is a CFNumber of type `kCFNumberLongLongType` representing the file offset at which to start the transfer.
- [let kCFStreamPropertyFTPPassword: CFString](kcfstreampropertyftppassword.md)
  FTP Password stream property key for set and copy operations. A value of type CFString for storing the login password. Don’t set this property when anonymous FTP is desired.
- [let kCFStreamPropertyFTPProxy: CFString](kcfstreampropertyftpproxy.md)
  FTP Proxy stream property key for set and copy operations. The property is a value of type CFDictionary that holds proxy dictionary key-value pairs. The dictionary returned by SystemConfiguration can also be set as the value of this property.
- [let kCFStreamPropertyFTPProxyHost: CFString](kcfstreampropertyftpproxyhost.md)
- [let kCFStreamPropertyFTPProxyPassword: CFString](kcfstreampropertyftpproxypassword.md)
- [let kCFStreamPropertyFTPProxyPort: CFString](kcfstreampropertyftpproxyport.md)
- [let kCFStreamPropertyFTPProxyUser: CFString](kcfstreampropertyftpproxyuser.md)
- [let kCFStreamPropertyFTPResourceSize: CFString](kcfstreampropertyftpresourcesize.md)
  FTP Resource Size read stream property key copy operations. This property stores a CFNumber of type `kCFNumberLongLongType` representing the size of a resource in bytes.
- [let kCFStreamPropertyFTPUsePassiveMode: CFString](kcfstreampropertyftpusepassivemode.md)
  FTP Passive Mode stream property key for set and copy operations. Set this property to `kCFBooleanTrue` to enable passive mode; set this property to `kCFBooleanFalse` to disable passive mode.
- [let kCFStreamPropertyFTPUserName: CFString](kcfstreampropertyftpusername.md)
  FTP User Name stream property key for set and copy operations. A value of type CFString for storing the login user name. Don’t set this property when anonymous FTP is desired.
- [func CFSocketStreamSOCKSGetError(UnsafePointer<CFStreamError>) -> Int32](cfsocketstreamsocksgeterror(_:).md)
  This function gets error codes in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.
- [func CFSocketStreamSOCKSGetErrorSubdomain(UnsafePointer<CFStreamError>) -> Int32](cfsocketstreamsocksgeterrorsubdomain(_:).md)
  Gets the error subdomain associated with errors in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.
- [func CFStreamCreatePairWithSocketToCFHost(CFAllocator?, CFHost, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](cfstreamcreatepairwithsockettocfhost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(CFAllocator?, CFNetService, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](cfstreamcreatepairwithsockettonetservice(_:_:_:_:).md)
  Creates a pair of streams for a CFNetService.
- [let kCFStreamNetworkServiceType: CFString](kcfstreamnetworkservicetype.md)
  The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See [`Stream Service Types`](https://developer.apple.com/documentation/CoreFoundation/stream-service-types) for a list of possible values.
- [let kCFStreamNetworkServiceTypeBackground: CFString](kcfstreamnetworkservicetypebackground.md)
  Specifies that the stream is a background download.
- [let kCFStreamNetworkServiceTypeCallSignaling: CFString](kcfstreamnetworkservicetypecallsignaling.md)
  A call signaling service.
- [let kCFStreamNetworkServiceTypeVideo: CFString](kcfstreamnetworkservicetypevideo.md)
  Specifies that the stream is providing interactive video data.
- [let kCFStreamNetworkServiceTypeVoIP: CFString](kcfstreamnetworkservicetypevoip.md)
  Specifies that the stream is providing VoIP service.
- [let kCFStreamNetworkServiceTypeVoice: CFString](kcfstreamnetworkservicetypevoice.md)
  Specifies that the stream is providing interactive voice data.
- [let kCFStreamErrorDomainFTP: Int32](kcfstreamerrordomainftp.md)
  The error code is an FTP error code.
- [let kCFStreamErrorDomainHTTP: Int32](kcfstreamerrordomainhttp.md)
  The error code is an HTTP error code.
- [let kCFStreamErrorDomainMach: Int32](kcfstreamerrordomainmach.md)
  The error code is a Mach error code defined in `mach/error.h`.
- [let kCFStreamErrorDomainNetDB: Int32](kcfstreamerrordomainnetdb.md)
  The error code is an error code defined in `netdb.h`.
- [let kCFStreamErrorDomainNetServices: Int32](kcfstreamerrordomainnetservices.md)
  The error code is a `CFNetService` error code. For details, see the [`CFNetServicesError`](cfnetserviceserror.md) enumeration.
- [let kCFStreamErrorDomainSOCKS: Int32](../CoreFoundation/kCFStreamErrorDomainSOCKS.md)
  The error code is a SOCKS proxy error.
- [let kCFStreamErrorDomainSSL: Int32](../CoreFoundation/kCFStreamErrorDomainSSL.md)
  The error code is an SSL error code as defined in `Security/SecureTransport.h`.
- [let kCFStreamErrorDomainSystemConfiguration: Int32](kcfstreamerrordomainsystemconfiguration.md)
  The error code is a system configuration error code as defined in `System/ConfigurationSystemConfiguration.h`.
- [let kCFStreamErrorDomainWinSock: CFIndex](kcfstreamerrordomainwinsock.md)
  When running CFNetwork code on Windows, this domain returns error codes associated with the underlying TCP/IP stack. You should also note that non-networking errors such as `ENOMEM` are delivered through the POSIX domain. See the header `winsock2.h` for relevant error codes.
- [let kCFStreamPropertyConnectionIsCellular: CFString](kcfstreampropertyconnectioniscellular.md)
  A boolean value indicating whether the stream is connected over a cellular (WWAN) interface. This is a read-only property, and is `false` until the connection has been established.
- [let kCFStreamPropertyNoCellular: CFString](kcfstreampropertynocellular.md)
  A Boolean value indicating that the connection should not be established over a cellular (WWAN) connection. This value can only be set  you open the stream.
- [let kCFStreamPropertyProxyLocalBypass: CFString](kcfstreampropertyproxylocalbypass.md)
  Proxy Local Bypass property key.
- [let kCFStreamPropertySOCKSPassword: CFString](../CoreFoundation/kCFStreamPropertySOCKSPassword.md)
  Constant for the key required to set a user’s password.
- [let kCFStreamPropertySOCKSProxy: CFString](../CoreFoundation/kCFStreamPropertySOCKSProxy.md)
  SOCKS proxy property key.
- [let kCFStreamPropertySOCKSProxyHost: CFString](../CoreFoundation/kCFStreamPropertySOCKSProxyHost.md)
  Constant for the SOCKS proxy host key.
- [let kCFStreamPropertySOCKSProxyPort: CFString](../CoreFoundation/kCFStreamPropertySOCKSProxyPort.md)
  Constant for the SOCKS proxy host port key.
- [let kCFStreamPropertySOCKSUser: CFString](../CoreFoundation/kCFStreamPropertySOCKSUser.md)
  Constant for the key required to set a user name.
- [let kCFStreamPropertySOCKSVersion: CFString](../CoreFoundation/kCFStreamPropertySOCKSVersion.md)
  Constant for the SOCKS version key.
- [let kCFStreamPropertySSLContext: CFString](kcfstreampropertysslcontext.md)
- [let kCFStreamPropertySSLPeerCertificates: CFString](kcfstreampropertysslpeercertificates.md)
  SSL Peer Certificates property key for copy operations, which return a `CFArray` object containing `SecCertificateRef` objects.
- [let kCFStreamPropertySSLPeerTrust: CFString](kcfstreampropertysslpeertrust.md)
  SSL Peer Trust property key for copy operations, which return a `SecTrustRef` object containing the result of the SSL handshake.
- [let kCFStreamPropertySSLSettings: CFString](kcfstreampropertysslsettings.md)
  SSL Settings property key for set operations.
- [let kCFStreamPropertyShouldCloseNativeSocket: CFString](../CoreFoundation/kCFStreamPropertyShouldCloseNativeSocket.md)
  Should Close Native Socket property key.
- [let kCFStreamPropertySocketExtendedBackgroundIdleMode: CFString](kcfstreampropertysocketextendedbackgroundidlemode.md)
  A Boolean value to request that the system keep a socket open and delays reclaiming it when the process moves to the background.
- [let kCFStreamPropertySocketRemoteHost: CFString](kcfstreampropertysocketremotehost.md)
  The key’s value is a `CFHostRef` for the remote host if it is known. If not, its value is `NULL`.
- [let kCFStreamPropertySocketRemoteNetService: CFString](kcfstreampropertysocketremotenetservice.md)
  The key’s value is a `CFNetServiceRef` for the remote network service if it is known. If not, its value is `NULL`.
- [let kCFStreamPropertySocketSecurityLevel: CFString](../CoreFoundation/kCFStreamPropertySocketSecurityLevel.md)
  Socket Security Level property key.
- [let kCFStreamSSLAllowsAnyRoot: CFString](kcfstreamsslallowsanyroot.md)
  Security property key whose value indicates whether root certificates should be allowed.
- [let kCFStreamSSLAllowsExpiredCertificates: CFString](kcfstreamsslallowsexpiredcertificates.md)
  Security property key whose value indicates whether expired certificates are allowed.
- [let kCFStreamSSLAllowsExpiredRoots: CFString](kcfstreamsslallowsexpiredroots.md)
  Security property whose value indicates whether expired root certificates are allowed.
- [let kCFStreamSSLCertificates: CFString](kcfstreamsslcertificates.md)
  Security property key whose value is a CFArray of SecCertificateRefs except for the first element in the array, which is a SecIdentityRef.
- [let kCFStreamSSLIsServer: CFString](kcfstreamsslisserver.md)
  Security property key whose value indicates whether the connection is to act as a server in the SSL process.
- [let kCFStreamSSLLevel: CFString](kcfstreamssllevel.md)
  Security property key whose value specifies the stream’s security level.
- [let kCFStreamSSLPeerName: CFString](kcfstreamsslpeername.md)
  Security property key whose value overrides the name used for certificate verification.
- [let kCFStreamSSLValidatesCertificateChain: CFString](kcfstreamsslvalidatescertificatechain.md)
  Security property key whose value indicates whether the certificate chain should be validated.
- [let kCFStreamSocketSOCKSVersion4: CFString](../CoreFoundation/kCFStreamSocketSOCKSVersion4.md)
  Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- [let kCFStreamSocketSOCKSVersion5: CFString](../CoreFoundation/kCFStreamSocketSOCKSVersion5.md)
  Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- [let kCFStreamSocketSecurityLevelNegotiatedSSL: CFString](../CoreFoundation/kCFStreamSocketSecurityLevelNegotiatedSSL.md)
  Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.
- [let kCFStreamSocketSecurityLevelNone: CFString](../CoreFoundation/kCFStreamSocketSecurityLevelNone.md)
  Specifies that no security level be set.
- [let kCFStreamSocketSecurityLevelSSLv2: CFString](../CoreFoundation/kCFStreamSocketSecurityLevelSSLv2.md)
  Specifies that SSL version 2 be set as the security protocol for a socket stream.
- [let kCFStreamSocketSecurityLevelSSLv3: CFString](../CoreFoundation/kCFStreamSocketSecurityLevelSSLv3.md)
  Specifies that SSL version 3 be set as the security protocol for a socket stream pair.
- [let kCFStreamSocketSecurityLevelTLSv1: CFString](../CoreFoundation/kCFStreamSocketSecurityLevelTLSv1.md)
  Specifies that TLS version 1 be set as the security protocol for a socket stream.
- [enum CFStreamErrorHTTP](cfstreamerrorhttp.md)
  Error codes that a read stream for an HTTP request may return.
- [enum CFStreamErrorHTTPAuthentication](cfstreamerrorhttpauthentication.md)
  Authentication error codes that may be returned when trying to apply authentication to a request.
- [Secure Sockets (SOCKS) Errors](1518266-secure-sockets-socks-errors.md)
  Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
### Reference
- [CFNetwork Data Types](cfnetwork-data-types.md)
  Callback types for various network services.
- [CFNetwork Enumerations](cfnetwork-enumerations.md)
  Enumerated values related to SOCKS.
- [CFNetwork Constants](cfnetwork-constants.md)
  Constants for use with CFNetwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CFNetwork)*