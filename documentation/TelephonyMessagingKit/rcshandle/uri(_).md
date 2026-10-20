# RCSHandle.uri(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: case  
**Role**: Case

A handle that represents a single recipient or sender, as identified by a URI.

**Availability**:
- iOS 26.0+

## Declaration

```swift
case uri(RCSHandle.URI)
```

#### Discussion

To create a URI handle from a phone number, use the [`phoneNumber(_:)`](./phonenumber%28_%29.md) method. The created URI will use the `tel:` scheme.

## See Also

### Accessing handle values
- [RCSHandle.URI](./uri.md)
  A structure that represents an RCS URI handle.
- [case group(RCSHandle.Group)](./group%28_%29.md)
  A handle that represents a group.
- [RCSHandle.Group](./group.md)
  A structure that represents an RCS group handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcshandle/uri(_:))*