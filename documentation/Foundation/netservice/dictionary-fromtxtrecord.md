# dictionary(fromTXTRecord:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary representing a TXT record given as an `NSData` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func dictionary(fromTXTRecord txtData: Data) -> [String : Data]
```

#### Return Value

A dictionary representing `txtData`. The dictionary’s keys are `NSString` objects using UTF8 encoding. The values associated with all the dictionary’s keys are `NSData` objects that encapsulate strings or data. Fails an assertion if `txtData` cannot be represented as an `NSDictionary` object.

## Parameters

- `txtData`: A data object encoding a TXT record.

## See Also

- [class func data(fromTXTRecord: [String : Data]) -> Data](netservice/data(fromtxtrecord:).md)
  Returns an `NSData` object representing a TXT record formed from a given dictionary.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/dictionary(fromtxtrecord:))*