# Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups

**Framework**: Audio Toolbox

If your Audio Unit plug-in creates auxiliary real-time rendering threads, add them to the host app’s audio workgroup so the system can schedule them appropriately.

#### Overview

Most Audio Unit plug-ins don’t need to create their own real-time threads, but some complex plug-ins do to achieve their required processing. For example, a synthesizer may need to create additional real-time rendering threads to achieve maximum polyphony. So that the system knows about these threads, join them to an audio workgroup. To know which audio workgroup to add them to, provide a render context observer.

##### Provide a Render Context Observer

An [`AURenderContextObserver`](aurendercontextobserver.md) is a block the Audio Unit plug-in holds that the system calls before each render request. With each request, the system passes the block an [`AudioUnitRenderContext`](audiounitrendercontext.md) object that provides the audio workgroup of the calling context. When the context’s audio workgroup changes, join your auxiliary real-time threads to the new audio workgroup.

```objc
#import <AudioToolbox/AudioToolbox.h>
 
-(AURenderContextObserver)renderContextObserver {
 
    // Create block safe pointer to kernel.
    __block AUKernel *kernel = _kernel;
     
    /* 
    The system calls this block on the render thread, 
    immediately before any render request.
    */
    return ^ (const AudioUnitRenderContext *context) {
        if (auto renderContext = context) {
            kernel->workgroupDidChange(renderContext->workgroup);
        }
        else {
            /**
            The new workgroup may be null in the case of a nonreal-time
            render context, or a real-time thread that is not part of any
            workgroup.
            */
            kernel->removeAllWorkgroups();
        }
    };
}
```

## See Also

- [Understanding Audio Workgroups](understanding-audio-workgroups.md)
  Learn how to optimize real-time rendering performance with the Audio Workgroups API.
- [Adding Parallel Real-Time Threads to Audio Workgroups](adding-parallel-real-time-threads-to-audio-workgroups.md)
  Optimize the performance of real-time audio threads that run in sync with the I/O thread by adding them to the audio device workgroup.
- [Adding Asynchronous Real-Time Threads to Audio Workgroups](adding-asynchronous-real-time-threads-to-audio-workgroups.md)
  Optimize system performance by adding real-time audio threads that run asynchronously to the I/O thread to custom audio workgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups)*