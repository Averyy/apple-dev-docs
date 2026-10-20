# expectsReturnValue

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the custom event expects to contain a return value.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var expectsReturnValue: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL expectsReturnValue;
```

## See Also

### Creating User Info for Custom Playback Events
- [init(properties: [TVPlaybackEventProperty : Any]?, expectsReturnValue: Bool)](./init%28properties,expectsreturnvalue%29.md)
  Create a new custom playback event user info dictionary.
- [struct TVPlaybackEventProperty](../tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.
- [var returnValue: Any?](./returnvalue.md)
  The return value type for the custom event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackcustomeventuserinfo/expectsreturnvalue)*