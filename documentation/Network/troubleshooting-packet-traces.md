# Troubleshooting Packet Traces

**Framework**: Network

Take action to address packet tracing problems.

#### Overview

If you’re having problems recording a packet trace, read this document for some troubleshooting tips.

##### Troubleshoot the Remote Virtual Interface Rvi

When you first launch Xcode, it installs the `rvictl` tool. If Terminal is unable to find the tool:

1. Make sure you have the latest version of Xcode installed.
2. Make sure `/usr/bin/` is in your shell search path.

If `rvictl` fails with the message `bootstrap_look_up(): 1102`, make sure that the `com.apple.rpmuxd` daemon is installed and loaded. The following command should print information about the daemon:

```shell
sudo launchctl list com.apple.rpmuxd
```

If the daemon is installed correctly, you should see output like this:

```shell
$ sudo launchctl list com.apple.rpmuxd
{
    "Label" = "com.apple.rpmuxd";
    …
};
```

If the daemon isn’t installed correctly you’ll see this:

```shell
$ sudo launchctl list com.apple.rpmuxd
Could not find service "com.apple.rpmuxd" in domain for system
```

This message can indicate that the daemon is unloaded. You can force it to load as follows:

```shell
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.rpmuxd.plist
```

##### Understand How Your Network Debugging Tool Deals with Local Traffic

Some network debugging tools have problems dealing with traffic to or from the local machine, and some work best with that arrangement. Consult the documentation that comes with your tool for up-to-date information about its limitations.

For example, the `tcpdump` tool may flag the TCP checksum of packets sent by the local machine as bad. This is because of TCP checksum offloading. It’s not a fatal problem, but if the bad checksums bother you, turn off this check by passing the `-K` option to `tcpdump`.

##### Avoid Dropped Packets By Increasing the Recording Buffer Size

If you record all the bytes of each packet, it’s possible to overrun the kernel’s packet recording buffer. In this case, your packet trace tool should report a problem. For example, the `tcpdump` tool prints a summary of how many packets were recorded, filtered, and  when you stop the recording.

```shell
$ sudo tcpdump -i en0 -w trace.pcap
tcpdump: listening on en0, link-type EN10MB (Ethernet), capture size 65535 bytes
^C
94 packets captured
177 packets received by filter
0 packets dropped by kernel
```

If the dropped count is non-zero, increase the packet recording buffer size by passing the `-B` option to `tcpdump`.

> **Note**:  For more information about this and other `tcpdump` options, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

##### Use Promiscuous Mode Effectively

On modern systems it’s generally best to run your packet trace tool on one of the machines involved in the communication you’re investigating. However, in some cases that’s not practical, so you have to run your tool on a different machine entirely. When doing so, be aware of these challenges:

- The target interface must support promiscuous mode, that is, the ability to record packets that aren’t destined for that interface. Most Ethernet interfaces support promiscuous mode. Most Wi-Fi interfaces also support promiscuous mode, but that’s not useful because of network topology restrictions. Other interface types typically don’t support promiscuous mode.
- The network topology must allow the interface to see the packets. Historically, you could ensure this by connecting your machines using a hub. However, hubs are almost unheard of these days: Your DSL gateway might claim to have “an embedded four-port hub”, but actually that’s a switch.
- By default, switches don’t forward all traffic to all ports. If you have a simple switch, there’s no way to override this default. For promiscuous mode to be useful, you’ll need an advanced switch that supports port mirroring, that is, the ability to forward all traffic to a specific port.
- If you’re trying to use promiscuous mode on Wi-Fi, be aware that Wi-Fi access points act like switches, with standard traffic being seen only by the stations involved and the access point. Only a low-level Wi-Fi packet trace can take advantage of Wi-Fi promiscuous mode; see [`Record Low-Level Details of Wi-Fi Traffic Management`](recording-a-wi-fi-packet-trace#Record-Low-Level-Details-of-Wi-Fi-Traffic-Management.md).

##### Get More Hints From the Wireshark Wiki

The [`Wireshark wiki`](https://developer.apple.comhttps://wiki.wireshark.org/) has some useful information about how to set up your packet tracing environment:

- The [`Ethernet Capture Setup`](https://developer.apple.comhttps://wiki.wireshark.org/CaptureSetup/Ethernet) page contains background information on how to set up your network for monitoring.
- The [`Hub Reference`](https://developer.apple.comhttps://wiki.wireshark.org/HubReference) page contains information on various types of hubs.
- The [`Switch Reference`](https://developer.apple.comhttps://wiki.wireshark.org/SwitchReference) page contains information on analysis features, such as port mirroring, found on various models of switches, including links to online documentation for those switches.

## See Also

- [Reading UNIX Manual Pages](../os/reading-unix-manual-pages.md)
  Use the Terminal app to read the documentation for low-level UNIX tools and APIs.
- [Recording a Wi-Fi Packet Trace](recording-a-wi-fi-packet-trace.md)
  Record traces of Wi-Fi traffic and traffic management.
- [Submitting a Packet Trace to Apple](submitting-a-packet-trace-to-apple.md)
  Learn the best way to record a packet trace when communicating with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Network/troubleshooting-packet-traces)*