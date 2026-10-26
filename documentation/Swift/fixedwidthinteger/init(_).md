# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Convert from an Backtrace.Address.

**Availability**:
- Mac Catalyst 13.0+
- macOS 26.0+

## Declaration

```swift
init?(_ address: Backtrace.Address)
```

#### Discussion

This initializer will return nil if the address width is larger than the type you are attempting to convert into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fixedwidthinteger/init(_:))*