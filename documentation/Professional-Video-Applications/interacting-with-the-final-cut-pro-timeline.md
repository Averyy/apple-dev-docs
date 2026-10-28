# Interacting with the Final Cut Pro Timeline

**Framework**: Professional-Video-Applications  
**Role**: Article

Extend your workflows beyond media exchange by enabling a workflow extension to interact with the Final Cut Pro timeline.

## Overview

When you want to extend your workflows to allow users to interact with the Final Cut Pro timeline, use the interface provided by the Workflow Extension SDK. This interface enables a workflow extension to access a limited set of information about a sequence currently opened in the Final Cut Pro timeline. The APIs implement methods that a workflow extension can call to access proxy instances of the Final Cut Pro timeline objects, such as current sequence or playhead position. By enabling an extension to interact with the Final Cut Pro timeline, you can receive updates to a project opened in the Final Cut Pro timeline and use this information to make necessary edits in a workflow extension project.

### Access the Host Proxy Object

Before you can access the Final Cut Pro timeline proxy objects, you need to get a proxy instance of the host object. The host object is an initial access point for the extension to access the Final Cut Pro timeline proxy objects. The `ProExtensionHost` framework includes the [`ProExtensionHostSingleton()`](../professional_video_applications/proextensionhostsingleton%28%29.md) method, which returns the singleton proxy instance of the host object. Once you have the proxy host object, validate that the object conforms to the [`FCPXHost`](../professional_video_applications/fcpxhost.md) protocol.

Use the [`timeline`](../professional_video_applications/fcpxhost/timeline.md) property of the `FCPXHost` protocol to access the Final Cut Pro timeline objects.

**Swift**:

```swift
let timeline = host.timeline
```

**Objective-C**:

```objc
FCPXTimeline* timeline = self.host.timeline; 
```

### Observe Changes in the Final Cut Pro Timeline

The most common use case for observing changes in the Final Cut Pro timeline is for a workflow that requires an extension to update its interface based on changes in the Final Cut Pro timeline. For example, workflows like the review and approval process might require you to sync the extension timeline with the Final Cut Pro timeline to provide real-time feedback to users about Final Cut Pro timeline state changes.

The `ProExtensionHost` framework defines a timeline proxy object that has methods you can call to observe and get notified about changes to timeline object properties, such as sequence or playhead position. After Final Cut Pro notifies an extension about changes in its timeline, you can access the new values for timeline object properties through their associated accessor methods.

To observe for changes in the Final Cut Pro timeline, register an observer object in your workflow extension using the [`add(_:)`](../professional_video_applications/fcpxtimeline/add%28_%29.md) method. The observer must conform to the [`FCPXTimelineObserver`](../professional_video_applications/fcpxtimelineobserver.md) protocol, and it plays an important role in letting your extension communicate with the Final Cut Pro timeline. In your extension code, choose the class that you use to sync the Final Cut Pro timeline with your internal data structures, and make that class act as an observer. A common choice is to use your extension view controller, but you can choose any other class in your extension.

**Swift**:

```swift
host.timeline?.add(self)
```

**Objective-C**:

```objc
[host.timeline addTimelineObserver(NSObject<FCPXTimelineObserver>*)self];
```

Once you register an observer, an extension can observe for changes in the timeline sequence, the selected time range within the sequence, and the current playhead position in the timeline.

The following image shows an example of a sequence that is playing in the Final Cut Pro timeline.

![Image showing an active timeline sequence.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3570244@2x.png)

The next image shows a selected time range in the Final Cut Pro timeline.

![Screenshot showing a time range selection within a sequence.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3570245@2x.png)

The image below shows the playhead position that marks the current position in the timeline or the browser.

![Screenshot showing the playhead position within a sequence.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3570246@2x.png)

