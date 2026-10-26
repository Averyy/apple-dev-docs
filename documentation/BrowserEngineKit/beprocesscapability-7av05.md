# BEProcessCapability

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

Capabilities of a helper extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
@interface BEProcessCapability : NSObject
```

## Topics

### Requesting a capability
- [- requestWithError:](./beprocesscapability-7av05/requestwitherror_.md)
  Requests a capability for the current process.
### Granting capabilities to browser extension processes
- [+ background](./beprocesscapability-7av05/background.md)
  A capability that enables an extension process to work in the background.
- [+ foreground](./beprocesscapability-7av05/foreground.md)
  A capability that enables an extension process to do foreground priority work.
- [+ mediaPlaybackAndCaptureWithEnvironment:](./beprocesscapability-7av05/mediaplaybackandcapturewithenvironment_.md)
  A capability that enables an extension process to access hardware that media capture and playback require.
- [+ suspended](./beprocesscapability-7av05/suspended.md)
  A capability that enables an extension process to stay in a suspended state.
### Instance Methods
- [- activateWithError:](./beprocesscapability-7av05/activatewitherror_.md)
  Activates the capability.
- [- suspendWithError:](./beprocesscapability-7av05/suspendwitherror_.md)
  Suspends the capability.
### Type Methods
- [+ screenCaptureWithEnvironment:](./beprocesscapability-7av05/screencapturewithenvironment_.md)
  The helper extension process may capture the contents of the screen.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Extension capabilities
- [BEMediaEnvironment](./bemediaenvironment-n91a.md)
  An object that identifies a media playback or streaming environment.
- [BEProcessCapabilityGrant](./beprocesscapabilitygrant.md)
  An object that represents a granted capability.
- [class BEWebContentFilter](./bewebcontentfilter.md)
  An object that represents a web content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapability-7av05)*