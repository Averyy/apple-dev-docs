# directParameter

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the object that corresponds to the direct parameter of the Apple event from which the receiver derives.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var directParameter: Any? { get set }
```

```objc
@property (retain, nullable) id directParameter;
```

## Discussion

You don’t normally override this method.

## Parameters

- `directParameter`: An object to be set as the direct parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/directparameter)*