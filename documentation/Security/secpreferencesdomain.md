# SecPreferencesDomain

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The keychain preference domains.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecPreferencesDomain
```

```c
enum SecPreferencesDomain : int;
```

## Overview

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. The default preference domain for system daemons (that is, for daemons running in the root session) is the system domain. The default preference domain for all other programs is the user domain. A common preference appears for all users and the system. For example, if you add a keychain to the keychain search list using [`SecPreferencesDomain.common`](./secpreferencesdomain/common.md) for the preference domain, the keychain is added to the search list for all users and the system.

## Topics

### Constants
- [SecPreferencesDomain.user](./secpreferencesdomain/user.md)
  Indicates the user preference domain preferences.
- [SecPreferencesDomain.system](./secpreferencesdomain/system.md)
  Indicates the system or daemon preference domain preferences.
- [SecPreferencesDomain.common](./secpreferencesdomain/common.md)
  Indicates the preferences are common to everyone.
- [SecPreferencesDomain.dynamic](./secpreferencesdomain/dynamic.md)
  Indicates a dynamic search list (typically provided by removable keychains such as smart cards).
### Initializers
- [init?(rawValue: Int32)](./secpreferencesdomain/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpreferencesdomain)*