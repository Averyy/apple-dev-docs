# Understanding Audio Workgroups

**Framework**: Audio Toolbox

Learn how to optimize real-time rendering performance with the Audio Workgroups API.

#### Overview

The Audio Workgroups API is a new feature available in macOS 11, iOS 14.0, watchOS 7.0 and tvOS 14.0. An audio workgroup helps the OS optimize performance by providing additional information about active real-time threads, including auxiliary ones created by apps and Audio Unit plug-ins.

An audio workgroup is a collection of real-time threads that work together to produce audio by a common deadline while spanning multiple processes, including the audio server and client apps and plug-ins. The system uses the audio workgroups to observe CPU usage of real-time threads so that it can better balance the competing interests of power consumption and performance. Apps and plug-ins that create their own real-time threads for audio synthesis or signal processing should adopt this new API.

> **Note**:  Only real-time threads can join an audio workgroup; nonreal-time threads cannot.

 Only real-time threads can join an audio workgroup; nonreal-time threads cannot.

##### Learn About Audio Workgroups

The diagram below shows how Core Audio runs an I/O thread in the audio server as part of the audio device’s workgroup. The thread wakes up at regular intervals and calls its associated client app to retrieve its audio output. When the client finishes rendering its audio, the system writes it to the output hardware, and the I/O thread sleeps. If a client takes too long to produce audio, the thread misses its deadline, which results in an audio overload and an interruption in audio playback. The I/O thread is the  thread of an audio device workgroup, and it informs the kernel of the beginning and end of each work cycle.

![A diagram that shows how Core Audio runs an I/O thread in the audio server.](https://docs-assets.developer.apple.com/published/85a6bf9ee0a0e8dfb0e606817d65cbab/media-3627695%402x.png)

For every audio server I/O thread, its associated app also has its own real-time render thread. The audio server wakes and waits for the app to produce its output on each I/O cycle. The system automatically joins the client app’s real-time thread to the audio device’s workgroup. By doing so, the system tells the kernel that both threads are working together with a common deadline and can better optimize performance.

> ❗ **Important**:  Your app or plug-in requires no additional work if the only real-time thread it uses is the one that the audio frameworks provide. The audio system automatically joins its real-time threads to an audio device workgroup.

 Your app or plug-in requires no additional work if the only real-time thread it uses is the one that the audio frameworks provide. The audio system automatically joins its real-time threads to an audio device workgroup.

If your app or Audio Unit plug-in creates and manages its own audio real-time threads, learn more about how to use the Audio Workgroup API in following articles:

- If your app creates auxiliary real-time threads that run in sync with the I/O thread, see [`Adding Parallel Real-Time Threads to Audio Workgroups`](adding-parallel-real-time-threads-to-audio-workgroups.md).
- If your app creates real-time threads that run asynchronously with the I/O thread, see [`Adding Asynchronous Real-Time Threads to Audio Workgroups`](adding-asynchronous-real-time-threads-to-audio-workgroups.md).
- If your Audio Unit plug-in creates auxiliary audio-rendering threads, see [`Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups`](adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups.md).

## See Also

- [Adding Parallel Real-Time Threads to Audio Workgroups](adding-parallel-real-time-threads-to-audio-workgroups.md)
  Optimize the performance of real-time audio threads that run in sync with the I/O thread by adding them to the audio device workgroup.
- [Adding Asynchronous Real-Time Threads to Audio Workgroups](adding-asynchronous-real-time-threads-to-audio-workgroups.md)
  Optimize system performance by adding real-time audio threads that run asynchronously to the I/O thread to custom audio workgroups.
- [Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups](adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups.md)
  If your Audio Unit plug-in creates auxiliary real-time rendering threads, add them to the host app’s audio workgroup so the system can schedule them appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/understanding-audio-workgroups)*