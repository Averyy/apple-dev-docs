# jsGlobalContextRef

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

Returns the C representation of the JavaScript context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var jsGlobalContextRef: JSGlobalContextRef! { get }
```

```objc
@property (readonly) JSGlobalContextRef JSGlobalContextRef;
```

## Discussion

See `JSContextRef` for the C JavaScriptCore API.

## See Also

### Working with the C JavaScriptCore API
- [init!(JSGlobalContextRef: JSGlobalContextRef!)](./init%28jsglobalcontextref%29-9m51.md)
  Creates a JavaScript context object from the equivalent C representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/jsglobalcontextref)*