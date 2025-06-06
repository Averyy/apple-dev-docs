# nodeID

**Framework**: Matter  
**Kind**: property

Node id for this controller.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
@NSCopying
var nodeID: NSNumber? { get set }
```

#### Discussion

If operationalCertificate is not nil, must be nil.  The provided operational certificate will be used as-is.

If not nil, must be a valid Matter operational node id.

If operationalCertificate is nil, nodeID and operationalKeypair are used to determine an operational certificate, as follows:

- When creating a new fabric:

** nodeID is allowed to be nil to indicate that a random node id should be generated.

- When using an existing fabric:

** nodeID is allowed to be nil to indicate that the existing operational node id should be used.  The existing operational keys will also be used, unless operationalKeypair is provided.  The existing caseAuthenticatedTags will be used.

** If nodeID is not nil, a new operational certificate will be generated for the provided node id (even if that matches the existing node id), using either the operationalKeypair if that is provided or a new randomly generated operational key, and using the provided caseAuthenticatedTags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstartupparams/nodeid-9iwwv)*