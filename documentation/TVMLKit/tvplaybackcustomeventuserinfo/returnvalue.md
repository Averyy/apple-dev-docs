# returnValue

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The return value type for the custom event.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var returnValue: Any? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) id returnValue;
```

## See Also

### Creating User Info for Custom Playback Events
- [init(properties: [TVPlaybackEventProperty : Any]?, expectsReturnValue: Bool)](./init%28properties,expectsreturnvalue%29.md)
  Create a new custom playback event user info dictionary.
- [struct TVPlaybackEventProperty](../tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.
- [var expectsReturnValue: Bool](./expectsreturnvalue.md)
  A Boolean value that indicates whether the custom event expects to contain a return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackcustomeventuserinfo/returnvalue)*