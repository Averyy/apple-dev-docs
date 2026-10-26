# BEMediaEnvironment

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An object that identifies a media playback or streaming environment.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```objc
@interface BEMediaEnvironment : NSObject
```

## Topics

### Managing media life cycle
- [- initWithWebPageURL:](./bemediaenvironment-n91a/initwithwebpageurl_.md)
  Creates a new media playback environment identified for a webpage URL.
- [- initWithXPCRepresentation:error:](./bemediaenvironment-n91a/initwithxpcrepresentation_error_.md)
  Creates a media session from an XPC object.
- [- activateWithError:](./bemediaenvironment-n91a/activatewitherror_.md)
  Activates the media environment.
- [- suspendWithError:](./bemediaenvironment-n91a/suspendwitherror_.md)
  Suspends the media environment.
### Creating capture sessions
- [- makeCaptureSessionWithError:](./bemediaenvironment-n91a/makecapturesessionwitherror_.md)
  Creates a new capture session in this media environment.
### Sharing references through XPC
- [- createXPCRepresentation](./bemediaenvironment-n91a/createxpcrepresentation.md)
  Creates an XPC object that represents the media environment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Extension capabilities
- [BEProcessCapability](./beprocesscapability-7av05.md)
  Capabilities of a helper extension process.
- [BEProcessCapabilityGrant](./beprocesscapabilitygrant.md)
  An object that represents a granted capability.
- [class BEWebContentFilter](./bewebcontentfilter.md)
  An object that represents a web content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bemediaenvironment-n91a)*