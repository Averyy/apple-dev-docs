# AudioWorkIntervalCreate

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Creates a new interval workgroup for managing real-time audio threads.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
os_workgroup_interval_tAudioWorkIntervalCreate(const char *name, os_clockid_t clock, os_workgroup_attr_t attr);
```

## Mentions

- [Adding Asynchronous Real-Time Threads to Audio Workgroups](./adding-asynchronous-real-time-threads-to-audio-workgroups.md)

## Return Value

A new interval workgroup object that manages real-time audio threads.

## Discussion

Use this function to create a new workgroup object that your code manages. The returned workgroup object has no associated threads initially. Join one or more threads to the workgroup, and designate one thread to manage the workgroup’s schedule. This designated thread sets the workgroup’s schedule using the [`os_workgroup_interval_start`](../os/os_workgroup_interval_start.md), [`os_workgroup_interval_update`](../os/os_workgroup_interval_update.md), and [`os_workgroup_interval_finish`](../os/os_workgroup_interval_finish.md) functions.

## Parameters

- `name`: An optional name for the workgroup. Use this name to identify the workgroups you create. You may specify `NULL` for this parameter.
- `clock`: The clock type to use when specifying time-related values for the workgroup. For a list of possible values, see [`os_clockid_t`](../os/os_clockid_t.md).
- `attr`: Additional attributes to associate with the workgroup. Specify `NULL` for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioworkintervalcreate)*