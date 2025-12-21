# isMultiThreaded

**Framework**: OpenGL ES  
**Kind**: property

A Boolean value that determines whether OpenGL ES defers work to another thread.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 7.1+
- tvOS 9.0+

## Declaration

```swift
var isMultiThreaded: Bool { get set }
```

#### Discussion

Set the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true) to enable multithreading in OpenGL ES. A multithreaded OpenGL ES context automatically creates a worker thread and transfers some of its calculations to that thread. When you enable multithreading on a multicore device, internal OpenGL ES calculations performed on the CPU act in parallel with your app, improving performance.

When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), OpenGL ES performs any CPU-based calculations for a command on the thread it was called from.

If the current device does not support multithreaded OpenGL ES, the value of this property is always [`false`](https://developer.apple.com/documentation/Swift/false)—attempting to set the value to [`true`](https://developer.apple.com/documentation/Swift/true) has no effect.

> **Note**:  Enabling multithreading has both costs and benefits to performance—you should choose a concurrency strategy that provides the most benefit to your app. For details, see [`Concurrency and OpenGL ES`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/ConcurrencyandOpenGLES/ConcurrencyandOpenGLES.html#//apple_ref/doc/uid/TP40008793-CH409) in [`OpenGL ES Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793).


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/ismultithreaded)*