# evaluationError

**Framework**: Foundation  
**Kind**: property

Returns the object specifier in which an evaluation error occurred.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var evaluationError: NSScriptObjectSpecifier? { get }
```

#### Return Value

The object specifier in which an evaluation error occurred.

#### Discussion

The object specifier failing to evaluate could be the receiver or any container specifier “above” the receiver.

## See Also

- [var evaluationErrorNumber: Int](nsscriptobjectspecifier/evaluationerrornumber.md)
  Sets the value of the evaluation error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/evaluationerror)*