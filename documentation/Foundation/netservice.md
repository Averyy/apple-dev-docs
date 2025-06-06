# NetService

**Framework**: Foundation  
**Kind**: class

A network service that broadcasts its availability using multicast DNS.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class NetService
```

#### Overview

The [`NetService`](netservice.md) class represents a network service, either one your application publishes or is a client of. This class and the [`NetServiceBrowser`](netservicebrowser.md) class use multicast DNS to convey information about network services to and from your application. The API of [`NetService`](netservice.md) provides a convenient way to publish the services offered by your application and to resolve the socket address for a service.

The types of services you access using [`NetService`](netservice.md) are the same types that you access directly using BSD sockets. HTTP and FTP are two services commonly provided by systems. (For a list of common services and the ports used by those services, see the file `/etc/services`.) Applications can also define their own custom services to provide specific data to clients.

You can use the [`NetService`](netservice.md) class as either a publisher of a service or a client of a service. If your application publishes a service, your code must acquire a port and prepare a socket to communicate with clients. Once your socket is ready, you use the [`NetService`](netservice.md) class to notify clients that your service is ready. If your application is the client of a network service, you can either create an [`NetService`](netservice.md) object directly (if you know the exact host and port information) or use an [`NetServiceBrowser`](netservicebrowser.md) object to browse for services.

To publish a service, initialize your [`NetService`](netservice.md) object with the service name, domain, type, and port information. All of this information must be valid for the socket created by your application. Once initialized, call the [`publish()`](netservice/publish().md) method to broadcast your service information to the network.

When connecting to a service, use the [`NetServiceBrowser`](netservicebrowser.md) class to locate the service on the network and obtain the corresponding [`NetService`](netservice.md) object. Once you have the object, call the [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) method to verify that the service is available and ready for your application. If it is, the [`addresses`](netservice/addresses.md) property provides the socket information you can use to connect to the service.

The methods of [`NetService`](netservice.md) operate asynchronously so your application is not impacted by the speed of the network. All information about a service is returned to your application through the [`NetService`](netservice.md) object’s delegate. You must provide a delegate object to respond to messages and to handle errors appropriately.

## Topics

### Creating Network Services
- [convenience init(domain: String, type: String, name: String)](netservice/init(domain:type:name:).md)
  Returns the receiver, initialized as a network service of a given type and sets the initial host information.
- [init(domain: String, type: String, name: String, port: Int32)](netservice/init(domain:type:name:port:).md)
  Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`.
### Configuring Network Services
- [class func data(fromTXTRecord: [String : Data]) -> Data](netservice/data(fromtxtrecord:).md)
  Returns an `NSData` object representing a TXT record formed from a given dictionary.
- [class func dictionary(fromTXTRecord: Data) -> [String : Data]](netservice/dictionary(fromtxtrecord:).md)
  Returns a dictionary representing a TXT record given as an `NSData` object.
- [var addresses: [Data]?](netservice/addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
- [var domain: String](netservice/domain.md)
  A string containing the domain for this service.
- [var includesPeerToPeer: Bool](netservice/includespeertopeer.md)
  Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available. [`false`](https://developer.apple.com/documentation/swift/false) by default.
- [func getInputStream(UnsafeMutablePointer<InputStream?>?, outputStream: UnsafeMutablePointer<OutputStream?>?) -> Bool](netservice/getinputstream(_:outputstream:).md)
  Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully.
- [var name: String](netservice/name.md)
  A string containing the name of this service.
- [var type: String](netservice/type.md)
  The type of the published service.
- [func txtRecordData() -> Data?](netservice/txtrecorddata.md)
  Returns the TXT record for the receiver.
- [func setTXTRecord(Data?) -> Bool](netservice/settxtrecord(_:).md)
  Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful.
- [var delegate: (any NetServiceDelegate)?](netservice/delegate.md)
  The delegate for the receiver.
### Managing Run Loops
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](netservice/schedule(in:formode:).md)
  Adds the service to the specified run loop.
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](netservice/remove(from:formode:).md)
  Removes the service from the given run loop for a given mode.
### Using Network Services
- [func publish()](netservice/publish.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](netservice/publish(options:).md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve()](netservice/resolve.md)
  Starts a resolve process for the service.
- [func resolve(withTimeout: TimeInterval)](netservice/resolve(withtimeout:).md)
  Starts a resolve process of a finite duration for the service.
- [var port: Int](netservice/port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](netservice/startmonitoring.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](netservice/stop.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](netservice/stopmonitoring.md)
  Stops the monitoring of TXT-record updates for the receiver.
### Obtaining the DNS Hostname
- [var hostName: String?](netservice/hostname.md)
  A string containing the DNS hostname for this service.
### Constants
- [NSNetServices Errors](nsnetservices-errors.md)
  If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [NetService.ErrorCode](netservice/errorcode-swift.enum.md)
  These constants identify errors that can occur when accessing net services.
- [NetService.Options](netservice/options.md)
  These constants specify options for a network service.

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

- [protocol NetServiceDelegate](netservicedelegate.md)
  The interface a net service uses to inform its delegate about the state of the service it offers.
- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells the user why the app is requesting access to the local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice)*