# JSContextGetGlobalContext(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Gets the global context of a JavaScript execution context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSContextGetGlobalContext(_ ctx: JSContextRef!) -> JSGlobalContextRef!
```

#### Return Value

The global context of `ctx`.

## Parameters

- `ctx`: The   with the global context you want to get.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgetglobalcontext(_:))*