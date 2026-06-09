# symbolicateAddress(_:)

**Framework**: CrashReportExtension  
**Kind**: method

Symbolicates an address, returning symbol info with inline frame expansion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
final func symbolicateAddress(_ address: UInt64) -> [SymbolicatedFrame]
```

#### Return Value

An array of frames, starting with the outermost.

## Parameters

- `address`: The address to symbolicate.

## See Also

- [func symbolicateAddresses([UInt64]) -> [[SymbolicatedFrame]]](crashedprocess/symbolicateaddresses(_:).md)
  Symbolicates an array of addresses, returning symbol information with inline frame expansion.
- [struct SymbolicatedFrame](symbolicatedframe.md)
  A type that represents a single symbolicated stack frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess/symbolicateaddress(_:))*