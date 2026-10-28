# domain

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string containing the domain for this service.

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
var domain: String { get }
```

```objc
@property (copy, readonly) NSString * domain;
```

## Discussion

This can be an explicit domain name or it can contain the generic local domain name, `@"local."` (note the trailing period, which indicates an absolute name).

This property’s value is set when the object is first initialized, whether by your code or by a browser object. See [`init(domain:type:name:)`](./init%28domain,type,name%29.md) for more information.

> **Backward Compatibility Note**:  This became a property in OS X v10.9 and iOS 7, but the underlying getter method (`domain`) has been available since this class was first introduced.

## See Also

### Configuring Network Services
- [class func data(fromTXTRecord: [String : Data]) -> Data](./data%28fromtxtrecord%29.md)
  Returns an `NSData` object representing a TXT record formed from a given dictionary.
- [class func dictionary(fromTXTRecord: Data) -> [String : Data]](./dictionary%28fromtxtrecord%29.md)
  Returns a dictionary representing a TXT record given as an `NSData` object.
- [var addresses: [Data]?](./addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/domain)*