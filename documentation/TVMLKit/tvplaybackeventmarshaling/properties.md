# properties

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array of custom playback event properties.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var properties: [TVPlaybackEventProperty : Any]? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDictionary<NSString *,id> * properties;
```

## See Also

### Processing Playback Events
- [func processReturnValue(value: JSValue, in: JSContext)](./processreturnvalue%28value,in%29.md)
  Converts a JavaScript value into a value that is readable in Swift or Objective-C.
- [struct TVPlaybackEventProperty](../tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventmarshaling/properties)*