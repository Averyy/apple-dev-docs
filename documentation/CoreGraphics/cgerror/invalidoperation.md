# CGError.invalidOperation

**Framework**: Core Graphics  
**Kind**: case

The requested operation is not valid for the parameters passed in, or the current system state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case invalidOperation
```

## See Also

- [CGError.cannotComplete](cgerror/cannotcomplete.md)
  The requested operation is inappropriate for the parameters passed in, or the current system state.
- [CGError.failure](cgerror/failure.md)
  A general failure occurred.
- [CGError.illegalArgument](cgerror/illegalargument.md)
  One or more of the parameters passed to a function are invalid. Check for `NULL` pointers.
- [CGError.invalidConnection](cgerror/invalidconnection.md)
  The parameter representing a connection to the window server is invalid.
- [CGError.invalidContext](cgerror/invalidcontext.md)
  The `CPSProcessSerNum` or context identifier parameter is not valid.
- [CGError.noneAvailable](cgerror/noneavailable.md)
  The requested operation could not be completed as the indicated resources were not found.
- [CGError.notImplemented](cgerror/notimplemented.md)
  Return value from obsolete function stubs present for binary compatibility, but not typically called.
- [CGError.rangeCheck](cgerror/rangecheck.md)
  A parameter passed in has a value that is inappropriate, or which does not map to a useful operation or value.
- [CGError.success](cgerror/success.md)
  The requested operation was completed successfully.
- [CGError.typeCheck](cgerror/typecheck.md)
  A data type or token was encountered that did not match the expected type or token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgerror/invalidoperation)*