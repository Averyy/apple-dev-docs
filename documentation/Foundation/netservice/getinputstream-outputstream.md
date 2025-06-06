# getInputStream(_:outputStream:)

**Framework**: Foundation  
**Kind**: method

Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func getInputStream(_ inputStream: UnsafeMutablePointer<InputStream?>?, outputStream: UnsafeMutablePointer<OutputStream?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the streams are created successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

After this method is called, no delegate callbacks are called by the receiver.

> **Note**:  If automatic reference counting is not used, the input and output streams returned through the parameters are , which means that you are responsible for releasing them to avoid memory leaks.

## Parameters

- `inputStream`: Upon return, the input stream for the receiver. Pass   if you do not need this stream.
- `outputStream`: Upon return, the output stream for the receiver. Pass   if you do not need this stream.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/getinputstream(_:outputstream:))*