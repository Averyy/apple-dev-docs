# RestrictedSandboxRevision

**Framework**: BrowserEngineKit  
**Kind**: enum

Revisions to the restricted sandbox rules.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
enum RestrictedSandboxRevision
```

#### Overview

Design your browser to support the latest revision to the restricted sandbox in all extensions, and opt in to new revisions as they become available.

The [`applyRestrictedSandbox(revision:)`](restrictedsandboxappliable/applyrestrictedsandbox(revision:).md) method of the [`RestrictedSandboxAppliable`](restrictedsandboxappliable.md) protocol takes an argument of this type.

## Topics

### Sandbox restriction revisions
- [RestrictedSandboxRevision.revision1](restrictedsandboxrevision/revision1.md)
  First revision of the restricted sandbox rules.
- [RestrictedSandboxRevision.revision2](restrictedsandboxrevision/revision2.md)
  Second revision of the restricted sandbox rules.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Limiting resource access in web content extensions](limiting-resource-access-in-content-extensions.md)
  Reduce the impact of vulnerabilities in web content extensions by limiting privileges.
- [Accessing files in browser extensions](accessing-files-in-browser-extensions.md)
  Grant extensions access to files from within your browser app.
- [Attributing memory to a content extension](attributing-memory-to-a-content-extension.md)
  Adhere to operating-system limits on GPU memory use.
- [protocol RestrictedSandboxAppliable](restrictedsandboxappliable.md)
  A protocol that browser extensions implement to opt into a more restricted sandbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/restrictedsandboxrevision)*