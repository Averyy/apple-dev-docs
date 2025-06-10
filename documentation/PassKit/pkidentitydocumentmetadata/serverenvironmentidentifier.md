# serverEnvironmentIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An identifier that references the target server environment Apple Pay servers need to connect with to provision the pass.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
var serverEnvironmentIdentifier: String { get set }
```

#### Discussion

If `serverEnvironmentIdentifier` isn’t present, the system uses the default Apply Pay server and returns an empty string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentmetadata/serverenvironmentidentifier)*