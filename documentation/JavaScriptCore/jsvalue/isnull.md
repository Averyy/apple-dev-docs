# isNull

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the instance corresponds to the JavaScript `null` value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isNull: Bool { get }
```

```objc
@property (readonly) BOOL isNull;
```

#### Discussion

The JavaScript `null` value is used only in cases where an actual value is expected but none is applicable. Note that `null` is not the same as `undefined`.

## See Also

### Determining the Type of a JavaScript Value
- [var isUndefined: Bool](./isundefined.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `undefined` value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/isnull)*