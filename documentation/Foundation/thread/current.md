# current

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the thread object representing the current thread of execution.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var current: Thread { get }
```

```objc
@property (class, strong, readonly) NSThread * currentThread;
```

#### Return Value

A thread object representing the current thread of execution.

## See Also

### Related Documentation
- [class func detachNewThreadSelector(Selector, toTarget: Any, with: Any?)](./detachnewthreadselector%28_,totarget,with%29.md)
  Detaches a new thread and uses the specified selector as the thread entry point.
### Querying the Environment
- [class func isMultiThreaded() -> Bool](./ismultithreaded%28%29.md)
  Returns whether the application is multithreaded.
- [class var callStackReturnAddresses: [NSNumber]](./callstackreturnaddresses.md)
  Returns an array containing the call stack return addresses.
- [class var callStackSymbols: [String]](./callstacksymbols.md)
  Returns an array containing the call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/current)*