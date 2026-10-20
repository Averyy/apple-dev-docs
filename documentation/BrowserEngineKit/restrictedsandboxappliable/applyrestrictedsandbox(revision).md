# applyRestrictedSandbox(revision:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Puts a browser extension into a more restricted sandbox.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func applyRestrictedSandbox(revision: RestrictedSandboxRevision)
```

## Mentions

- [Limiting resource access in web content extensions](../limiting-resource-access-in-content-extensions.md)

## Parameters

- `revision`: The revision of the sandbox restriction rules to apply.

## Default Implementations

### RestrictedSandboxAppliable Implementations
- [func applyRestrictedSandbox(revision: RestrictedSandboxRevision)](./applyrestrictedsandbox%28revision%29-6kcga.md)
  When called, the process will enter a restrictive sandbox mode.
- [func applyRestrictedSandbox(revision: RestrictedSandboxRevision)](./applyrestrictedsandbox%28revision%29-7e337.md)
  When called, the process will enter a restrictive sandbox mode.

## See Also

### Applying sandbox restrictions
- [enum RestrictedSandboxRevision](../restrictedsandboxrevision.md)
  Revisions to the restricted sandbox rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/restrictedsandboxappliable/applyrestrictedsandbox(revision:))*