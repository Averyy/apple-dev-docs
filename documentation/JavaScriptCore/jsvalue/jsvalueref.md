# jsValueRef

**Framework**: JavaScriptCore  
**Kind**: property

Returns the C representation of the JavaScript value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var jsValueRef: JSValueRef! { get }
```

#### Discussion

See `JSValueRef` for the C JavaScriptCore API.

## See Also

- [init!(JSValueRef: JSValueRef!, inContext: JSContext!)](jsvalue/init(jsvalueref:incontext:).md)
  Creates a JavaScript value object from the equivalent C representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/jsvalueref)*