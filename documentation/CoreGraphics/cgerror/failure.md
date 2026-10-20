# CGError.failure

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

A general failure occurred.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case failure
```

```c
kCGErrorFailure
```

## See Also

### Constants
- [CGError.cannotComplete](./cannotcomplete.md)
  The requested operation is inappropriate for the parameters passed in, or the current system state.
- [CGError.illegalArgument](./illegalargument.md)
  One or more of the parameters passed to a function are invalid. Check for `NULL` pointers.
- [CGError.invalidConnection](./invalidconnection.md)
  The parameter representing a connection to the window server is invalid.
- [CGError.invalidContext](./invalidcontext.md)
  The `CPSProcessSerNum` or context identifier parameter is not valid.
- [CGError.invalidOperation](./invalidoperation.md)
  The requested operation is not valid for the parameters passed in, or the current system state.
- [CGError.noneAvailable](./noneavailable.md)
  The requested operation could not be completed as the indicated resources were not found.
- [CGError.notImplemented](./notimplemented.md)
  Return value from obsolete function stubs present for binary compatibility, but not typically called.
- [CGError.rangeCheck](./rangecheck.md)
  A parameter passed in has a value that is inappropriate, or which does not map to a useful operation or value.
- [CGError.success](./success.md)
  The requested operation was completed successfully.
- [CGError.typeCheck](./typecheck.md)
  A data type or token was encountered that did not match the expected type or token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgerror/failure)*