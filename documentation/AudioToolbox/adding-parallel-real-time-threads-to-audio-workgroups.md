# Adding Parallel Real-Time Threads to Audio Workgroups

**Framework**: Audio Toolbox

Optimize the performance of real-time audio threads that run in sync with the I/O thread by adding them to the audio device workgroup.

#### Overview

If your app creates one or more auxiliary real-time threads that run in sync with the audio server I/O thread, join them to its audio workgroup. Doing so informs the system that these threads are rendering to the same deadline, which helps it optimize performance.

##### Add Your Threads to the Audio Device Workgroup

Begin by retrieving the audio device’s workgroup, so you can join your threads to it. Retrieve it from the I/O Audio Unit (AUHAL or AURemoteIO) using either the [`kAudioOutputUnitProperty_OSWorkgroup`](kaudiooutputunitproperty_osworkgroup.md) property for AUv2, or the [`AUAudioUnit`](auaudiounit.md) [`osWorkgroup`](auaudiounit/osworkgroup.md) property for AUv3. In macOS, you can also get it directly from the audio device by using the HAL API. Then, in your real-time thread, call [`os_workgroup_join`](https://developer.apple.com/documentation/os/3649707-os_workgroup_join) to join it to the workgroup, and call [`os_workgroup_leave`](https://developer.apple.com/documentation/os/3649708-os_workgroup_leave) when you’ve finished your work, as shown in the example below.

```objc
#import <AudioToolbox/AudioToolbox.h>
 
// Get the workgroup from the AUHal.
os_workgroup_t _Nonnull workgroup = auHal.osWorkgroup;

// An opaque join token that the client needs to pass to join and leave a workgroup.
os_workgroup_join_token_s joinToken;

void realtimeThreadFunction(os_workgroup_t workgroup) {
    
    // Join this thread to the workgroup.
    const int result = os_workgroup_join(workgroup, &joinToken);
    if (result == 0) {
        // Success.
    }
    else if (result == EALREADY) {
        // The thread is already part of a workgroup that can't be
        // nested in the the specified workgroup.
        return;
    }
    else if (result == EINVAL) {
        // The workgroup has been canceled.
        return;
    }
    
    // Work cycle.
    while (threadShouldRun) {
        // Typically, wait on a semaphore.
        waitForWork();
        // The controlling thread signaled this thread to stop.
        if (threadShouldRun) {
            performCustomAudioDSPWorkUnit();
            // Typically, signal a semaphore.
            signalWorkComplete();
        }
    }
    
    // Before exiting the thread, leave the workgroup.
    os_workgroup_leave(workgroup, &joinToken);
}
```

## See Also

- [Understanding Audio Workgroups](understanding-audio-workgroups.md)
  Learn how to optimize real-time rendering performance with the Audio Workgroups API.
- [Adding Asynchronous Real-Time Threads to Audio Workgroups](adding-asynchronous-real-time-threads-to-audio-workgroups.md)
  Optimize system performance by adding real-time audio threads that run asynchronously to the I/O thread to custom audio workgroups.
- [Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups](adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups.md)
  If your Audio Unit plug-in creates auxiliary real-time rendering threads, add them to the host app’s audio workgroup so the system can schedule them appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/adding-parallel-real-time-threads-to-audio-workgroups)*