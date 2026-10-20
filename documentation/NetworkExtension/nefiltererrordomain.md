# NEFilterErrorDomain

**Framework**: Network Extension  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const NEFilterErrorDomain;
```

#### Discussion

Match this constant to the [`domain`](../Foundation/nserror/domain.md) of an [`NSError`](../Foundation/nserror.md) encountered when calling methods on [`NEFilterManager`](./nefiltermanager.md). The [`NEFilterManagerError`](./nefiltermanagererror.md) enumeration defines possible [`code`](../Foundation/nserror/code.md) values for these errors.

## See Also

### Errors
- [enum NEFilterManagerError](./nefiltermanagererror.md)
  Error codes specific to filter managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltererrordomain)*