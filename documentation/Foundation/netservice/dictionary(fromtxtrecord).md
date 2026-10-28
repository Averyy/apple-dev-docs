# dictionary(fromTXTRecord:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a dictionary representing a TXT record given as an `NSData` object.

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
class func dictionary(fromTXTRecord txtData: Data) -> [String : Data]
```

```objc
+ (NSDictionary<NSString *,NSData *> *) dictionaryFromTXTRecordData:(NSData *) txtData;
```

## Return Value

A dictionary representing `txtData`. The dictionary’s keys are `NSString` objects using UTF8 encoding. The values associated with all the dictionary’s keys are `NSData` objects that encapsulate strings or data. Fails an assertion if `txtData` cannot be represented as an `NSDictionary` object.

## Parameters

- `txtData`: A data object encoding a TXT record.

## See Also

### Configuring Network Services
- [class func data(fromTXTRecord: [String : Data]) -> Data](./data%28fromtxtrecord%29.md)
  Returns an `NSData` object representing a TXT record formed from a given dictionary.
- [var addresses: [Data]?](./addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/dictionary(fromtxtrecord:))*