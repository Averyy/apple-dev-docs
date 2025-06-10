# NEFilterErrorDomain

**Framework**: Network Extension  
**Kind**: var

The domain for errors resulting from calls to the filter manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
let NEFilterErrorDomain: String
```

#### Discussion

Match this constant to the [`domain`](https://developer.apple.com/documentation/Foundation/NSError/domain) of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) encountered when calling methods on [`NEFilterManager`](nefiltermanager.md). The [`NEFilterManagerError`](nefiltermanagererror.md) enumeration defines possible [`code`](https://developer.apple.com/documentation/Foundation/NSError/code) values for these errors.

## See Also

- [enum NEFilterManagerError](nefiltermanagererror.md)
  Error codes specific to filter managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltererrordomain)*