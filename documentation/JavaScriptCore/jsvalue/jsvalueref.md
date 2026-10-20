# jsValueRef

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) JSValueRef JSValueRef;
```

#### Discussion

See `JSValueRef` for the C JavaScriptCore API.

## See Also

### Working with the C JavaScriptCore API
- [init!(JSValueRef: JSValueRef!, inContext: JSContext!)](./init%28jsvalueref,incontext%29.md)
  Creates a JavaScript value object from the equivalent C representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/jsvalueref)*