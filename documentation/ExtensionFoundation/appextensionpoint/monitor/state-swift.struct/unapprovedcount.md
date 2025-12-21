# unapprovedCount

**Framework**: ExtensionFoundation  
**Kind**: property

The number of identity entries that someone hasn’t yet enabled.

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
var unapprovedCount: Int { get }
```

#### Discussion

For app extensions that reside outside the host app, a person must approve the use of an app extension before the host app can use it. This property reflects the number of app extensions currently waiting for approval. If the value of this property is greater than zero, consider presenting [`EXAppExtensionBrowserViewController`](https://developer.apple.com/documentation/ExtensionKit/EXAppExtensionBrowserViewController) to display the extension enablement UI.

## See Also

- [var identities: [AppExtensionIdentity]](appextensionpoint/monitor/state-swift.struct/identities.md)
  The set of approved and enabled app extensions.
- [var disabledCount: Int](appextensionpoint/monitor/state-swift.struct/disabledcount.md)
  The number of app extensions that someone disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.struct/unapprovedcount)*