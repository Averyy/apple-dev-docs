# TVPlaybackEventProperty

**Framework**: TVMLKit  
**Kind**: struct  
**Role**: Structure

Extend this structure to create your own custom playback event properties.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
struct TVPlaybackEventProperty
```

```c
typedef NSString * TVPlaybackEventProperty;
```

## Topics

### Initializers
- [init(String)](./tvplaybackeventproperty/init%28_%29.md)
- [init(rawValue: String)](./tvplaybackeventproperty/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating User Info for Custom Playback Events
- [init(properties: [TVPlaybackEventProperty : Any]?, expectsReturnValue: Bool)](./tvplaybackcustomeventuserinfo/init%28properties,expectsreturnvalue%29.md)
  Create a new custom playback event user info dictionary.
- [var expectsReturnValue: Bool](./tvplaybackcustomeventuserinfo/expectsreturnvalue.md)
  A Boolean value that indicates whether the custom event expects to contain a return value.
- [var returnValue: Any?](./tvplaybackcustomeventuserinfo/returnvalue.md)
  The return value type for the custom event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventproperty)*