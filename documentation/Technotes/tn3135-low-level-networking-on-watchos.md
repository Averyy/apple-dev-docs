# TN3135: Low-level networking on watchOS

**Framework**: Technotes

Learn about the supported use cases for low-level networking on watchOS.

#### Overview

watchOS groups networking into two categories:

- High-level networking.  This includes the HTTP and HTTPS support in [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession), and any code layered on top of that.
- Low-level networking.  This includes [`Network`](https://developer.apple.com/documentation/network) framework, [`Stream`](https://developer.apple.com/documentation/foundation/stream), and any other API that runs a TCP connection or UDP session directly.  That includes the low-level aspects of [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession), namely [`URLSessionStreamTask`](https://developer.apple.com/documentation/foundation/urlsessionstreamtask) and [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask).   It also includes APIs, like [`NWBrowser`](https://developer.apple.com/documentation/network/nwbrowser) and [`NetService`](https://developer.apple.com/documentation/foundation/netservice), that interact directly with Bonjour.

watchOS allows all apps to use high-level networking equally.  However, it only allows an app to use low-level networking under specific circumstances:

- It allows an audio streaming app to use low-level networking while actively streaming audio.  Support for this was introduced in watchOS 6.
- It allows a VoIP app to use low-level networking while running a call using [`CallKit`](https://developer.apple.com/documentation/callkit).  Support for this was added in watchOS 9.
- It allows an app on watchOS to set up an application service listener so that the same app on tvOS can establish a low-level connection to it using the [`DeviceDiscoveryUI`](https://developer.apple.comhttps://developer.apple.com/documentation/devicediscoveryui) framework.  Support for this was added in watchOS 9 and tvOS 16.

watchOS blocks low-level networking outside of these specific circumstances.  For example, if a normal app attempts to start an [`NWConnection`](https://developer.apple.com/documentation/network/nwconnection), that connection will stay in the [`NWConnection.State.waiting(_:)`](https://developer.apple.com/documentation/network/nwconnection/state-swift.enum/waiting(_:)) state with an error of `ENETDOWN`.  Similarly, an [`NWPathMonitor`](https://developer.apple.com/documentation/network/nwpathmonitor) will remain in the [`NWPath.Status.unsatisfied`](https://developer.apple.com/documentation/network/nwpath/status-swift.enum/unsatisfied) state.

> ❗ **Important**: watchOS versions 6 through 8 had a bug where low-level networking might work outside of these circumstances (r. 83682211).  That bug has been fixed in watchOS 9, which correctly enforces the rules described above.

The BSD sockets API doesn’t work for networking on watchOS under any circumstances.  Use Network framework instead.

Foundation has various APIs for synchronously creating a value using bytes loaded from a URL.  For example, [`init(contentsOf:options:)`](https://developer.apple.com/documentation/foundation/data/init(contentsof:options:)) creates a data value in this way.  Using these APIs with network URLs is not best practice on any Apple platform and is not supported by watchOS.  Instead, load network URLs with a dedicated asynchronous networking API, like [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession).

When writing watchOS networking code, test it on a real device; the simulator always allows low-level networking.

Also, test your networking code in a wide variety of network environments.  Specifically, test it when the paired iPhone is available *and* when the paired iPhone is not available.  The best way to test the latter is to turn off both Wi-Fi and Bluetooth in the Settings app on the iPhone.  Do not use Control Center for this.  For an explanation of the difference between these two mechanisms, see [`Use Bluetooth and Wi-Fi in Control Center`](https://developer.apple.comhttps://support.apple.com/HT208086).

For more information about building an audio streaming app for watchOS, see WWDC 2019 Session 716 [`Streaming Audio on watchOS 6`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/716/).

#### Revision History

- **2026-07-16** Fixed a broken link.
- **2024-02-27** Fixed a typo.
- **2022-10-18** Added a discussion of the DeviceDiscoveryUI framework.
- **2022-09-27** Republished as TN3135.  Updated with information about watchOS 9.  Made significant editorial changes.
- **2021-05-14** Updated to call out that [`URLSessionStreamTask`](https://developer.apple.com/documentation/foundation/urlsessionstreamtask) and [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask) are considered low-level networking.
- **2019-12-18** First published as “Low-Level Networking on watchOS” on Apple Developer Forums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3135-low-level-networking-on-watchos)*