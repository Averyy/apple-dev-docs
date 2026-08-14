# AEAssessmentBinaryExecutable

**Framework**: Automatic Assessment Configuration  
**Kind**: class

A non-bundled, non-UI executable (e.g. a launchd daemon) designated as an assessment participant by its on-disk path.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
class AEAssessmentBinaryExecutable
```

#### Overview

Use this for a participant that has no bundle identifier and so cannot be expressed as an [`AEAssessmentApplication`](aeassessmentapplication.md). It feeds only the app-launch allowlist under [`allowsOnlyParticipantsToRun`](aeassessmentconfiguration/allowsonlyparticipantstorun.md) and, when its configuration permits, network access; UI policies (frontmost app, window server, media, menu bar) do not apply.

Matching is by exact on-disk path. At runtime the executable must also satisfy [`requiresSignatureValidation`](aeassessmentbinaryexecutable/requiressignaturevalidation.md) (and the team identifier, if set), so a swapped or re-signed binary is not silently trusted. Leave [`requiresSignatureValidation`](aeassessmentbinaryexecutable/requiressignaturevalidation.md) enabled (the default) unless the executable is unsigned.

> **Note**: [`AEAssessmentApplication`](aeassessmentapplication.md) for bundled participants.

## Topics

### Initializers
- [init(binaryExecutableURL: URL)](aeassessmentbinaryexecutable/init(binaryexecutableurl:).md)
- [init(binaryExecutableURL: URL, teamIdentifier: String?)](aeassessmentbinaryexecutable/init(binaryexecutableurl:teamidentifier:).md)
### Instance Properties
- [var binaryExecutableURL: URL](aeassessmentbinaryexecutable/binaryexecutableurl.md)
  On-disk path of the executable.
- [var requiresSignatureValidation: Bool](aeassessmentbinaryexecutable/requiressignaturevalidation.md)
  Whether the running executable’s code signature is validated. Defaults to `YES`.
- [var teamIdentifier: String?](aeassessmentbinaryexecutable/teamidentifier.md)
  Team identifier the running executable’s signature must match, or `nil` to skip the team check.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutable)*