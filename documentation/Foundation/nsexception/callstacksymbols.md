# callStackSymbols

**Framework**: Foundation  
**Kind**: property

An array containing the current call stack symbols.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var callStackSymbols: [String] { get }
```

#### Discussion

An array of strings describing the call stack backtrace at the moment the exception was first raised. The format of each string is determined by the `backtrace_symbols()` API

## See Also

- [var callStackReturnAddresses: [NSNumber]](nsexception/callstackreturnaddresses.md)
  The call return addresses related to a raised exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/callstacksymbols)*