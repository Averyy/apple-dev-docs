# addresses

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A read-only array containing `NSData` objects, each of which contains a socket address for the service.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t or nw_listener_t in Network framework instead

## Declaration

```swift
var addresses: [Data]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSData *> * addresses;
```

## Discussion

An array containing `NSData` objects, each of which contains a socket address for the service. Each `NSData` object in the returned array contains an appropriate `sockaddr` structure that you can use to connect to the socket. The exact type of this structure depends on the service to which you are connecting. If no addresses were resolved for the service, the returned array contains zero elements.

It is possible for a single service to resolve to more than one address or not resolve to any addresses. A service might resolve to multiple addresses if the computer publishing the service is currently multihoming.

> **Backward Compatibility Note**:  This became a property in OS X v10.9 and iOS 7, but the underlying getter method (`addresses`) has been available since this class was first introduced.

## See Also

### Related Documentation
- [func resolve()](./resolve%28%29.md)
  Starts a resolve process for the service.
### Configuring Network Services
- [class func data(fromTXTRecord: [String : Data]) -> Data](./data%28fromtxtrecord%29.md)
  Returns an `NSData` object representing a TXT record formed from a given dictionary.
- [class func dictionary(fromTXTRecord: Data) -> [String : Data]](./dictionary%28fromtxtrecord%29.md)
  Returns a dictionary representing a TXT record given as an `NSData` object.
- [var domain: String](./domain.md)
  A string containing the domain for this service.
- [var includesPeerToPeer: Bool](./includespeertopeer.md)
  Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available.
- [func getInputStream(UnsafeMutablePointer<InputStream?>?, outputStream: UnsafeMutablePointer<OutputStream?>?) -> Bool](./getinputstream%28_,outputstream%29.md)
  Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully.
- [var name: String](./name.md)
  A string containing the name of this service.
- [var type: String](./type.md)
  The type of the published service.
- [func txtRecordData() -> Data?](./txtrecorddata%28%29.md)
  Returns the TXT record for the receiver.
- [func setTXTRecord(Data?) -> Bool](./settxtrecord%28_%29.md)
  Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful.
- [var delegate: (any NetServiceDelegate)?](./delegate.md)
  The delegate for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/addresses)*