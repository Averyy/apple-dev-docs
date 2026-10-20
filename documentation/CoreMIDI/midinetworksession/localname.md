# localName

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The name of this session’s entity.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var localName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * localName;
```

#### Discussion

The session’s endpoints inherit this value.

## See Also

### Inspecting a Sessions
- [var networkName: String](./networkname.md)
  The name with which this session advertises itself over Bonjour.
- [var networkPort: Int](./networkport.md)
  The session’s UDP port.
- [func sourceEndpoint() -> MIDIEndpointRef](./sourceendpoint%28%29.md)
  Returns the session’s source endpoint.
- [func destinationEndpoint() -> MIDIEndpointRef](./destinationendpoint%28%29.md)
  Returns the session’s destination endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/localname)*