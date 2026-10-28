# callStackReturnAddresses

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSArray<NSNumber *> * callStackReturnAddresses;
```

## Return Value

An array containing the call stack return addresses. Each element is an `NSNumber` object containing an `NSUInteger` value.

## See Also

### Querying the Environment
- [class func isMultiThreaded() -> Bool](./ismultithreaded%28%29.md)
  Returns whether the application is multithreaded.
- [class var current: Thread](./current.md)
  Returns the thread object representing the current thread of execution.
- [class var callStackSymbols: [String]](./callstacksymbols.md)
  Returns an array containing the call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/callstackreturnaddresses)*