# identities

**Framework**: ExtensionFoundation  
**Kind**: property

The set of approved and enabled app extensions.

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
var identities: [AppExtensionIdentity] { get }
```

#### Discussion

Use this property to get the set of app extensions your host app can currently load.

## See Also

- [var disabledCount: Int](appextensionpoint/monitor/state-swift.struct/disabledcount.md)
  The number of app extensions that someone disabled.
- [var unapprovedCount: Int](appextensionpoint/monitor/state-swift.struct/unapprovedcount.md)
  The number of identity entries that someone hasn’t yet enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.struct/identities)*