Based on the [`FCPXTimelineObserver`](../professional_video_applications/fcpxtimelineobserver.md) methods implemented in your observer object, Final Cut Pro notifies an observer about state changes to the timeline object properties. For example, if you implement the [`activeSequenceChanged()`](../professional_video_applications/fcpxtimelineobserver/activesequencechanged%28%29.md) method in the observer object, Final Cut Pro notifies the observer when a sequence changes in its timeline. In the method implementation, get details about the new sequence using the [`activeSequence`](../professional_video_applications/fcpxtimeline/activesequence.md) property.

**Swift**:

```swift
func activeSequenceChanged() {
    let sequence = host.timeline?.activeSequence

    // do something with the sequence returned above
}

```

**Objective-C**:

```objc
- (void) activeSequenceChanged
{
   FCPXSequence* sequence = host.timeline.activeSequence;

   // do something with the sequence returned above
}
```

By observing for changes in the Final Cut Pro playhead position, you can support workflows that sync playback between the extension and the Final Cut Pro timeline. To sync playback, in your observer’s  [`playheadTimeChanged()`](../professional_video_applications/fcpxtimelineobserver/playheadtimechanged%28%29.md) implementation, use the [`playheadTime()`](../professional_video_applications/fcpxtimeline/playheadtime%28%29.md) method to get the new Final Cut Pro playhead time, and then update the workflow extension playhead position to the new time.

**Swift**:

```swift
func playheadTimeChanged() {
   if let time = host.timeline?.playheadTime() {
        currentTime = time
    }
}
```

**Objective-C**:

```objc
- (void) playheadTimeChanged
{
   CMTime time = [self.host.timeline playheadTime];

   [self setCurrentTime:time]
}
```

### Move the Playhead Position

You can support workflows that allow users to locate a specific playhead position in the Final Cut Pro timeline by using the [`movePlayhead(to:)`](../professional_video_applications/fcpxtimeline/moveplayhead%28to%29.md) method. Calling this method in your extension allows you to manage the Final Cut Pro playhead by moving it to a position based on user input. For example, you can use the `movePlayheadTo` method to allow users to locate a specific playhead position in the Final Cut Pro timeline that a reviewer has referred to in a project opened in the workflow extension.

To move the Final Cut Pro playhead position based on user input, add a UI element in the extension interface to receive user action. Then, in the action method of the UI element, invoke the [`movePlayhead(to:)`](../professional_video_applications/fcpxtimeline/moveplayhead%28to%29.md) method to move the Final Cut Pro playhead to a time the user specifies.

**Swift**:

```swift
func someMethodRespondingToUIElement(withNewTime newTime: CMTime) {    
    let resultTime = host.timeline?.movePlayhead(to: newTime)
}
```

**Objective-C**:

```objc
- (void) someMethodRespondingToUIElement:(CMTime)newTime
{
   CMTime resultTime = [host.timeline movePlayheadTo:newTime]
}
```

You can also use the `movePlayheadTo` method to sync playback between sequences opened in the extension and the Final Cut Pro timeline, by moving the Final Cut Pro playhead position to match the workflow extension playhead time.

> **Note**: Do not move the Final Cut Pro timeline playhead when your workflow extension object gets notified of the change in the Final Cut Pro timeline playhead time.

## See Also

### FCPX Interactions
- [protocol FCPXHost](../professional_video_applications/fcpxhost.md)
  A protocol that provides an interface to retrieve the Final Cut Pro timeline proxy objects and details of the host app.
- [func ProExtensionHostSingleton() -> (any NSObjectProtocol)?](../professional_video_applications/proextensionhostsingleton%28%29.md)
  Returns the singleton proxy instance of the host object.
- [class FCPXTimeline](../professional_video_applications/fcpxtimeline.md)
  An interface that has methods and properties to communicate and interact with the Final Cut Pro timeline.
- [protocol FCPXTimelineObserver](../professional_video_applications/fcpxtimelineobserver.md)
  An interface with optional methods implemented by observers of [`FCPXTimeline`](../professional_video_applications/fcpxtimeline.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/interacting-with-the-final-cut-pro-timeline)*