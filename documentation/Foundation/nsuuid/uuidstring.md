# uuidString

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSString * UUIDString;
```

## Discussion

A string containing a formatted UUID for example `E621E1F8-C36C-495A-93FC-0C247A3E6E5F`.

Use this property when you need a string representation of the `NSUUID` object—for example, to compare with a [`CFUUID`](../../CoreFoundation/cfuuid.md) object.

## See Also

### Get UUID Values
- [func getBytes(UnsafeMutablePointer<UInt8>)](./getbytes%28_%29.md)
  Returns the UUID as bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/uuidstring)*