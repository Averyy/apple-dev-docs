# AuthorizationEnvironment

**Framework**: Security  
**Kind**: typealias

An authorization item set designated to hold environment information relevant to authorization decisions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AuthorizationEnvironment = AuthorizationItemSet
```

#### Discussion

The authorization items in the set represent data about the environment, such as user name and other information gathered during evaluation of authorization.

This set is actually an instance of an [`AuthorizationItemSet`](authorizationitemset.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationenvironment)*