# AEAssessmentBinaryExecutable

**Framework**: Automatic Assessment Configuration  
**Kind**: class  
**Role**: Class

A non-bundled, non-UI executable (e.g. a launchd daemon) designated as an assessment participant by its on-disk path.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class AEAssessmentBinaryExecutable
```

```objc
@interface AEAssessmentBinaryExecutable : NSObject
```

## Overview

Use this for a participant that has no bundle identifier and so cannot be expressed as an [`AEAssessmentApplication`](./aeassessmentapplication.md). It feeds only the app-launch allowlist under [`allowsOnlyParticipantsToRun`](./aeassessmentconfiguration/allowsonlyparticipantstorun.md) and, when its configuration permits, network access; UI policies do not apply.

Matching is by exact on-disk path. At runtime the executable must also satisfy [`requiresSignatureValidation`](./aeassessmentbinaryexecutable/requiressignaturevalidation.md) (and the team identifier, if set), so a swapped or re-signed binary is not silently trusted.

With [`requiresSignatureValidation`](./aeassessmentbinaryexecutable/requiressignaturevalidation.md) enabled (the default), an unsigned or invalidly signed binary is treated as unavailable: a participant that isn’t [`isRequired`](./aeassessmentbinaryexecutableconfiguration/isrequired.md) is dropped from enforcement, while a required one prevents the assessment session from beginning.

> **See Also**: [`allowsOnlyParticipantsToRun`](./aeassessmentconfiguration/allowsonlyparticipantstorun.md) for why the launch allowlist requires a signature, and [`AEAssessmentApplication`](./aeassessmentapplication.md) for bundled participants.

## Topics

### Initializers
- [init(binaryExecutableURL: URL)](./aeassessmentbinaryexecutable/init%28binaryexecutableurl%29.md)
- [init(binaryExecutableURL: URL, teamIdentifier: String?)](./aeassessmentbinaryexecutable/init%28binaryexecutableurl,teamidentifier%29.md)
### Instance Properties
- [var binaryExecutableURL: URL](./aeassessmentbinaryexecutable/binaryexecutableurl.md)
  On-disk path of the executable.
- [var requiresSignatureValidation: Bool](./aeassessmentbinaryexecutable/requiressignaturevalidation.md)
  Whether the running executable’s code signature is validated. Defaults to `YES`.
- [var teamIdentifier: String?](./aeassessmentbinaryexecutable/teamidentifier.md)
  Team identifier the running executable’s signature must match, or `nil` to skip the team check.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentbinaryexecutable)*