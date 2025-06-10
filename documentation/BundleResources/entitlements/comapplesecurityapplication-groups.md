# App Groups Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A list of identifiers specifying the groups your app belongs to.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- macOS 10.7+
- tvOS 9.0+
- watchOS 2.0+

#### Discussion

App groups allow multiple apps produced by a single development team to access shared containers and keychain access groups, and communicate using interprocess communication (IPC). Apps may belong to one or more app groups.

Format the identifier as follows:

```console
group.<group name>
```

Apple ensures that the group name you choose is unique when you register the app group on the Apple Developer website. For more information, see [`Register an app group`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-identifiers/register-an-app-group).

In macOS, you can also create app groups or add apps to existing app groups using this identifier format:

```console
<team identifier>.<group name>
```

You don’t need to register app groups that use this format on the Apple Developer website.

Apps within an app group share access to a group container. For more information about container creation, location, and deletion, see [`containerURL(forSecurityApplicationGroupIdentifier:)`](https://developer.apple.com/documentation/Foundation/FileManager/containerURL(forSecurityApplicationGroupIdentifier:)).

Apps within a group can communicate with other members in the group using IPC mechanisms including Mach IPC, XPC, POSIX semaphores and shared memory, and UNIX domain sockets. In macOS, use app groups to enable IPC communication between two sandboxed apps, or between a sandboxed app and a nonsandboxed app. You use the app group identifier in the service identifier for your IPC mechanism, so keep these restrictions in mind when creating your app group identifier:

| IPC mechanism | Requirements |
| --- | --- |
| Mach IPC, XPC | The service name has the format `<group identifier>.<unique name>`. The maximum length of the service name is `BOOTSTRAP_MAX_NAME_LEN` characters. |
| POSIX semaphores | The service identifer has the format `<group identifier>/<unique name>`. The maximum length of the service identifier is `PSEMNAMLEN` characters. |
| POSIX shared memory | The service identifer has the format `<group identifier>/<unique name>`. The maximum length of the service identifier is `PSHMNAMLEN` characters. |
| UNIX domain sockets | The path to the socket needs to be in your app group container, and the name of the socket is limited to `SOCK_MAXADDRLEN` characters, which includes two bytes that are reserved for `sun_len` and `sun_family`. |

App groups that you register in your Apple Developer profile also act as keychain access groups. For more information about the relationship between app groups and keychain access groups, see [`Sharing access to keychain items among a collection of apps`](https://developer.apple.com/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps).

To add this entitlement to your app, enable the App Groups capability in Xcode, and add the groups your app belongs to.

## See Also

- [Keychain Access Groups Entitlement](entitlements/keychain-access-groups.md)
  The identifiers for the keychain groups that the app may share items with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.application-groups)*