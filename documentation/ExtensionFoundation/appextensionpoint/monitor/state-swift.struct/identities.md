# identities

**Framework**: ExtensionFoundation  
**Kind**: property  
**Role**: Instance Property

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

### Getting the app extension status
- [var disabledCount: Int](./disabledcount.md)
  The number of app extensions that someone disabled.
- [var unapprovedCount: Int](./unapprovedcount.md)
  The number of identity entries that someone hasn’t yet enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.struct/identities)*