# NSParameterAssert

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

Validates the specified parameter.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
#define NSParameterAssert(condition)
```

## Discussion

Assertions evaluate a condition and, if the condition evaluates to false, call the assertion handler for the current thread, passing it a format string and a variable number of arguments. Each thread has its own assertion handler, which is an object of class `NSAssertionHandler`. When invoked, an assertion handler prints an error message that includes method and class names (or the function name). It then raises an `NSInternalInconsistencyException` exception.

This macro validates a parameter for an Objective-C method. Simply provide the parameter as the `condition` argument. The macro evaluates the parameter and, if it is false, it logs an error message that includes the parameter and then raises an exception.

Assertions are disabled if the preprocessor macro `NS_BLOCK_ASSERTIONS` is defined. All assertion macros return void.

> ❗ **Important**:  Do not call functions with side effects in the `condition` parameter of this macro. The `condition` parameter is not evaluated when assertions are disabled, so if you call functions with side effects, those functions may never get called when you build the project in a non-debug configuration.

> **Note**:  Not all release configurations disable assertions by default.

## See Also

### Related Documentation
- [func NSLogv(String, CVaListPointer)](./nslogv%28_,_%29.md)
  Logs an error message to the Apple System Log facility.
- [NSLog](./nslog.md)
  Logs an error message to the Apple System Log facility.
### Assertions
- [class NSAssertionHandler](./nsassertionhandler.md)
  An object that logs an assertion to the console.
- [NSAssert](./nsassert.md)
  Generates an assertion if a given condition is false.
- [NSAssert1](./nsassert1.md)
  Generates an assertion if a given condition is false.
- [NSAssert2](./nsassert2.md)
  Generates an assertion if a given condition is false.
- [NSAssert3](./nsassert3.md)
  Generates an assertion if a given condition is false.
- [NSAssert4](./nsassert4.md)
  Generates an assertion if a given condition is false.
- [NSAssert5](./nsassert5.md)
  Generates an assertion if a given condition is false.
- [NSCAssert](./nscassert.md)
  Generates an assertion if the given condition is false.
- [NSCAssert1](./nscassert1.md)
  Generates an assertion if a given condition is false.
- [NSCAssert2](./nscassert2.md)
  Generates an assertion if a given condition is false.
- [NSCAssert3](./nscassert3.md)
  Generates an assertion if a given condition is false.
- [NSCAssert4](./nscassert4.md)
  Generates an assertion if a given condition is false.
- [NSCAssert5](./nscassert5.md)
  Generates an assertion if a given condition is false.
- [NSCParameterAssert](./nscparameterassert.md)
  Evaluates the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsparameterassert)*