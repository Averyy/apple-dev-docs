# Adding Asynchronous Real-Time Threads to Audio Workgroups

**Framework**: Audio Toolbox

Optimize system performance by adding real-time audio threads that run asynchronously to the I/O thread to custom audio workgroups.

#### Overview

If your app creates auxiliary real-time threads that run asynchronously to the audio server’s I/O thread, add them to a custom audio workgroup. Doing so informs the system of these threads and their deadlines, which helps it optimize performance.

##### Create Workgroups

If your auxiliary real-time threads run asynchronously to the I/O thread, you don’t add them to the audio device workgroup, but instead create a new audio workgroup. For each thread that has a unique work interval, create a new audio workgroup for it by calling [`AudioWorkIntervalCreate`](audioworkintervalcreate.md). Your workgroup may contain multiple threads, but only one is the primary thread and is responsible for controlling the others. In this thread, call [`os_workgroup_interval_start`](https://developer.apple.com/documentation/os/os_workgroup_interval_start) in each work cycle. The start time that you pass to this function can be the present, or a time in the past if you know exactly when the system scheduled your work cycle to begin. The function’s deadline argument has to be a timestamp value greater than the start time.

```objc
#include <mach/mach_time.h>
#import <AudioToolbox/AudioToolbox.h>

// This workgroup attribute isn't currently used. Set it to NULL.
os_workgroup_attr_t _Nullable attr = nullptr;

// One nanosecond in seconds.
constexpr static double kOneNanosecond = 1.0e9;

// The I/O interval time in seconds.
constexpr static double kIOIntervalTime = 0.020;

// The clock identifier that specifies interval timestamps.
os_clockid_t clockId = OS_CLOCK_MACH_ABSOLUTE_TIME;

// Create a workgroup interval.
os_workgroup_interval_t _Nullable workgroup =
    AudioWorkIntervalCreate("My Work Interval", clockId, attr);

void realtimeThreadFunction() {

    // Join this thread to the workgroup.
    if (!joinThisThreadToWorkgroup(workgroup)) {
        // Early return, unable to add this thread to the workgroup
        return;
    }

    // Get the mach time info.
    struct mach_timebase_info timeBaseInfo;
    mach_timebase_info(&timeBaseInfo);

    // The frequency of the clock is: (timeBaseInfo.denom / timeBaseInfo.numer) * kOneNanosecond
    const auto nanoSecFrequency = static_cast<double>(timeBaseInfo.denom) / static_cast<double>(timeBaseInfo.numer);
    const auto frequency = nanoSecFrequency * kOneNanosecond;

    // Convert the interval time in seconds to mach time length.
    const auto intervalMachLength = static_cast<int64_t>(kIOIntervalTime * frequency);
    while (true) {
        // Get the current host time.
        const auto currentTime = mach_absolute_time();
        const auto deadline = currentTime + intervalMachLength;

        // Call os_workgroup_interval_start each time the thread begins a work cycle
        int result = os_workgroup_interval_start(workgroup, currentTime, deadline, nullptr);

        if (result != 0) {
            // Something went wrong.
        }

        // Perform some custom DSP processing.
        customAudioDSP();

        // Call os_workgroup_interval_finish on completion of each a work cycle.
        result = os_workgroup_interval_finish(workgroup, nullptr);
    }
}

// Return true if the method joined the thread to the workgroup.
bool joinThisThreadToWorkgroup(os_workgroup_t workgroup) {
    // Join this thread to the workgroup.
    const int result = os_workgroup_join(workgroup, &joinToken);
    if (result == 0) {
        // Success.
    } else if (result == EALREADY) {
        // The thread is already part of a workgroup that can't be
        // nested in the the specified workgroup.
        return false;
    } else if (result == EINVAL) {
        // The workgroup has been canceled.
        return false;
    }
    return true;
}
```

If your app has other real-time threads that render to this audio workgroup’s deadline, you can join them to the audio workgroup as shown in the example below.

```objc
#import <AudioToolbox/AudioToolbox.h>
 
#import <AudioToolbox/AudioToolbox.h>

// The workgroup interval created in the previous example.
os_workgroup_interval_t workgroup = ...

void realtimeThreadFunction(os_workgroup_t workgroup) {

    // Join this thread to the workgroup.
    if (!joinThisThreadToWorkgroup(workgroup)) {
        // Early return, unable to add this thread to the workgroup
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
- [Adding Parallel Real-Time Threads to Audio Workgroups](adding-parallel-real-time-threads-to-audio-workgroups.md)
  Optimize the performance of real-time audio threads that run in sync with the I/O thread by adding them to the audio device workgroup.
- [Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups](adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups.md)
  If your Audio Unit plug-in creates auxiliary real-time rendering threads, add them to the host app’s audio workgroup so the system can schedule them appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/adding-asynchronous-real-time-threads-to-audio-workgroups)*