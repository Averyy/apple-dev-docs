# delegate

**Framework**: Foundation  
**Kind**: property

The delegate for the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var delegate: (any NetServiceDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`NetServiceDelegate`](netservicedelegate.md) protocol, and is not retained.

> **Note**:  This became a property in OS X v10.9 and iOS 7, but the underlying getter and setter methods (`delegate` and `setDelegate`) have been available since this class was first introduced.

 This became a property in OS X v10.9 and iOS 7, but the underlying getter and setter methods (`delegate` and `setDelegate`) have been available since this class was first introduced.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/delegate)*