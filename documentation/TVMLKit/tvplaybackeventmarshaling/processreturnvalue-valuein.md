# processReturnValue(value:in:)

**Framework**: TVMLKit  
**Kind**: method

Converts a JavaScript value into a value that is readable in Swift or Objective-C.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
optional func processReturnValue(value: JSValue, in jsContext: JSContext)
```

## Parameters

- `value`: A JavaScript value returned by the dispatch event.
- `jsContext`: The JavaScript context for the value.

## See Also

- [var properties: [TVPlaybackEventProperty : Any]?](tvplaybackeventmarshaling/properties.md)
  An array of custom playback event properties.
- [struct TVPlaybackEventProperty](tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventmarshaling/processreturnvalue(value:in:))*