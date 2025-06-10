# Analyzing audio performance with Instruments

**Framework**: Audio Toolbox

Ensure a smooth and immersive audio experience in your apps using Audio System Trace.

#### Overview

Poor quality audio playback can ruin the immersive experience in your app, making it crucial to maintain smooth audio playback by eliminating glitches and dropouts. When you encounter an audio glitch, you hear unintended distortion in the playback — pops, dropouts, and clicks. The Audio System Trace template includes several instruments that provide information about your app’s performance and help you troubleshoot audio issues. The Audio Statistics, Audio Server, and Audio Client tracks are instruments in the Audio System Trace template that provide insights, errors, and warnings about the Core Audio system, and enable you to improve your appʼs audio experience.

##### Launch Audio System Trace

From Xcode’s Product menu, choose Profile, or press Command-I. After Instruments launches, select Audio System Trace, then click Choose.

![A screenshot of the profiling templates in Instruments that shows Audio System Trace selected. At the bottom, there are two buttons: Cancel and Choose.](https://docs-assets.developer.apple.com/published/9c281699ca3c2ada165eb891446651d0/media-4306594%402x.png)

The Audio System Trace template includes the following instrument tracks:

##### Explore the Audio System Trace Instruments

Audio System Trace instruments include tracks to help you isolate where glitches are occurring and identify the cause of audio performance issues. You can view the audio system performance captured in an audio system trace in two ways:

- You can capture a trace by clicking the Record button in the toolbar. Your app launches Audio System Trace and starts recording. Within your app, perform the actions that reproduce the audio performance issue you want to analyze, and then click the Stop button to stop recording.
- You can open an audio system trace you previously recorded. In Instruments, choose File > Open, select a trace file, and click Open.

![A screenshot of recording an Audio System Trace. At the top, there is a recording button. Clicking the recording button starts the recording.](https://docs-assets.developer.apple.com/published/b4557d78f14cf6ca8e0418e956e9a405/media-4306618%402x.png)

The audio system trace appears in a new window, along with the timeline and detail panes, as shown in the following screenshot.

![A screenshot of the highlights and the areas of interest of a trace: Audio Instruments, Recording Controls, Audio Client track, Audio Statistics track, Audio Server track, Process track, Run Information, Timeline pane, inspector pane, and detail pane. ](https://docs-assets.developer.apple.com/published/c73b4cd429b877e2912d7c7ef0a6e8ba/media-4309270%402x.png)

Move your pointer along the top of the trace timeline pane to see points of interest along the Audio Client and Audio Server tracks. To identify audio performance issues, click the points of interest to view errors and warnings.

![A screenshot of the trace timeline pane. It shows points of interest along the different tracks.](https://docs-assets.developer.apple.com/published/078fe87acbd3aef4ef8700d4e4c20d3e/media-4309315%402x.png)

To have better granularity for a specific track, use your mouse or trackpad to zoom in to the corresponding area of the track for more information. Click a point of interest to update the detail pane for that selected track and view any corresponding detail information.

![A screenshot of points of interest along the various tracts. It shows the contents of a point of interest displayed when you click it.  ](https://docs-assets.developer.apple.com/published/ba55be106f2bec3322ac52ba67385e14/media-4309314%402x.png)

##### Analyze Audio Performance Statistics

The Audio Statistics track gives an overview of each engine’s jitter and sample time information to provide insights into the system’s audio performance. The track displays two graphs: Engine Jitter and I/O Threads. The Engine Jitter graph quantifies deviations from an expected tick cadence. The I/O Threads graph shows the number of concurrent audio threads. The Engine represents a collection of one or more audio devices bound together.

Click the arrow next to the instrument name to switch between these two graphs.

![A screenshot of the Audio Statistics Instrument button selected in the Audio Statistics track. Clicking the Instrument button displays the two buttons you can choose for the track information. The buttons are Engine Jitter and I/O Threads.](https://docs-assets.developer.apple.com/published/db5fda27e99a7c21a72a02048610064c/media-4306636%402x.png)

The table below describes the colors and associated jitter times in the Audio Statistics track.

| Color | Jitter time µs (microseconds) |
| --- | --- |
| Green | 0–30 µs |
| Orange | 31–100 µs |
| Red | > 100 µs |

The Audio Statistics track’s detail pane includes the following menu items:

##### Identify Glitches with the Audio Server Track

The Audio Server track provides Engine Time Stamp and I/O Cycle Load graphs, and related points of interest. Engine timestamp refers to the time when the audio engine processes audio, and it can help determine where a delay or other problem occurred in the audio processing chain. I/O cycle load refers to the time the system spends processing an audio buffer relative to the available time to process that buffer.

If the client doesn’t complete its operation during the allotted cycle time, the system can’t process the audio in real-time, leading to dropouts or glitches. If the I/O cycle load is consistently high, it indicates the audio processing might be too complex or intensive for the current buffer size and sample rate configuration.

Click the arrow next to the instrument name to switch between the Engine Time Stamp and I/O Cycle Load graphs.

![A screenshot of the Audio Server Instrument button selected in the Audio Server Track. Clicking the Instrument button displays the two buttons you can select for the track information. The buttons are I/O Cycle Load and Engine Time Stamp.](https://docs-assets.developer.apple.com/published/9f91fa1e1d1673c62299cb73449ce94c/media-4309276%402x.png)

As you view these tracks, pay particular attention to the red points of interest, which help you isolate where the audio issues occur. Typically, these issues occur when the I/O cycle takes too long. The points of interest include overloads, clock discontinuity errors, reanchors, and read safety violations.

An overload occurs if you don’t deliver data on time, leading to issues in real-time audio playback. It’s indicated in red on the graph and has a red point of interest. If you don’t promptly write audio data to the output buffer, the speakers lack the necessary information for continuous playback and glitch until they receive the missing data. A clock discontinuity occurs when the clock has failed to stay in sync or there has been a break in the device’s continuous samples. When detecting a clock discontinuity, Core Audio actively attempts to reanchor the device’s clock with the timeline. A read safety violation tracks how close to a driver’s safety offset a read was.

##### View Zero Timestamp Information

Switching to the Zero Time Stamp detail pane in the Audio Server track can help you determine if an operation doesn’t complete within an audio I/O cycle, leading to overloads and glitches.

A ring buffer is a fixed-size data structure where the last element connects to the first. Every time the audio driver completes a loop of the ring buffer, it generates a new zero timestamp. The following screenshot shows the Audio Server’s detail pane with zero timestamp information.

![A screenshot of the tracks in the template. It shows a callout to the zero timestamp selection at the bottom of the screen, and the detail pane updates with the Zero Time Stamp events. ](https://docs-assets.developer.apple.com/published/74742b558a3fc4404d49d47e52827547/media-4311862%402x.png)

The following menu items describe the zero timestamp information in the Audio Server track’s detail pane shown above:

##### Inspect the Audio Client Track

The audio stack has a client/server architecture. To analyze audio system performance, you may want to examine what happens between the server and the client (your app). The Audio Client track provides information about the timing of I/O process callbacks for your app. Points of interest show issues with your app’s audio performance and correlate to points of interest in the Audio Server track.

![A screenshot of the Audio Client track and detail pane for the track. It shows the point of interest for the track on overloads in the detail pane at the bottom.](https://docs-assets.developer.apple.com/published/41e3a88fad091efefc9771da967dceba/media-4311403%402x.png)

##### Use Real Time Operations

In the screenshot below, overloads are visible in the Audio Server track and are likely to cause glitches. Client operations might be conducting non–real-time operations that aren’t safe, which can cause overloads. Blocking on a lock, allocating memory, or performing complex operations that exceed the allotted audio server time are examples of non–real-time operations that can cause glitches.

![A screenshot of the Audio Server track with overloads. ](https://docs-assets.developer.apple.com/published/d2d6f91ba37bcca15173173e107a305b/media-4311436%402x.png)

##### Complete Multiple Audio Threads By a Common Deadline

Completing multiple real-time audio threads by a common deadline is important, or glitches can occur. An audio workgroup consists of real-time threads collaborating across various processes — such as the audio server, client apps, and plug-ins — to generate audio by a common deadline. The system uses audio workgroups to effectively monitor the CPU utilization of real-time threads, aiming to optimize the trade-off between energy efficiency and system performance.

> 💡 **Tip**:  Use Audio Workgroups API to optimize your audio threads’ performance, giving the operating system insight into active real-time threads, including auxiliary ones that other apps and Audio Unit plug-ins created. For further insights into audio workgroups, see [`Understanding Audio Workgroups`](understanding-audio-workgroups.md).

##### Analyze Backtrace Information

With your app’s track, you can select the detail row where the overload occurs to see the corresponding backtrace in the inspector pane, as shown in the screenshot below. The backtrace information can take you to your code that’s causing audio performance issues.

![A screenshot of the app’s track selected. It shows the detail pane and displays a corresponding backtrace in the inspector pane.](https://docs-assets.developer.apple.com/published/2499534deb0ca0141bd925e8fc77bfed/media-4311883%402x.png)

##### Confirm Tracks Have No Errors or Warnings

When you’ve corrected all glitches appearing in your Audio Client and Audio Server tracks, you see the Audio Server track with the client audio completed within the time allotted by the server. As shown below, there are no errors or warnings in the tracks.

![A screenshot of the Audio Client, Audio Statistics, and Audio Server tracks. It shows no errors or warnings in the tracks.](https://docs-assets.developer.apple.com/published/4770001657ca239093b07b717fa88720/media-4311885%402x.png)

## See Also

- [Audio Converter Services](audio-converter-services.md)
  Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](audio-toolbox-debugging.md)
  Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](audio-codec.md)
  Translate audio data from one format to another.
- [Clock Utilities](clock-utilities.md)
  Manage time-related information associated with audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/analyzing-audio-performance-with-instruments)*