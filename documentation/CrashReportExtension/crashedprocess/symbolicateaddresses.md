# symbolicateAddresses(_:)

**Framework**: CrashReportExtension  
**Kind**: method

Symbolicates an array of addresses, returning symbol information with inline frame expansion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
final func symbolicateAddresses(_ addresses: [UInt64]) -> [[SymbolicatedFrame]]
```

#### Return Value

An array of frame arrays, in order of the addresses requested.

## Parameters

- `addresses`: The addresses to symbolicate.

## See Also

- [func symbolicateAddress(UInt64) -> [SymbolicatedFrame]](crashedprocess/symbolicateaddress(_:).md)
  Symbolicates an address, returning symbol info with inline frame expansion.
- [struct SymbolicatedFrame](symbolicatedframe.md)
  A type that represents a single symbolicated stack frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess/symbolicateaddresses(_:))*