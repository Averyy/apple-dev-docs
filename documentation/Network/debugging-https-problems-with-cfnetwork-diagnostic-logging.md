# Debugging HTTPS Problems with CFNetwork Diagnostic Logging

**Framework**: Network

Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.

#### Overview

If you’re using [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and need to debug a complex networking issue, you can enable CFNetwork diagnostic logging to get detailed information about the progress of your network requests. CFNetwork diagnostic logging has unique advantages relative to other network debugging tools, including:

- Minimal setup
- The ability to look at network traffic that’s protected by Transport Layer Security (TLS)
- Information about CFNetwork’s internal state, like which cookies get saved and applied

For information about other network debugging tools, see [`Choosing a Network Debugging Tool`](choosing-a-network-debugging-tool.md).

> **Note**:  Xcode 13 includes the HTTP Tracing instrument to aid in debugging HTTP issues. See [`Analyzing HTTP traffic with Instruments`](https://developer.apple.com/documentation/Foundation/analyzing-http-traffic-with-instruments).

 Xcode 13 includes the HTTP Tracing instrument to aid in debugging HTTP issues. See [`Analyzing HTTP traffic with Instruments`](https://developer.apple.com/documentation/Foundation/analyzing-http-traffic-with-instruments).

##### Understand the Security Implications

CFNetwork diagnostic logs may contain decrypted TLS data and other security-sensitive information. Take these precautions:

- Restrict access to any logs you capture.
- If you build an app that enables this logging programmatically, make sure that anyone who receives that app understands the security implications of using it.
- If you send a log to Apple, redact any security-sensitive information.

> ❗ **Important**:  CFNetwork diagnostic logs may contain information that’s  security-sensitive. Protect these logs accordingly.

 CFNetwork diagnostic logs may contain information that’s  security-sensitive. Protect these logs accordingly.

##### Enable Logging in Xcode

To enable CFNetwork diagnostic logging, edit the current scheme (choose Product > Scheme > Edit Scheme), navigate to the Arguments tab, and add a `CFNETWORK_DIAGNOSTICS` item to the Environment Variables list. The value of this item can range from 0 to 3, where 0 turns logging off, and higher numbers give you progressively more logging. When you next run your app and use [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), CFNetwork diagnostic log entries appear in Xcode’s debug console area. If the console area isn’t visible, choose View > Debug Area > Show Debug Area to show it.

##### Enable Logging Programmatically to See Problems Outside of Xcode

To investigate problems outside of Xcode, programmatically enable CFNetwork diagnostic logging by setting the environment variable directly.

```objc
setenv("CFNETWORK_DIAGNOSTICS", "3", 1);
```

Do this right at the beginning of the app’s launch sequence:

- If you’re programming in Objective-C, put the code at the start of your `main` function.
- If your program has a C++ component, make sure this code runs before any C++ static initializers that use CFNetwork or any APIs, like [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), that use CFNetwork.
- If you’re programming in Swift, put this code in `main.swift`.

> **Note**:  By default, Swift apps don’t have a `main.swift`; [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) explains how to add one.

 By default, Swift apps don’t have a `main.swift`; [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) explains how to add one.

##### View Log Entries

How you view the resulting log entries depends on your specific situation:

- In macOS, if you can reproduce the problem locally, run the Console utility on your Mac and view log entries there.
- In iOS, if you can reproduce the problem locally, and you’re able to connect the device to your Mac through USB, run the Console utility on your Mac and view log entries there. Make sure you select your iOS device from the source list on the left of the main Console window (choose View > Show Sources if the source list isn’t visible).
- If neither of the above work for you — for example, if you’re trying to debug a problem that can only be reproduced by one of your users in the field — get a sysdiagnose log from the machine exhibiting the problem and then extract the log entries from that. See the [`Bug Reporting > Profiles and Logs`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/) page on the developer website for details on how to get a sysdiagnose log.

## See Also

- [Choosing a Network Debugging Tool](choosing-a-network-debugging-tool.md)
  Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](debugging-http-server-side-errors.md)
  Understand HTTP server-side errors and how to debug them.
- [Recording a Packet Trace](recording-a-packet-trace.md)
  Learn how to record a low-level trace of network traffic.
- [Taking Advantage of Third-Party Network Debugging Tools](taking-advantage-of-third-party-network-debugging-tools.md)
  Learn about the available third-party network debugging tools.
- [Testing and Debugging L4S in Your App](testing-and-debugging-l4s-in-your-app.md)
  Learn how to verify your app on an L4S-capable host and network to improve your app’s responsiveness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging)*