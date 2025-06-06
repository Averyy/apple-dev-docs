# TVPlaybackEventProperty

**Framework**: TVMLKit  
**Kind**: struct

Extend this structure to create your own custom playback event properties.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
struct TVPlaybackEventProperty
```

## Topics

### Initializers
- [init(String)](tvplaybackeventproperty/init(_:).md)
- [init(rawValue: String)](tvplaybackeventproperty/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(properties: [TVPlaybackEventProperty : Any]?, expectsReturnValue: Bool)](tvplaybackcustomeventuserinfo/init(properties:expectsreturnvalue:).md)
  Create a new custom playback event user info dictionary.
- [var expectsReturnValue: Bool](tvplaybackcustomeventuserinfo/expectsreturnvalue.md)
  A Boolean value that indicates whether the custom event expects to contain a return value.
- [var returnValue: Any?](tvplaybackcustomeventuserinfo/returnvalue.md)
  The return value type for the custom event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventproperty)*