# getInputStream(_:outputStream:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully.

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
func getInputStream(_ inputStream: UnsafeMutablePointer<InputStream?>?, outputStream: UnsafeMutablePointer<OutputStream?>?) -> Bool
```

```objc
- (BOOL) getInputStream:(NSInputStream **) inputStream outputStream:(NSOutputStream **) outputStream;
```

## Return Value

[`true`](../../Swift/true.md) if the streams are created successfully, otherwise [`false`](../../Swift/false.md).

## Discussion

After this method is called, no delegate callbacks are called by the receiver.

> **Note**:  If automatic reference counting is not used, the input and output streams returned through the parameters are *retained*, which means that you are responsible for releasing them to avoid memory leaks.

## Parameters

- `inputStream`: Upon return, the input stream for the receiver. Pass `NULL` if you do not need this stream.
- `outputStream`: Upon return, the output stream for the receiver. Pass `NULL` if you do not need this stream.

## See Also

### Configuring Network Services
- [class func data(fromTXTRecord: [String : Data]) -> Data](./data%28fromtxtrecord%29.md)
  Returns an `NSData` object representing a TXT record formed from a given dictionary.
- [class func dictionary(fromTXTRecord: Data) -> [String : Data]](./dictionary%28fromtxtrecord%29.md)
  Returns a dictionary representing a TXT record given as an `NSData` object.
- [var addresses: [Data]?](./addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
- [var domain: String](./domain.md)
  A string containing the domain for this service.
- [var includesPeerToPeer: Bool](./includespeertopeer.md)
  Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/getinputstream(_:outputstream:))*