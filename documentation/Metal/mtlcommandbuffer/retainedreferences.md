# retainedReferences

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the command buffer maintains strong references to the resources it uses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var retainedReferences: Bool { get }
```

```objc
@property (readonly) BOOL retainedReferences;
```

## Discussion

You can configure this property when you create a command buffer by setting [`retainedReferences`](../mtlcommandbufferdescriptor/retainedreferences.md) of an [`MTLCommandBufferDescriptor`](../mtlcommandbufferdescriptor.md) instance and calling the [`makeCommandBuffer(descriptor:)`](../mtlcommandqueue/makecommandbuffer%28descriptor%29.md) method. The [`makeCommandBuffer()`](../mtlcommandqueue/makecommandbuffer%28%29.md) method sets this property to [`true`](../../Swift/true.md), and [`makeCommandBufferWithUnretainedReferences()`](../mtlcommandqueue/makecommandbufferwithunretainedreferences%28%29.md) sets it to [`false`](../../Swift/false.md).

If [`false`](../../Swift/false.md), your app is responsible for maintaining strong references to all the resources the command buffer relies on until it completes.

> ❗ **Important**:  Releasing a resource before a command buffer’s commands complete may cause a runtime error or erratic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/retainedreferences)*