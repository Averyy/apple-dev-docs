# Taking Advantage of Third-Party Network Debugging Tools

**Framework**: Network

Learn about the available third-party network debugging tools.

#### Overview

iOS and macOS have built-in network debugging tools (see [`Analyzing HTTP traffic with Instruments`](https://developer.apple.com/documentation/Foundation/analyzing-http-traffic-with-instruments) and [`Choosing a Network Debugging Tool`](choosing-a-network-debugging-tool.md)), but you may also want to take advantage of the third-party tools discussed here.

> ❗ **Important**:  Information about products not manufactured by Apple is provided without recommendation or endorsement. Apple assumes no responsibility with regard to the selection, performance, or use of third-party products. [`Contact the vendor`](https://developer.apple.comhttps://support.apple.com/en-us/HT201777) for additional information. Other company and product names may be trademarks of their respective owners.

##### Debugging Http Proxies

- **[`Charles HTTP Proxy`](https://developer.apple.comhttps://www.charlesproxy.com/)**: A debugging HTTP proxy that enables a developer to view all of the HTTP and HTTPS traffic between their machine and the internet.
- **[`mitmproxy`](https://developer.apple.comhttps://mitmproxy.org/)**: A free and open source interactive debugging HTTP proxy. The name stands for *machine-in-the-middle proxy*.

##### Macos Apps

- **[`Debookee`](https://developer.apple.comhttps://www.iwaxx.com/debookee/)**: A simple and powerful network traffic analyzer for macOS.
- **[`IPNetMonitorX`](https://developer.apple.comhttp://www.sustworks.com/site/prod_ipmx_overview.html)**: A network troubleshooting toolkit for debugging internet service problems and optimizing performance.
- **[`Wireshark`](https://developer.apple.comhttps://www.wireshark.org)**: A free and open source packet analyzer that supports macOS.

##### Command Line Tools

- **[`tcpflow`](https://developer.apple.comhttp://www.circlemud.org/jelson/software/tcpflow/)**: A program that records data transmitted as part of TCP connections (flows), and stores the data in a way that’s convenient for protocol analysis or debugging.
- **[`tcptrace`](https://developer.apple.comhttp://tcptrace.org/)**: An open source tool for analyzing the TCP connections in a packet trace.

## See Also

- [Choosing a Network Debugging Tool](choosing-a-network-debugging-tool.md)
  Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](debugging-http-server-side-errors.md)
  Understand HTTP server-side errors and how to debug them.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](debugging-https-problems-with-cfnetwork-diagnostic-logging.md)
  Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.
- [Recording a Packet Trace](recording-a-packet-trace.md)
  Learn how to record a low-level trace of network traffic.
- [Testing and Debugging L4S in Your App](testing-and-debugging-l4s-in-your-app.md)
  Learn how to verify your app on an L4S-capable host and network to improve your app’s responsiveness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/taking-advantage-of-third-party-network-debugging-tools)*