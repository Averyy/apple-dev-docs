# RestrictedSandboxAppliable

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol that browser extensions implement to opt into a more restricted sandbox.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
protocol RestrictedSandboxAppliable
```

## Mentions

- [Limiting resource access in web content extensions](limiting-resource-access-in-content-extensions.md)

#### Overview

Call [`applyRestrictedSandbox(revision:)`](restrictedsandboxappliable/applyrestrictedsandbox(revision:).md) to enter the restricted sandbox, indicating which revision of the sandbox restrictions to apply. In revision 1, corresponding to [`RestrictedSandboxRevision.revision1`](restrictedsandboxrevision/revision1.md), additional restrictions affect the web content extension only. For more information, see [`Limiting resource access in web content extensions`](limiting-resource-access-in-content-extensions.md).

## Topics

### Applying sandbox restrictions
- [func applyRestrictedSandbox(revision: RestrictedSandboxRevision)](restrictedsandboxappliable/applyrestrictedsandbox(revision:).md)
  Puts a browser extension into a more restricted sandbox.
- [enum RestrictedSandboxRevision](restrictedsandboxrevision.md)
  Revisions to the restricted sandbox rules.

## Relationships

### Inherited By
- [NetworkingExtension](networkingextension.md)
- [RenderingExtension](renderingextension.md)
- [WebContentExtension](webcontentextension.md)

## See Also

- [Limiting resource access in web content extensions](limiting-resource-access-in-content-extensions.md)
  Reduce the impact of vulnerabilities in web content extensions by limiting privileges.
- [Accessing files in browser extensions](accessing-files-in-browser-extensions.md)
  Grant extensions access to files from within your browser app.
- [Attributing memory to a content extension](attributing-memory-to-a-content-extension.md)
  Adhere to operating-system limits on GPU memory use.
- [enum RestrictedSandboxRevision](restrictedsandboxrevision.md)
  Revisions to the restricted sandbox rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/restrictedsandboxappliable)*