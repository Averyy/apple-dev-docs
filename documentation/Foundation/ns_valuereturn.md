# NS_VALUERETURN

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

Permits program control to exit from an exception-handling domain with a value of a specified type.

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
#define NS_VALUERETURN(v, t)
```

#### Discussion

The `NS_VALUERETURN` macro returns program control to the caller out of the exception-handling domain—that is, a section of code between the [`NS_DURING`](./ns_during.md) and [`NS_HANDLER`](./ns_handler.md) macros that might raise an exception. The specified value (of the specified type) is returned to the caller. The standard `return` statement does not work as expected in the exception-handling domain.

## Parameters

- `v`: A value to preserve beyond the exception-handling domain.
- `t`: The type of the value specified in `val`.

## See Also

### Legacy Macros
- [NS_DURING](./ns_during.md)
  Marks the start of the exception-handling domain.
- [NS_ENDHANDLER](./ns_endhandler.md)
  Marks the end of the local event handler.
- [NS_HANDLER](./ns_handler.md)
  Marks the end of the exception-handling domain and the start of the local exception handler.
- [NS_VOIDRETURN](./ns_voidreturn.md)
  Permits program control to exit from an exception-handling domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/ns_valuereturn)*