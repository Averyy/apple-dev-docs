# uuidString

**Framework**: Foundation  
**Kind**: property

The UUID as a string.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uuidString: String { get }
```

#### Discussion

A string containing a formatted UUID for example `E621E1F8-C36C-495A-93FC-0C247A3E6E5F`.

Use this property when you need a string representation of the `NSUUID` object—for example, to compare with a [`CFUUID`](https://developer.apple.com/documentation/CoreFoundation/CFUUID) object.

## See Also

- [func getBytes(UnsafeMutablePointer<UInt8>)](nsuuid/getbytes(_:).md)
  Returns the UUID as bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/uuidstring)*