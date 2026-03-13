# Token

**Framework**: ManagedSettings  
**Kind**: struct

A representation of an activity, such as an app or website, that doesn’t reveal its identity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
struct Token<T>
```

#### Overview

Managed Settings uses a `Token` to preserve user privacy and prevent anyone outside of a Family Sharing group from identifying what apps and websites the family accesses. You can use tokens to restrict and filter device use without accessing personal information.

The ManagedSettings framework provides the following types of tokens:

- **[`ApplicationToken`](applicationtoken.md)**: An opaque representation of a selected app.
- **[`WebDomainToken`](webdomaintoken.md)**: An opaque representation of a selected web domain.
- **[`ActivityCategoryToken`](activitycategorytoken.md)**: An opaque representation of a selected category of activity.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/token)*