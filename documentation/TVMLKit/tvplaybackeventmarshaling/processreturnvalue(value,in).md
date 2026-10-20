# processReturnValue(value:in:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Converts a JavaScript value into a value that is readable in Swift or Objective-C.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func processReturnValue(value: JSValue, in jsContext: JSContext)
```

```objc
- (void) processReturnJSValue:(JSValue *) value inContext:(JSContext *) jsContext;
```

## Parameters

- `value`: A JavaScript value returned by the dispatch event.
- `jsContext`: The JavaScript context for the value.

## See Also

### Processing Playback Events
- [var properties: [TVPlaybackEventProperty : Any]?](./properties.md)
  An array of custom playback event properties.
- [struct TVPlaybackEventProperty](../tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventmarshaling/processreturnvalue(value:in:))*