# JSContextGetGroup(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Gets the context group that a JavaScript execution context belongs to.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSContextGetGroup(_ ctx: JSContextRef!) -> JSContextGroupRef!
```

#### Return Value

The group that `ctx` belongs to.

## Parameters

- `ctx`: The   with the group you want to get.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontextgetgroup(_:))*