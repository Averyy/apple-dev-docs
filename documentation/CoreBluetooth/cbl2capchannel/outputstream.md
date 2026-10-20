# outputStream

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The stream used for writing data to the peer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var outputStream: OutputStream! { get }
```

```objc
@property (nonatomic, readonly) NSOutputStream * outputStream;
```

## See Also

### Accessing Streams
- [var inputStream: InputStream!](./inputstream.md)
  The stream used for reading data from the remote peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbl2capchannel/outputstream)*