# NSAssert3

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

Generates an assertion if a given condition is false.

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
#define NSAssert3(condition, desc, arg1, arg2, arg3)
```

#### Discussion

The `NSAssert3` macro evaluates the condition and serves as a front end to the assertion handler.

Each thread has its own assertion handler, which is an object of class `NSAssertionHandler`. When invoked, an assertion handler prints an error message that includes the method and class names (or the function name). It then raises an `NSInternalInconsistencyException` exception. If `condition` evaluates to [`false`](../Swift/false.md), the macro invokes [`handleFailureInMethod:object:file:lineNumber:description:`](./nsassertionhandler/handlefailureinmethod_object_file_linenumber_description_.md) on the assertion handler for the current thread, passing `desc` as the description string and `arg1`, `arg2`, and `arg3` as substitution variables.

This macro should be used only within Objective-C methods.

Assertions are disabled if the preprocessor macro `NS_BLOCK_ASSERTIONS` is defined or the `ENABLE_NS_ASSERTIONS` Xcode build setting is disabled.

> ❗ **Important**:  Do not call functions with side effects in the `condition` parameter of this macro. The `condition` parameter is not evaluated when assertions are disabled, so if you call functions with side effects, those functions may never get called when you build the project in a non-debug configuration.

> **Note**:  Not all release configurations disable assertions by default.

## Parameters

- `condition`: An expression that evaluates to [`true`](../Swift/true.md) or [`false`](../Swift/false.md).
- `desc`: An `NSString` object that contains a `printf`-style string containing an error message describing the failure condition and placeholders for three arguments.
- `arg1`: An argument to be inserted, in place, into `desc`.
- `arg2`: An argument to be inserted, in place, into `desc`.
- `arg3`: An argument to be inserted, in place, into `desc`.

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
- [NSParameterAssert](./nsparameterassert.md)
  Validates the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsassert3)*