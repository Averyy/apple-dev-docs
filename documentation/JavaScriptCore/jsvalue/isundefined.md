# isUndefined

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL isUndefined;
```

## Discussion

The JavaScript `undefined` value is used for variables that have not yet been assigned a value, for formal parameters in functions for which no actual parameter has been passed, and as the result of expressions or function calls that do not explicitly return a value. Note that `undefined` is not the same as `null`.

## See Also

### Determining the Type of a JavaScript Value
- [var isNull: Bool](./isnull.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `null` value.
- [var isBoolean: Bool](./isboolean.md)
  A Boolean value that indicates whether the instance is a JavaScript Boolean value.
- [var isNumber: Bool](./isnumber.md)
  A Boolean value that indicates whether the instance is a JavaScript numeric value.
- [var isString: Bool](./isstring.md)
  A Boolean value that indicates whether the instance is a JavaScript `String` object.
- [var isObject: Bool](./isobject.md)
  A Boolean value that indicates whether the instance is a JavaScript object.
- [var isArray: Bool](./isarray.md)
  A Boolean value that indicates whether the instance is a JavaScript array value.
- [var isDate: Bool](./isdate.md)
  A Boolean value that indicates whether the instance is a JavaScript `Date` object.
- [var isSymbol: Bool](./issymbol.md)
  A Boolean value that indicates whether the instance is a symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isundefined)*