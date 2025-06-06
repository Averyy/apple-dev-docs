# JSContextGetGlobalObject(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Gets the global object of a JavaScript execution context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSContextGetGlobalObject(_ ctx: JSContextRef!) -> JSObjectRef!
```

#### Return Value

The global object of `ctx`.

## Parameters

- `ctx`: The   with the global object you want to get.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgetglobalobject(_:))*