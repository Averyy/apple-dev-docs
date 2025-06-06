# callStackReturnAddresses

**Framework**: Foundation  
**Kind**: property

Returns an array containing the call stack return addresses.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var callStackReturnAddresses: [NSNumber] { get }
```

#### Return Value

An array containing the call stack return addresses. Each element is an `NSNumber` object containing an `NSUInteger` value.

## See Also

- [class func isMultiThreaded() -> Bool](thread/ismultithreaded.md)
  Returns whether the application is multithreaded.
- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [class var callStackSymbols: [String]](thread/callstacksymbols.md)
  Returns an array containing the call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/callstackreturnaddresses)*