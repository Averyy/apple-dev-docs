# Analyzing the performance of a foveated streaming session

**Framework**: Foveated Streaming

Use the Foveated Streaming Statistics instrument to evaluate the performance of your visionOS streaming client app.

#### Overview

Maintaining a high frame rate while minimizing latency is critical to ensure a comfortable and immersive foveated streaming experience on Apple Vision Pro. The Foveated Streaming framework delivers high-quality immersive content to Apple Vision Pro through a highly-optimized, real-time pipeline:

- Apple Vision Pro sends its pose and information about the approximate region where the person is looking to a streaming server.
- The server uses the pose to render a frame.
- The server foveates that frame for streaming, applying encoding at higher resolution only where necessary.
- The server sends the foveated frame back to Apple Vision Pro for decoding and display.

This intricate, real-time process demands minimal latency to mitigate motion sickness, disorientation, and breaks in immersion that high latency causes.

To get useful information specific to foveated streaming, profile your app with the Foveated Streaming Statistics instrument. This instrument helps you identify:

- Available network bandwidth and streaming rate.
- Received and reprojected frame rates.
- End-to-end streaming latency.

For more information on how to use Instruments, see [`Profiling apps using Instruments`](https://developer.apple.com/tutorials/instruments).

#### Prepare the Foveated Streaming Statistics Instrument

To set up a new Instruments document from Xcode:

1. Choose Product > Profile; this opens the Instruments app.
2. In Instruments, select the Blank template, then click Choose.
3. In the Instruments selector, click “+ Instrument”.
4. In the filter field, enter “fov” to quickly locate the Foveated Streaming Statistics instrument.
5. Double click the instrument to add the Foveated Streaming Statistics instrument.

![A screenshot of the Instruments app with the Foveated Streaming Statistics instrument added to a blank template. The right side of the window displays three sections with settings for Target, Recorder Settings, and Foveated Streaming Statistics. Under the Target section the target is set to attach to the FoveatedStreaming-Sample app. Under the Recorder Settings section, the Recording Mode is set to Deferred. There are no settings under the Foveated Streaming Statistics section.](https://docs-assets.developer.apple.com/published/bfa0729e05117bf797a92ca6f1cf61b8/setting-up-instruments%402x.png)

> 💡 **Tip**: You can add additional instruments alongside the Foveated Streaming Statistics instrument to create a more comprehensive performance profile of your app. For more information, see [`Analyzing the performance of your visionOS app`](https://developer.apple.com/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app).

#### Capture Streaming Statistics

To collect metrics for a foveated streaming session:

1. Click the Record button at the top left of the window to start capturing profile data.
2. Connect the [`FoveatedStreamingSession`](foveatedstreamingsession.md) in your app to a streaming endpoint that’s actively streaming content.
3. Click the stop button to stop recording.

![A screenshot of a run of the Foveated Streaming Statistics instrument displaying graphs with metrics for Average Streaming Rate, Available Bandwidth, Frame Receive Rate, Reprojection Rate, Pose Rate, Pose To Frame Submitted Latency, Pose To Frame Dequeued Latency, Pose To Frame Received Latency, and Pose Upload Latency. The Pose Rate metric is selected in a panel at the bottom of the window, displaying a Minimum Pose Rate of 68.8 FPS, an Average Pose Rate of 90.2 FPS, and a Maximum Pose Rate of 125.3 FPS.](https://docs-assets.developer.apple.com/published/35db9637a9dd12d62dd8eabf0e0dad1b/performance-graphs%402x.png)

The Foveated Streaming Statistics instrument collects metrics on the following:

- **Average Streaming Rate**: The amount of data being streamed per second.
- **Available Bandwidth**: The total network bandwidth available for streaming. This acts as the upper limit on the Average Streaming Rate.
- **Frame Receive Rate**: The number of frames received from the streaming server per second.
- **Reprojection Rate**: The frame rate the app displays the received frames with. For example, if the Frame Receive Rate is lower than the maximum frame rate of the display, Apple Vision Pro re-projects the received frames to improve the overall frame rate.
- **Pose Rate**: The sampling rate of the device pose that Apple Vision Pro sends to the streaming server.
- **Pose to Frame Submitted Latency**: The end-to-end latency from Apple Vision Pro sending the device pose to receiving, decoding, and submitting a streamed frame to display.
- **Pose to Frame Dequeued Latency**: The latency from Apple Vision Pro sending the device pose to receiving an encoded frame and dequeing it from a buffer to compensate for network timing fluctuations.
- **Pose to Frame Received Latency**: The latency from Apple Vision Pro sending the device pose to receiving an encoded frame.
- **Pose Upload Latency**: The one-way latency between Apple Vision Pro sending the device pose and the server receiving it.

#### Diagnose Performance Issues

The most common source of foveated streaming performance issues is network limitations. If you observe visual artifacts, stuttering, or a lack of responsiveness, begin by examining the Available Bandwidth and Average Streaming Rate. A significant gap between these two values, or consistently low numbers for either, strongly indicates that your network connection is the limiting factor. This could be due to network congestion, poor Wi-Fi signal strength, or other connectivity problems.

#### Evaluate Your Apps Performance

If the `Available Bandwidth` and `Average Streaming Rate` appear reasonable, the next step is to investigate your app’s internal performance. One indicator of your app’s performance is the Pose Rate. For optimal foveated streaming, the Pose Rate should be consistent with the device’s refresh rate; for example, 90 Hz. A Pose Rate significantly below this target suggests that your app isn’t running at its maximum frame rate. This indicates that something within your app’s logic or rendering pipeline is causing slowdowns.

In such cases, you can use other Xcode instruments, like Time Profiler, to pinpoint the specific performance bottlenecks within your app.

To understand the overall responsiveness and end-to-end latency of the system, monitor the Pose to Frame Submitted Latency metric. This metric measures the total time from when Apple Vision Pro sends a device pose to when decoding and submitting the corresponding streamed frame for display.

You want this latency to be as low as possible for a fluid and reactive experience. Consistently high Pose to Frame Submitted Latency — even when initial network and streaming rates seem adequate — can suggest more subtle or intermittent network issues, such as network jitter or packet loss, which might not be immediately obvious from average bandwidth metrics.

If this latency is high, focus on optimizing your network environment for stability and consistency, or review your app’s processing and rendering pipeline for any client-side work that could introduce delays before frame submission.

## See Also

- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)
  Integrate NVIDIA CloudXR™ and the session management connection protocol into your desktop or cloud application to stream high-fidelity spatial content to Apple Vision Pro.
- [Establishing foveated streaming sessions with Apple Vision Pro](establishing-foveated-streaming-sessions-with-apple-vision-pro.md)
  Discover, pair, and manage streaming sessions between Apple Vision Pro and local streaming endpoints by implementing the session management connection protocol.
- [Creating a foveated streaming client on visionOS](creating-a-foveated-streaming-client-on-visionos.md)
  Build a visionOS app that streams high-fidelity immersive content from a computer or the cloud using the Foveated Streaming framework.
- [class FoveatedStreamingSession](foveatedstreamingsession.md)
  A session that manages a foveated streaming connection to a local or remote streaming endpoint.
- [struct FoveatedStreamingSpaceContent](foveatedstreamingspacecontent.md)
  A type that defines the content of an immersive space displaying a foveated stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/analyzing-the-performance-of-a-foveated-streaming-session)*