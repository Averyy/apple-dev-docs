# kMIDINotPermitted

**Framework**: Core MIDI  
**Kind**: var

The process doesn’t have privileges for the requested operation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kMIDINotPermitted: OSStatus { get }
```

## See Also

- [var kMIDIInvalidClient: OSStatus](kmidiinvalidclient.md)
  The client is invalid.
- [var kMIDIInvalidPort: OSStatus](kmidiinvalidport.md)
  The port is invalid.
- [var kMIDIWrongEndpointType: OSStatus](kmidiwrongendpointtype.md)
  A function received a source endpoint when it required a destination endpoint, or vice versa.
- [var kMIDINoConnection: OSStatus](kmidinoconnection.md)
  The connection you’re trying to close doesn’t exist.
- [var kMIDIUnknownEndpoint: OSStatus](kmidiunknownendpoint.md)
  The system doesn’t recognize the endpoint.
- [var kMIDIUnknownProperty: OSStatus](kmidiunknownproperty.md)
  The property you’re trying to query isn’t set on the object.
- [var kMIDIWrongPropertyType: OSStatus](kmidiwrongpropertytype.md)
  The value you assigned to the property is the wrong type.
- [var kMIDINoCurrentSetup: OSStatus](kmidinocurrentsetup.md)
  A MIDI setup object doesn’t currently exist.
- [var kMIDIMessageSendErr: OSStatus](kmidimessagesenderr.md)
  The communication with the MIDI server failed.
- [var kMIDIServerStartErr: OSStatus](kmidiserverstarterr.md)
  The system can’t start the MIDI server.
- [var kMIDISetupFormatErr: OSStatus](kmidisetupformaterr.md)
  The system can’t read the saved state.
- [var kMIDIWrongThread: OSStatus](kmidiwrongthread.md)
  A driver is calling a non-I/O function in the server from a thread other than the server’s main thread.
- [var kMIDIObjectNotFound: OSStatus](kmidiobjectnotfound.md)
  The requested object doesn’t exist.
- [var kMIDIIDNotUnique: OSStatus](kmidiidnotunique.md)
  The identifier you’re trying to set isn’t unique.
- [var kMIDIUnknownError: OSStatus](kmidiunknownerror.md)
  The system can’t perform the requested operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidinotpermitted)*