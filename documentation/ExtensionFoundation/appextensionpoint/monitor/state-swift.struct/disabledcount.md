# disabledCount

**Framework**: ExtensionFoundation  
**Kind**: property

The number of app extensions that someone disabled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
var disabledCount: Int { get }
```

#### Discussion

A person can disable app extensions to prevent your host app from loading them. This property reflects the number of app extensions someone explicitly disabled.

## See Also

- [var identities: [AppExtensionIdentity]](appextensionpoint/monitor/state-swift.struct/identities.md)
  The set of approved and enabled app extensions.
- [var unapprovedCount: Int](appextensionpoint/monitor/state-swift.struct/unapprovedcount.md)
  The number of identity entries that someone hasn’t yet enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.struct/disabledcount)*