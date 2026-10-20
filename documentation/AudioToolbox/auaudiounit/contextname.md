# contextName

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Information about the host context in which the audio unit is connected, for display in the audio unit’s view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contextName: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) NSString * contextName;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * contextName;
```

#### Discussion

For example—a host could set “track 3” as the context, so that the audio unit’s view could then display “My audio unit on track 3”.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_ContextName` API.

## See Also

### Providing Data to the Host
- [var musicalContextBlock: AUHostMusicalContextBlock?](./musicalcontextblock.md)
  A callback to the host for musical context information.
- [var transportStateBlock: AUHostTransportStateBlock?](./transportstateblock.md)
  A callback to the host for transport state information.
- [var supportsMPE: Bool](./supportsmpe.md)
  A Boolean value that indicates whether the audio unit supports multi-dimensional polyphonic expression.
- [typealias AUHostMusicalContextBlock](../auhostmusicalcontextblock.md)
  A block through which hosts provide musical tempo, time signature, and beat position.
- [typealias AUHostTransportStateBlock](../auhosttransportstateblock.md)
  A block through which hosts provide information about their transport state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/contextname)*