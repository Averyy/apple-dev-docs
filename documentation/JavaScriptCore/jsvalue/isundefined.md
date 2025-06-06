# isUndefined

**Framework**: JavaScriptCore  
**Kind**: property

A Boolean value that indicates whether the instance corresponds to the JavaScript `undefined` value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isUndefined: Bool { get }
```

#### Discussion

The JavaScript `undefined` value is used for variables that have not yet been assigned a value, for formal parameters in functions for which no actual parameter has been passed, and as the result of expressions or function calls that do not explicitly return a value. Note that `undefined` is not the same as `null`.

## See Also

- [var isNull: Bool](jsvalue/isnull.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `null` value.
- [var isBoolean: Bool](jsvalue/isboolean.md)
  A Boolean value that indicates whether the instance is a JavaScript Boolean value.
- [var isNumber: Bool](jsvalue/isnumber.md)
  A Boolean value that indicates whether the instance is a JavaScript numeric value.
- [var isString: Bool](jsvalue/isstring.md)
  A Boolean value that indicates whether the instance is a JavaScript `String` object.
- [var isObject: Bool](jsvalue/isobject.md)
  A Boolean value that indicates whether the instance is a JavaScript object.
- [var isArray: Bool](jsvalue/isarray.md)
  A Boolean value that indicates whether the instance is a JavaScript array value.
- [var isDate: Bool](jsvalue/isdate.md)
  A Boolean value that indicates whether the instance is a JavaScript `Date` object.
- [var isSymbol: Bool](jsvalue/issymbol.md)
  A Boolean value that indicates whether the instance is a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isundefined)*