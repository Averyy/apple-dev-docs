# Recording a Wi-Fi Packet Trace

**Framework**: Network

Record traces of Wi-Fi traffic and traffic management.

#### Overview

When working with Wi-Fi, your best option for recording a packet trace depends on whether you’re interested in the network traffic itself, or in the details of how the Wi-Fi network manages traffic.

##### Record a High Level Packet Trace of Wi Fi Traffic

If you’re primarily interested in the traffic going over the Wi-Fi — that is, you would like to ignore all the low-level details of Wi-Fi and treat the Wi-Fi network like an Ethernet network without all those pesky wires — use one of the following high-level approaches:

- If possible, run the packet trace on one of the machines involved in the communication — including using RVI to record an iOS packet trace. That’s the easiest solution. See [`Recording a Packet Trace`](recording-a-packet-trace.md) for instructions.
- If your Wi-Fi access point supports bridge mode (notably, all Apple base stations do), you can bridge the Wi-Fi network on to an Ethernet network and then use standard Ethernet techniques to capture a packet trace. You won’t be able to see Wi-Fi to Wi-Fi traffic, but in many situations that’s not a problem.
- If you enable Internet Sharing on your Mac, and have your Wi-Fi clients join the shared network, you can run your packet trace program on the Mac and see all the Wi-Fi traffic. If you target the Mac’s Wi-Fi interface, you will see all traffic, including Wi-Fi to Wi-Fi traffic. If you target the Mac’s Ethernet interface, you will only see traffic entering or leaving the Wi-Fi network.

##### Record Low Level Details of Wi Fi Traffic Management

If you are interested in the low-level details of how the Wi-Fi network manages traffic, record a low-level Wi-Fi packet trace. To do this:

1. Choose a Mac on which to record your trace. That Mac cannot use the Wi-Fi interface for normal network traffic while recording the trace.
2. Configure your access point to use a fixed channel. When recording a packet trace, you must specify the channel to record, and having the access point choose its channel automatically makes that harder.
3. Either temporarily turn off the Wi-Fi password on your network or use a separate test network that has no password. If the Wi-Fi network has a password, Wi-Fi encryption makes it harder to examine the trace.
4. Open the Wireless Diagnostics app (you can find this in `/System/Library/CoreServices/Applications/`).
5. Choose Window > Sniffer.
6. In the Sniffer window, select the channel number and width you want to record and click Start.
7. Click Stop when you’re done.
8. In the Finder, navigate to `/var/tmp/` and look for the resulting `.pcap` file.

## See Also

- [Troubleshooting Packet Traces](troubleshooting-packet-traces.md)
  Take action to address packet tracing problems.
- [Submitting a Packet Trace to Apple](submitting-a-packet-trace-to-apple.md)
  Learn the best way to record a packet trace when communicating with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/recording-a-wi-fi-packet-trace)*