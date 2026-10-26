# NS_VOIDRETURN

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

Permits program control to exit from an exception-handling domain.

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
#define NS_VOIDRETURN
```

#### Discussion

The `NS_VOIDRETURN` macro returns program control to the caller out of the exception-handling domain—that is, a section of code between the [`NS_DURING`](./ns_during.md) and [`NS_HANDLER`](./ns_handler.md) macros that might raise an exception. The standard `return` statement does not work as expected in the exception-handling domain.

## See Also

### Legacy Macros
- [NS_DURING](./ns_during.md)
  Marks the start of the exception-handling domain.
- [NS_ENDHANDLER](./ns_endhandler.md)
  Marks the end of the local event handler.
- [NS_HANDLER](./ns_handler.md)
  Marks the end of the exception-handling domain and the start of the local exception handler.
- [NS_VALUERETURN](./ns_valuereturn.md)
  Permits program control to exit from an exception-handling domain with a value of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/ns_voidreturn)*