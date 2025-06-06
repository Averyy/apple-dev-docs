# Hosting Guest Code

**Framework**: Security

Securely launch and manage plug-ins and other executable entities, known as guest code, from within your app acting as a host.

#### Overview

The functions in this section are called only by code that is hosting guests. In the context of code signing, a host is code that creates, launches, and manages other code—its guests. A host must do this without compromising its own integrity. As part of that duty, it maintains state for each of its guests and answers questions about them.

In general, a host is responsible for defending itself against its guests. That is, a host is generally assumed to have a separate code identity from its guests and must prevent its guests from altering its internal data structures or otherwise altering the host code. However, a host can declare itself to be a dedicated host, in which case its only function is to run its specified dedicated guest. In that case, the system treats the host and its guest as a single code entity and the host does not have to defend itself from its guest. For more information on dedicated hosts, see [`kSecCSDedicatedHost`](kseccsdedicatedhost.md).

Both hosts and guests are represented by code objects—that is, by objects of type [`SecCode`](seccode.md). Within the hosting API, guests are identified by simple numeric handles that are unique and valid only in the context of their specific host.

The functions in this section always apply to the code host making the calls. They cannot be used to directly interrogate another host.

In order to be considered a code host by [`Code Signing Services`](code-signing-services.md), code must call either the [`SecHostCreateGuest`](sechostcreateguest.md) function or the [`SecHostSetHostingPort`](sechostsethostingport.md) function. Code that calls the [`SecHostCreateGuest`](sechostcreateguest.md) function is considered to be acting in proxy hosting mode. Code that calls the [`SecHostSetHostingPort`](sechostsethostingport.md) function is considered to be acting in dynamic hosting mode.

In proxy hosting mode, the host provides information about its guests when it creates or loads them, when it removes them, and when it changes their status. [`Code Signing Services`](code-signing-services.md) caches this information and answers queries about guests from this pool of information. The host is not directly involved in answering such queries, and has no way to intervene.

In dynamic hosting mode, the host provides a Mach port that receives direct queries about its guests. The host then responds directly to questions about its guests.

Once this mode is set, there is no way to switch to the other mode, and any call to a function that belongs to the wrong mode fails. However, from the point of view of services requesting information about guest code, there is no distinction between guests hosted by proxy and those hosted dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/hosting-guest-code)*