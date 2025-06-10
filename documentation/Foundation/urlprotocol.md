# URLProtocol

**Framework**: Foundation  
**Kind**: class

An abstract class that handles the loading of protocol-specific URL data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class URLProtocol
```

#### Overview

Don’t instantiate a [`URLProtocol`](urlprotocol.md) subclass directly. Instead, create subclasses for any custom protocols or URL schemes that your app supports. When a download starts, the system creates the appropriate protocol object to handle the corresponding URL request. You define your protocol class and call the [`registerClass(_:)`](urlprotocol/registerclass(_:).md) class method during your app’s launch time so that the system is aware of your protocol.

> **Note**:  You cannot use this class to define custom URL schemes and protocols in watchOS 2 and later.

To support the customization of protocol-specific requests, create extensions to the [`URLRequest`](urlrequest.md) class to provide any custom API that you need. You can store and retrieve protocol-specific request data by using [`URLProtocol`](urlprotocol.md)’s class methods [`property(forKey:in:)`](urlprotocol/property(forkey:in:).md) and [`setProperty(_:forKey:in:)`](urlprotocol/setproperty(_:forkey:in:).md).

Create a [`URLResponse`](urlresponse.md) for each request your subclass processes successfully. You may want to create a custom [`URLResponse`](urlresponse.md) class to provide protocol specific information.

##### Subclassing Notes

When overriding methods of this class, be aware that methods that take a `task` parameter are preferred by the system to those that do not. Therefore, you should override the task-based methods when subclassing, as follows:

Swift:

- Initialization — Override [`init(task:cachedResponse:client:)`](urlprotocol/init(task:cachedresponse:client:).md) instead of or in addition to [`init(request:cachedResponse:client:)`](urlprotocol/init(request:cachedresponse:client:).md). Also override the task-based [`canInit(with:)`](urlprotocol/caninit(with:)-18gbo.md) instead of or in addition to the request-based [`canInit(with:)`](urlprotocol/caninit(with:)-76brg.md).

Objective-C:

- Initialization — Override [`canInit(with:)`](urlprotocol/caninit(with:)-18gbo.md) and [`init(task:cachedResponse:client:)`](urlprotocol/init(task:cachedresponse:client:).md) instead of or in addition to [`canInit(with:)`](urlprotocol/caninit(with:)-76brg.md) and [`init(request:cachedResponse:client:)`](urlprotocol/init(request:cachedresponse:client:).md).

## Topics

### Creating protocol objects
- [init(request: URLRequest, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)](urlprotocol/init(request:cachedresponse:client:).md)
  Creates a URL protocol instance to handle the request.
- [convenience init(task: URLSessionTask, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)](urlprotocol/init(task:cachedresponse:client:).md)
  Creates a URL protocol instance to handle the task.
### Registering and unregistering protocol classes
- [class func registerClass(AnyClass) -> Bool](urlprotocol/registerclass(_:).md)
  Attempts to register a subclass of [`URLProtocol`](urlprotocol.md), making it visible to the URL loading system.
- [class func unregisterClass(AnyClass)](urlprotocol/unregisterclass(_:).md)
  Unregisters the specified subclass of [`URLProtocol`](urlprotocol.md).
### Determining If a subclass can handle a request
- [class func canInit(with: URLRequest) -> Bool](urlprotocol/caninit(with:)-76brg.md)
  Determines whether the protocol subclass can handle the specified request.
- [class func canInit(with: URLSessionTask) -> Bool](urlprotocol/caninit(with:)-18gbo.md)
  Determines whether the protocol subclass can handle the specified task.
### Getting and setting request properties
- [class func property(forKey: String, in: URLRequest) -> Any?](urlprotocol/property(forkey:in:).md)
  Fetches the property associated with the specified key in the specified request.
- [class func setProperty(Any, forKey: String, in: NSMutableURLRequest)](urlprotocol/setproperty(_:forkey:in:).md)
  Sets the property associated with the specified key in the specified request.
- [class func removeProperty(forKey: String, in: NSMutableURLRequest)](urlprotocol/removeproperty(forkey:in:).md)
  Removes the property associated with the specified key in the specified request.
### Providing a canonical version of a request
- [class func canonicalRequest(for: URLRequest) -> URLRequest](urlprotocol/canonicalrequest(for:).md)
  Returns a canonical version of the specified request.
### Determining if requests are cache equivalent
- [class func requestIsCacheEquivalent(URLRequest, to: URLRequest) -> Bool](urlprotocol/requestiscacheequivalent(_:to:).md)
  A Boolean value indicating whether two requests are equivalent for cache purposes.
### Starting and stopping downloads
- [func startLoading()](urlprotocol/startloading.md)
  Starts protocol-specific loading of the request.
- [func stopLoading()](urlprotocol/stoploading.md)
  Stops protocol-specific loading of the request.
### Getting protocol attributes
- [var cachedResponse: CachedURLResponse?](urlprotocol/cachedresponse.md)
  The protocol’s cached response.
- [var client: (any URLProtocolClient)?](urlprotocol/client.md)
  The object the protocol uses to communicate with the URL loading system.
- [protocol URLProtocolClient](urlprotocolclient.md)
  The interface used by [`URLProtocol`](urlprotocol.md) subclasses to communicate with the URL Loading System.
- [var request: URLRequest](urlprotocol/request.md)
  The protocol’s request.
- [var task: URLSessionTask?](urlprotocol/task.md)
  The protocol’s task.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var protocolClasses: [AnyClass]?](urlsessionconfiguration/protocolclasses.md)
  An array of extra protocol subclasses that handle requests in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol)*