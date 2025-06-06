# kAuthorizationRightExecute

**Framework**: Security  
**Kind**: var

The type for an authorization item requesting the right to execute with privileges.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAuthorizationRightExecute: String { get }
```

#### Discussion

In addition to this right, you should obtain whatever rights the tool needs to perform its operation on your behalf. The [`AuthorizationItem`](authorizationitem.md) should contain the full path of the tool you wish to execute in the `value` and `valueLength` fields.  In the future we will limit the right to only execute the requested path, and we will display this information to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kauthorizationrightexecute)*