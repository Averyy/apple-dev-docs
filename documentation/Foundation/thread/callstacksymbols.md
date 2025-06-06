# callStackSymbols

**Framework**: Foundation  
**Kind**: property

Returns an array containing the call stack symbols.

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
class var callStackSymbols: [String] { get }
```

#### Return Value

An array containing the call stack symbols. Each element is an `NSString` object with a value in a format determined by the `backtrace_symbols()` function. For more information, see backtrace_symbols(3) macOS Developer Tools Manual Page.

#### Discussion

The return value describes the call stack backtrace of the current thread at the moment this method was called.

## See Also

- [class func isMultiThreaded() -> Bool](thread/ismultithreaded.md)
  Returns whether the application is multithreaded.
- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [class var callStackReturnAddresses: [NSNumber]](thread/callstackreturnaddresses.md)
  Returns an array containing the call stack return addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/callstacksymbols)*