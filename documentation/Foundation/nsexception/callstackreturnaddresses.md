# callStackReturnAddresses

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The call return addresses related to a raised exception.

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
var callStackReturnAddresses: [NSNumber] { get }
```

```objc
@property (copy, readonly) NSArray<NSNumber *> * callStackReturnAddresses;
```

#### Discussion

An array of [`NSNumber`](../nsnumber.md) objects encapsulating [`NSUInteger`](../../ObjectiveC/nsuinteger.md) values. Each value is a call frame return address. The array of stack frames starts at the point at which the exception was first raised, with the first items being the most recent stack frames.

`NSException` subclasses posing as the `NSException` class or subclasses or other API elements that interfere with the exception-raising mechanism may not get this information.

## See Also

### Getting Exception Stack Frames
- [var callStackSymbols: [String]](./callstacksymbols.md)
  An array containing the current call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexception/callstackreturnaddresses)*