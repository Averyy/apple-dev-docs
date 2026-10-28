# Workflow Extensions

**Framework**: Professional-Video-Applications  
**Role**: API Collection

Integrate your app’s workflow within the Final Cut Pro interface to streamline data exchange.

## Overview

When your app supports workflows that require users to exchange data between your app and Final Cut Pro, consider adding a workflow extension to your app. A workflow extension is not a replacement for your app; it’s an extension of the app’s functionality, made available within the Final Cut Pro interface. When a user’s workflow requires frequent switching between your app and the Final Cut Pro interface, having your app’s functionality within the interface provides a seamless user experience.

You must use a macOS app to contain and deliver your workflow extension. The app that contains the extension is called the *container app*.

When a user launches an extension, Final Cut Pro hosts the extension in its interface, inside a floating window, and becomes the *host app*. However, the amount of information a workflow extension presents in a floating window space may not be sufficient for complex tasks. Create an extension for workflows that are optimized for limited screen size; for example, managing media files, and browsing and accessing stock footage. Delegate time-consuming or complicated tasks to the container app.

![Screenshot showing a workflow extension inside a floating window in the Final Cut Pro interface.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3570238@2x.png)

You can extend a workflow extension’s functionality beyond data exchange by using the libraries provided in the Workflow Extension SDK. The libraries facilitate a workflow extension’s interaction and communication with the Final Cut Pro timeline. You can use the APIs in the SDK to support workflows that allow users to collaborate in real time on a project opened in both Final Cut Pro and the workflow extension.

## Topics

### Essentials
- [Designing Workflow Extensions](./designing-workflow-extensions.md)
  Follow these design guidelines to provide a unique experience to workflow extension users.
- [Building a Workflow Extension](./building-a-workflow-extension.md)
  Create a workflow extension in Xcode by using the Final Cut Pro Workflow Extension template.
### Information Property List Keys
- [ProExtensionPrincipalViewControllerClass](../BundleResources/information-property-list/nsextension/proextensionprincipalviewcontrollerclass.md)
  The name of the principal view controller class of your extension.
- [ProExtensionAttributes](../BundleResources/information-property-list/nsextension/proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
### FCPX Interactions
- [Interacting with the Final Cut Pro Timeline](./interacting-with-the-final-cut-pro-timeline.md)
  Extend your workflows beyond media exchange by enabling a workflow extension to interact with the Final Cut Pro timeline.
- [protocol FCPXHost](../professional_video_applications/fcpxhost.md)
  A protocol that provides an interface to retrieve the Final Cut Pro timeline proxy objects and details of the host app.
- [func ProExtensionHostSingleton() -> (any NSObjectProtocol)?](../professional_video_applications/proextensionhostsingleton%28%29.md)
  Returns the singleton proxy instance of the host object.
- [class FCPXTimeline](../professional_video_applications/fcpxtimeline.md)
  An interface that has methods and properties to communicate and interact with the Final Cut Pro timeline.
- [protocol FCPXTimelineObserver](../professional_video_applications/fcpxtimelineobserver.md)
  An interface with optional methods implemented by observers of [`FCPXTimeline`](../professional_video_applications/fcpxtimeline.md) objects.
### FCPX Timeline Proxy Objects
- [class FCPXObject](../professional_video_applications/fcpxobject.md)
  An abstract superclass for Final Cut Pro timeline proxy objects.
- [enum FCPXObjectType](../professional_video_applications/fcpxobjecttype.md)
  The Final Cut Pro timeline object types.
- [class FCPXLibrary](../professional_video_applications/fcpxlibrary.md)
  An object that contains details of a Final Cut Pro library.
- [class FCPXEvent](../professional_video_applications/fcpxevent.md)
  An object that contains details of an event in the Final Cut Pro library.
- [class FCPXProject](../professional_video_applications/fcpxproject.md)
  An object that contains details of a project with the sequence open in the Final Cut Pro timeline.
- [class FCPXSequence](../professional_video_applications/fcpxsequence.md)
  An object that contains details of a sequence that’s open in the Final Cut Pro timeline.
- [enum FCPXSequenceTimecodeFormat](../professional_video_applications/fcpxsequencetimecodeformat.md)
  The display format of the sequence timecode.

## See Also

### XML Data Exchange
- [Content and Metadata Exchanges with Final Cut Pro](./content-and-metadata-exchanges-with-final-cut-pro.md)
  Send media assets and timeline sequences to Final Cut Pro for editing, and receive rendered media and editing decisions in your app.
- [FCPXML Reference](./fcpxml-reference.md)
  Create documents that describe the data your app or workflow extension exchanges with Final Cut Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/workflow-extensions)*