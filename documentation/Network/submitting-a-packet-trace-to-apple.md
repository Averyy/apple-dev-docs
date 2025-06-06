# Submitting a Packet Trace to Apple

**Framework**: Network

Learn the best way to record a packet trace when communicating with Apple.

#### Overview

At times you may need to record a packet trace and then share it with Apple for further analysis. For example:

- You might be reporting a bug where a packet trace is needed by the Apple engineers to understand, and hence fix, the bug.
- You might be working with Developer Technical Support (DTS) to investigate a problem that can only be reproduced on your network.

When you submit a packet trace in such situations, follow the instructions below to ensure that you’ve included all the relevant information.

> **Note**:  These instructions are also useful if you’re investigating a problem reported by an advanced user and need them to send  a packet trace to further that investigation.

 These instructions are also useful if you’re investigating a problem reported by an advanced user and need them to send  a packet trace to further that investigation.

##### Record the Trace

Follow these steps to record a packet trace to submit to Apple.

> **Note**:  These steps assume you’re recording the trace using the facilities built in to macOS. If necessary you can use a third-party tool, and even a tool on another platform, to record your trace, but make sure to read the information on packet trace formats in [`Work Through the Submission Checklist`](submitting-a-packet-trace-to-apple#Work-Through-the-Submission-Checklist.md).

 These steps assume you’re recording the trace using the facilities built in to macOS. If necessary you can use a third-party tool, and even a tool on another platform, to record your trace, but make sure to read the information on packet trace formats in [`Work Through the Submission Checklist`](submitting-a-packet-trace-to-apple#Work-Through-the-Submission-Checklist.md).

1. If you’re developing for the Mac, determine the correct interface as described in [`Choose the Correct Interface`](recording-a-packet-trace#Choose-the-Correct-Interface.md). If you’re developing for iOS, set up a remote virtual interface (RVI) per the instructions in [`Set Up iOS Packet Tracing`](recording-a-packet-trace#Set-Up-iOS-Packet-Tracing.md).
2. Open a Terminal window and run the command `sudo tcpdump -i en0 -w trace.pcap`, replacing `en0` with the name of the network interface from step 1.
3. Reproduce the problem.
4. When you’re done, press Control-C in Terminal to stop the packet trace.
5. Locate the resulting `trace.pcap` file.
6. Follow the instructions in [`Work Through the Submission Checklist`](submitting-a-packet-trace-to-apple#Work-Through-the-Submission-Checklist.md) to ensure that you’ve included all the necessary information.
7. Submit the file to Apple as described in [`Submit the Packet Trace to Apple`](submitting-a-packet-trace-to-apple#Submit-the-Packet-Trace-to-Apple.md).

##### Work Through the Submission Checklist

When you submit a packet trace to Apple, make sure you provide:

- The system type and OS version of the computer that recorded the packet trace. In the case of an RVI trace, include this information for both the Mac and the iOS device.
- If you’re using a packet trace tool that’s not built in to macOS, include the name and version of the tool you used to record the packet trace.

For each relevant machine shown in the packet trace, describe the following:

- The machine’s role in the network conversation
- The system type and OS version
- The machine’s IP address
- The machine’s hardware address (also known as the Ethernet address, Wi-Fi address, or MAC address)

##### Submit the Packet Trace to Apple

Before you submit your trace to Apple, make sure you’ve included all of the information described in [`Work Through the Submission Checklist`](submitting-a-packet-trace-to-apple#Work-Through-the-Submission-Checklist.md). You can put this information in a separate text file if you want, but it’s OK to just include it as text in your bug report, DTS support request, and so on.

If you’re using a packet trace tool whose native file format is PCAP or PcapNg (including `tcpdump`, Wireshark, and various others), you can include your packet trace file as is. Otherwise, include the original packet trace file and, if the file isn’t already text, export the trace as text and include that text file as well. That way Apple is guaranteed to be able to read your packet trace.

## See Also

- [Troubleshooting Packet Traces](troubleshooting-packet-traces.md)
  Take action to address packet tracing problems.
- [Recording a Wi-Fi Packet Trace](recording-a-wi-fi-packet-trace.md)
  Record traces of Wi-Fi traffic and traffic management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/submitting-a-packet-trace-to-apple)*