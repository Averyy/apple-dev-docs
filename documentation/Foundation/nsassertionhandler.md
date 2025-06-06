# NSAssertionHandler

**Framework**: Foundation  
**Kind**: class

An object that logs an assertion to the console.

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
class NSAssertionHandler
```

#### Overview

`NSAssertionHandler` objects are automatically created to handle false assertions. Assertion macros, such as `NSAssert` and `NSCAssert`, are used to evaluate a condition, and if the condition evaluates to false, the macros pass a string to an `NSAssertionHandler` object describing the failure. Each thread has its own `NSAssertionHandler` object. When invoked, an assertion handler prints an error message that includes the method and class (or function) containing the assertion and raises an `NSInternalInconsistencyException`.

You create assertions only using the assertion macros—you rarely need to invoke `NSAssertionHandler` methods directly. The macros for use inside methods and functions send [`handleFailureInMethod:object:file:lineNumber:description:`](nsassertionhandler/handlefailureinmethod:object:file:linenumber:description:.md) and [`handleFailureInFunction:file:lineNumber:description:`](nsassertionhandler/handlefailureinfunction:file:linenumber:description:.md) messages respectively to the current assertion handler. The assertion handler for the current thread is obtained using the [`current`](nsassertionhandler/current.md) class method. See [`NSAssertionHandlerKey`](nsassertionhandlerkey.md) if you need to customize the behavior of [`NSAssertionHandler`](nsassertionhandler.md).

## Topics

### Handling Assertion Failures
- [class var current: NSAssertionHandler](nsassertionhandler/current.md)
  Returns the `NSAssertionHandler` object associated with the current thread.
### Constants
- [NSAssertionHandlerKey](nsassertionhandlerkey.md)
  This constant refers to a key in the thread dictionary of the per-thread assertion handler object

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsassertionhandler)*